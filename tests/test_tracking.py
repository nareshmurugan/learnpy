"""Behavior tests for progression gates; never learner assessment solutions."""

import argparse
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


REPO = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("track", REPO / "tools/track.py")
track = importlib.util.module_from_spec(spec)
spec.loader.exec_module(track)


class TrackingTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.catalog = json.loads((REPO / "curriculum/catalog.json").read_text())
        self.progress = {
            "schema_version": 1, "mentor": "Naresh", "learner": "Raajashree",
            "system_approved": False, "first_task_authorized": False, "decisions": [],
            "tasks": {
                task["id"]: {
                    "status": "LOCKED", "checks": dict.fromkeys(track.CHECKS, False),
                    "score": None, "mastery": [], "submission_commit": None,
                    "review_path": None, "history": [],
                } for task in self.catalog["tasks"]
            },
        }
        self.task = self.catalog["tasks"][0]
        self.task_folder = self.root / self.task["path"]

    def args(self, status, task_id="PY-001", by="Naresh", **kwargs):
        values = dict(task_id=task_id, status=status, by=by, commit=None,
                      review=None, score=None, check=[], mastery=[])
        values.update(kwargs)
        return argparse.Namespace(**values)

    def record(self, status, **kwargs):
        # Match the CLI's load/validate/save boundary: failed actions never persist.
        candidate = copy.deepcopy(self.progress)
        track.record(self.catalog, candidate, self.args(status, **kwargs), self.root)
        self.progress = candidate

    def approvals(self):
        track.approve(self.progress, "approve-system", "Naresh")
        track.approve(self.progress, "authorize-first-task", "Naresh")

    def prepare(self):
        self.task_folder.mkdir(parents=True)
        (self.task_folder / "README.md").write_text("Test fixture learner material.")

    def submit_and_review(self):
        self.approvals()
        self.prepare()
        self.record("ASSIGNED")
        self.record("IN PROGRESS", by="Raajashree")
        with patch.object(track, "verify_commit"):
            self.record("SUBMITTED", by="Raajashree", commit="a" * 40)
        self.record("REVIEW")
        review = self.task_folder / "notes/review.md"
        review.parent.mkdir()
        review.write_text("Fixture mentor feedback about the submitted revision.")
        return str(review.relative_to(self.root))

    def pass_args(self, **kwargs):
        values = dict(score=80, check=list(track.CHECKS), mastery=["all"])
        values.update(kwargs)
        return values

    def test_fresh_state_and_next_do_not_advance(self):
        before = copy.deepcopy(self.progress)
        track.validate(self.catalog, self.progress, self.root)
        self.assertIn("approve", track.next_task(self.catalog, self.progress))
        self.assertEqual(before, self.progress)
        self.assertTrue(all(item["status"] == "LOCKED" for item in self.progress["tasks"].values()))

    def test_approval_order_and_mentor_authority(self):
        with self.assertRaisesRegex(ValueError, "Approve the system first"):
            track.approve(self.progress, "authorize-first-task", "Naresh")
        with self.assertRaisesRegex(ValueError, "Only Naresh"):
            track.approve(self.progress, "approve-system", "Raajashree")
        track.approve(self.progress, "approve-system", "Naresh")
        self.assertIn("explicitly authorize", track.next_task(self.catalog, self.progress))
        with self.assertRaisesRegex(ValueError, "already recorded"):
            track.approve(self.progress, "approve-system", "Naresh")

    def test_assignment_requires_approvals_and_prepared_material(self):
        with self.assertRaisesRegex(ValueError, "approve"):
            self.record("ASSIGNED")
        self.approvals()
        with self.assertRaisesRegex(ValueError, "Prepare"):
            self.record("ASSIGNED")
        self.prepare()
        self.record("ASSIGNED")
        self.assertIn("ASSIGNED", track.next_task(self.catalog, self.progress))

    def test_unpassed_prerequisite_blocks_second_task(self):
        self.approvals()
        with self.assertRaisesRegex(ValueError, "prerequisite"):
            self.record("ASSIGNED", task_id=self.catalog["tasks"][1]["id"])

    def test_status_jumps_and_nonmentor_decisions_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "Cannot move"):
            self.record("PASSED")
        with self.assertRaisesRegex(ValueError, "Only Naresh"):
            self.record("ASSIGNED", by="Raajashree")
        with self.assertRaisesRegex(ValueError, "recorded author"):
            self.record("IN PROGRESS", by="Unknown")

    def test_submission_requires_new_commit_and_cannot_become_pass(self):
        self.approvals()
        self.prepare()
        self.record("ASSIGNED")
        self.record("IN PROGRESS", by="Raajashree")
        with self.assertRaisesRegex(ValueError, "needs --commit"):
            self.record("SUBMITTED", by="Raajashree")
        with patch.object(track, "verify_commit"):
            self.record("SUBMITTED", by="Raajashree", commit="a" * 40)
        with self.assertRaisesRegex(ValueError, "Cannot move"):
            self.record("PASSED")
        self.assertIn("SUBMITTED", track.next_task(self.catalog, self.progress))

    def test_score_alone_and_incomplete_mastery_cannot_pass(self):
        review = self.submit_and_review()
        with self.assertRaisesRegex(ValueError, "All checks"):
            self.record("PASSED", score=100, review=review)
        with self.assertRaisesRegex(ValueError, "All checks"):
            self.record("PASSED", review=review, score=100, check=list(track.CHECKS), mastery=["explain"])
        with self.assertRaisesRegex(ValueError, "Pass threshold"):
            self.record("PASSED", review=review, **self.pass_args(score=79))
        self.assertEqual(self.progress["tasks"]["PY-001"]["status"], "REVIEW")

    def test_review_requires_nonempty_task_local_file(self):
        self.submit_and_review()
        with self.assertRaisesRegex(ValueError, "inside this task"):
            self.record("PASSED", review="missing.md", **self.pass_args())
        outside = self.root / "other-review.md"
        outside.write_text("Wrong task.")
        with self.assertRaisesRegex(ValueError, "inside this task"):
            self.record("PASSED", review="other-review.md", **self.pass_args())
        with self.assertRaisesRegex(ValueError, "inside the repository"):
            self.record("PASSED", review="../review.md", **self.pass_args())

    def test_full_evidence_pass_unlocks_next_without_assigning_it(self):
        review = self.submit_and_review()
        self.record("PASSED", review=review, **self.pass_args())
        next_id = self.catalog["tasks"][1]["id"]
        self.assertIn(next_id, track.next_task(self.catalog, self.progress))
        self.assertEqual(self.progress["tasks"][next_id]["status"], "LOCKED")

    def test_revision_preserves_history_but_resets_assessment(self):
        review = self.submit_and_review()
        self.record("REVISION", review=review, score=60, check=["theory"], mastery=["explain"])
        self.record("IN PROGRESS", by="Raajashree")
        state = self.progress["tasks"]["PY-001"]
        self.assertFalse(any(state["checks"].values()))
        self.assertEqual(state["mastery"], [])
        self.assertIsNone(state["score"])
        self.assertIsNone(state["submission_commit"])
        self.assertIsNone(state["review_path"])
        previous = state["history"][-2]
        self.assertEqual(previous["submission_commit"], "a" * 40)
        self.assertEqual(previous["review_path"], review)
        with patch.object(track, "verify_commit"):
            with self.assertRaisesRegex(ValueError, "new commit"):
                self.record("SUBMITTED", by="Raajashree", commit="a" * 40)
            self.record("SUBMITTED", by="Raajashree", commit="b" * 40)
        self.assertEqual(self.progress["tasks"]["PY-001"]["submission_commit"], "b" * 40)

    def test_checkpoint_and_capstone_have_higher_thresholds(self):
        self.assertTrue(all(task["pass_score"] == 85 for task in self.catalog["tasks"]
                            if task["kind"] == "checkpoint"))
        self.assertEqual(self.catalog["tasks"][-1]["pass_score"], 90)
        # Exercise threshold enforcement on a review fixture without skipping predecessors.
        review = self.submit_and_review()
        self.catalog["tasks"][0]["pass_score"] = 85
        with self.assertRaisesRegex(ValueError, "Pass threshold"):
            self.record("PASSED", review=review, **self.pass_args(score=84))
        self.record("PASSED", review=review, **self.pass_args(score=85))

    def test_catalog_cycles_duplicates_and_state_mismatches_are_rejected(self):
        bad = copy.deepcopy(self.catalog)
        bad["tasks"][0]["prerequisites"] = [bad["tasks"][1]["id"]]
        with self.assertRaisesRegex(ValueError, "earlier tasks"):
            track.validate(bad, self.progress, self.root)
        bad = copy.deepcopy(self.catalog)
        bad["tasks"][1]["id"] = "PY-001"
        with self.assertRaisesRegex(ValueError, "duplicate task ID"):
            track.validate(bad, self.progress, self.root)
        self.progress["tasks"].pop("PY-001")
        with self.assertRaisesRegex(ValueError, "exactly match"):
            track.validate(self.catalog, self.progress, self.root)

    def test_render_is_deterministic_and_keeps_state_unchanged(self):
        (self.root / "curriculum").mkdir()
        before = copy.deepcopy(self.progress)
        track.render(self.catalog, self.progress, self.root)
        first = (self.root / "progress.md").read_bytes()
        roadmap = (self.root / "curriculum/roadmap.md").read_bytes()
        track.render(self.catalog, self.progress, self.root)
        self.assertEqual(first, (self.root / "progress.md").read_bytes())
        self.assertEqual(roadmap, (self.root / "curriculum/roadmap.md").read_bytes())
        self.assertEqual(before, self.progress)

    def test_cli_real_git_submission_and_failed_action_persistence(self):
        (self.root / "curriculum").mkdir()
        (self.root / "tools").mkdir()
        (self.root / "tools/track.py").write_bytes((REPO / "tools/track.py").read_bytes())
        (self.root / "curriculum/catalog.json").write_text(json.dumps(self.catalog))
        (self.root / "progress.json").write_text(json.dumps(self.progress))

        def cli(*arguments):
            return subprocess.run([sys.executable, "tools/track.py", *arguments], cwd=self.root,
                                  capture_output=True, text=True, check=False)

        initial = (self.root / "progress.json").read_bytes()
        self.assertEqual(cli("record", "PY-001", "ASSIGNED", "--by", "Naresh").returncode, 1)
        self.assertEqual(initial, (self.root / "progress.json").read_bytes())
        for action in ("approve-system", "authorize-first-task"):
            result = cli(action, "--by", "Naresh")
            self.assertEqual(result.returncode, 0, result.stderr)
        self.prepare()
        for status in ("ASSIGNED", "IN PROGRESS"):
            result = cli("record", "PY-001", status, "--by", "Naresh")
            self.assertEqual(result.returncode, 0, result.stderr)
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True, capture_output=True)
        subprocess.run(["git", "add", "."], cwd=self.root, check=True, capture_output=True)
        subprocess.run(["git", "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                        "-c", "commit.gpgsign=false", "commit", "-qm", "Fixture submission"],
                       cwd=self.root, check=True, capture_output=True)
        before = (self.root / "progress.json").read_bytes()
        result = cli("record", "PY-001", "SUBMITTED", "--by", "Raajashree", "--commit", "0" * 40)
        self.assertEqual(result.returncode, 1)
        self.assertEqual(before, (self.root / "progress.json").read_bytes())
        sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=self.root, text=True).strip()
        result = cli("record", "PY-001", "SUBMITTED", "--by", "Raajashree", "--commit", sha)
        self.assertEqual(result.returncode, 0, result.stderr)
        saved = json.loads((self.root / "progress.json").read_text())
        self.assertEqual(saved["tasks"]["PY-001"]["status"], "SUBMITTED")
        self.assertEqual(saved["tasks"]["PY-001"]["submission_commit"], sha)


if __name__ == "__main__":
    unittest.main()
