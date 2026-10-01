#!/usr/bin/env python3
"""Mentor-side workflow tracking; uses only the Python standard library."""

import argparse
import json
from pathlib import Path
import re
import subprocess
import sys
from datetime import datetime, timezone


ROOT = Path(__file__).resolve().parents[1]
STATUSES = {"LOCKED", "ASSIGNED", "IN PROGRESS", "SUBMITTED", "REVIEW", "REVISION", "PASSED"}
CHECKS = ("theory", "hands_on", "test", "review")
MASTERY = ("explain", "read", "predict", "write", "find_mistakes", "debug", "combine", "solve_independently")
TRANSITIONS = {
    "LOCKED": {"ASSIGNED"},
    "ASSIGNED": {"IN PROGRESS"},
    "IN PROGRESS": {"SUBMITTED"},
    "SUBMITTED": {"REVIEW"},
    "REVIEW": {"REVIEW", "REVISION", "PASSED"},
    "REVISION": {"IN PROGRESS"},
    "PASSED": set(),
}


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def read(root=ROOT):
    catalog = json.loads((root / "curriculum/catalog.json").read_text(encoding="utf-8"))
    progress = json.loads((root / "progress.json").read_text(encoding="utf-8"))
    validate(catalog, progress, root)
    return catalog, progress


def relative_path(root, value):
    if not isinstance(value, str) or not value or Path(value).is_absolute():
        raise ValueError("Paths must be nonempty and relative to the repository.")
    path = (root / value).resolve()
    if not path.is_relative_to(root.resolve()) or ".." in Path(value).parts:
        raise ValueError("Paths must stay inside the repository.")
    return path


def validate(catalog, progress, root=ROOT):
    if catalog.get("schema_version") != 1 or progress.get("schema_version") != 1:
        raise ValueError("Unsupported schema version.")
    if progress.get("mentor") != "Naresh" or progress.get("learner") != "Raajashree":
        raise ValueError("Mentor and learner names do not match this program.")
    for gate in ("system_approved", "first_task_authorized"):
        if type(progress.get(gate)) is not bool:
            raise ValueError(f"{gate} must be true or false.")
    if progress["first_task_authorized"] and not progress["system_approved"]:
        raise ValueError("Approve the system before authorizing the first task.")
    levels = catalog.get("levels", [])
    if [level["id"] for level in levels] != list(range(19)):
        raise ValueError("The catalog must include levels 0 through 18 in order.")
    seen = set()
    paths = set()
    tasks = catalog.get("tasks", [])
    if not tasks or tasks[0]["id"] != "PY-001":
        raise ValueError("The curriculum must start with PY-001.")
    for task in tasks:
        task_id = task["id"]
        if not re.fullmatch(r"(?:PY-\d{3}|PRJ-\d{3}|CP-\d{2}|CAP-\d{3})", task_id) or task_id in seen:
            raise ValueError(f"Invalid or duplicate task ID: {task_id}")
        if task["kind"] not in {"concept", "project", "checkpoint", "capstone"}:
            raise ValueError(f"Unknown task kind: {task_id}")
        if task["level"] not in range(19) or not task.get("topic"):
            raise ValueError(f"Invalid level or topic: {task_id}")
        minimum, maximum = task["hours"]
        if not 0 < minimum <= maximum or not 0 < task["pass_score"] <= 100:
            raise ValueError(f"Invalid time budget or pass threshold: {task_id}")
        relative_path(root, task["path"])
        if task["path"] in paths:
            raise ValueError(f"Duplicate task path: {task_id}")
        if len(task["prerequisites"]) != len(set(task["prerequisites"])):
            raise ValueError(f"Duplicate prerequisite: {task_id}")
        if any(dependency not in seen for dependency in task["prerequisites"]):
            raise ValueError(f"Prerequisites must reference earlier tasks: {task_id}")
        if seen and not task["prerequisites"]:
            raise ValueError(f"Only PY-001 may have no prerequisites: {task_id}")
        seen.add(task_id)
        paths.add(task["path"])
    if set(progress.get("tasks", {})) != seen:
        raise ValueError("Progress task IDs must exactly match the catalog.")
    active = []
    for task in tasks:
        task_id = task["id"]
        record = progress["tasks"][task_id]
        status = record.get("status")
        if status not in STATUSES:
            raise ValueError(f"Invalid status: {task_id}")
        if set(record.get("checks", {})) != set(CHECKS) or any(
            type(value) is not bool for value in record["checks"].values()
        ):
            raise ValueError(f"Checks must contain four booleans: {task_id}")
        score = record.get("score")
        if score is not None and (type(score) is not int or not 0 <= score <= 100):
            raise ValueError(f"Score must be an integer from 0 to 100: {task_id}")
        mastery = record.get("mastery", [])
        if not isinstance(mastery, list) or len(mastery) != len(set(mastery)) or set(mastery) - set(MASTERY):
            raise ValueError(f"Invalid mastery evidence categories: {task_id}")
        commit = record.get("submission_commit")
        if commit is not None and not re.fullmatch(r"[0-9a-f]{40}", commit):
            raise ValueError(f"Submission commit must be a full Git SHA: {task_id}")
        if not isinstance(record.get("history"), list):
            raise ValueError(f"Task history must be a list: {task_id}")
        if status != "LOCKED":
            if not progress["first_task_authorized"]:
                raise ValueError(f"Assignment requires both mentor approvals: {task_id}")
            if any(progress["tasks"][dep]["status"] != "PASSED" for dep in task["prerequisites"]):
                raise ValueError(f"Unpassed prerequisite: {task_id}")
        if status not in {"LOCKED", "PASSED"}:
            active.append(task_id)
        if status in {"SUBMITTED", "REVIEW", "REVISION", "PASSED"} and not commit:
            raise ValueError(f"Submitted work needs a commit: {task_id}")
        review = record.get("review_path")
        if review is not None:
            review_file(root, task, review)
        if status in {"REVISION", "PASSED"} and not review:
            raise ValueError(f"Decision requires a review file: {task_id}")
        if status == "PASSED":
            if score is None or score < task["pass_score"]:
                raise ValueError(f"Pass threshold not reached: {task_id}")
            if not all(record["checks"].values()) or set(mastery) != set(MASTERY):
                raise ValueError(f"All checks and mastery criteria must be verified: {task_id}")
    if len(active) > 1:
        raise ValueError("Only one assignment may be active at a time.")


def review_file(root, task, value):
    path = relative_path(root, value)
    task_path = relative_path(root, task["path"])
    if not path.is_relative_to(task_path) or not path.is_file() or not path.read_text(encoding="utf-8").strip():
        raise ValueError("The review must be a nonempty file inside this task folder.")
    return path


def verify_commit(root, value):
    if not value or not re.fullmatch(r"[0-9a-f]{40}", value):
        raise ValueError("Provide --commit with a full 40-character Git SHA.")
    result = subprocess.run(
        ["git", "cat-file", "-e", value + "^{commit}"], cwd=root,
        capture_output=True, text=True, check=False,
    )
    if result.returncode:
        raise ValueError("The submission commit is not available in this local Git repository.")


def gate(progress):
    if not progress["system_approved"]:
        return "Waiting for Naresh to approve the mentorship system. No task may be assigned."
    if not progress["first_task_authorized"]:
        return "System approved; waiting for Naresh to explicitly authorize PY-001."
    return None


def next_task(catalog, progress):
    blocked = gate(progress)
    if blocked:
        return blocked
    for task in catalog["tasks"]:
        status = progress["tasks"][task["id"]]["status"]
        if status not in {"LOCKED", "PASSED"}:
            return f"{task['id']} — {task['topic']}: {status}. Finish review/revision before advancing."
    for task in catalog["tasks"]:
        if progress["tasks"][task["id"]]["status"] == "LOCKED" and all(
            progress["tasks"][dep]["status"] == "PASSED" for dep in task["prerequisites"]
        ):
            return f"Eligible for preparation: {task['id']} — {task['topic']}. Naresh must assign it."
    return "All catalog tasks have passed. Naresh can plan further specialization."


def approve(progress, action, actor):
    if actor != progress["mentor"]:
        raise ValueError("Only Naresh can record mentor approval.")
    field = "system_approved" if action == "approve-system" else "first_task_authorized"
    if field == "first_task_authorized" and not progress["system_approved"]:
        raise ValueError("Approve the system first.")
    if progress[field]:
        raise ValueError("This approval is already recorded.")
    progress[field] = True
    progress["decisions"].append({"at": now(), "by": actor, "action": action})


def record(catalog, progress, args, root=ROOT):
    task = next((task for task in catalog["tasks"] if task["id"] == args.task_id), None)
    if task is None:
        raise ValueError(f"Unknown task: {args.task_id}")
    state = progress["tasks"][args.task_id]
    target = args.status
    if args.by not in {progress["mentor"], progress["learner"]}:
        raise ValueError("The recorded author must be Naresh or Raajashree.")
    if target in {"ASSIGNED", "REVIEW", "REVISION", "PASSED"} and args.by != progress["mentor"]:
        raise ValueError("Only Naresh may assign, review, or decide advancement.")
    if target not in TRANSITIONS[state["status"]]:
        raise ValueError(f"Cannot move from {state['status']} to {target}.")
    if target == "ASSIGNED":
        if gate(progress):
            raise ValueError(gate(progress))
        if any(progress["tasks"][dep]["status"] != "PASSED" for dep in task["prerequisites"]):
            raise ValueError("Every prerequisite must pass before assignment.")
        if any(item["status"] not in {"LOCKED", "PASSED"} for item in progress["tasks"].values()):
            raise ValueError("Finish the active assignment first.")
        material = relative_path(root, task["path"]) / "README.md"
        if not material.is_file() or not material.read_text(encoding="utf-8").strip():
            raise ValueError("Prepare the learner README in the catalog task folder before assignment.")
    if args.commit:
        if target != "SUBMITTED":
            raise ValueError("Record the submission commit only when moving to SUBMITTED.")
        verify_commit(root, args.commit)
        if any(event.get("to") == "SUBMITTED" and event.get("submission_commit") == args.commit
               for event in state["history"]):
            raise ValueError("A revised submission needs a new commit containing the corrections.")
        state["submission_commit"] = args.commit
    elif target == "SUBMITTED":
        raise ValueError("Every submission, including a revision, needs --commit.")
    if (args.check or args.mastery or args.score is not None or args.review) and (
        args.by != progress["mentor"] or target not in {"REVIEW", "REVISION", "PASSED"}
    ):
        raise ValueError("Only Naresh can record assessment evidence during review or a decision.")
    if args.review:
        review_file(root, task, args.review)
        state["review_path"] = args.review
    if args.score is not None:
        state["score"] = args.score
    for check in args.check:
        state["checks"][check] = True
    if args.mastery:
        state["mastery"] = list(MASTERY) if "all" in args.mastery else sorted(set(args.mastery))
    if target == "REVISION" and not args.review:
        raise ValueError("Provide --review with specific corrections and reassessment requirements.")
    # A resubmission must be assessed afresh; earlier checks do not prove corrections.
    if state["status"] == "REVISION" and target == "IN PROGRESS":
        state.update(checks=dict.fromkeys(CHECKS, False), score=None, mastery=[],
                     submission_commit=None, review_path=None)
    previous = state["status"]
    state["status"] = target
    state["history"].append({
        "at": now(), "by": args.by, "from": previous, "to": target,
        "submission_commit": state["submission_commit"], "review_path": state["review_path"],
        "score": state["score"], "checks": dict(state["checks"]), "mastery": list(state["mastery"]),
    })
    validate(catalog, progress, root)


def write_progress(progress, root=ROOT):
    temporary = root / "progress.json.tmp"
    temporary.write_text(json.dumps(progress, indent=2) + "\n", encoding="utf-8")
    temporary.replace(root / "progress.json")


def render(catalog, progress, root=ROOT):
    validate(catalog, progress, root)
    roadmap = [
        "# Python roadmap", "", "Generated from `catalog.json` with `python3 tools/track.py render`.", "",
        "This is the complete planned curriculum, not a set of issued assignments. Each concept",
        "gets its own learner task when eligible. The sequence is deliberately conservative:",
        "pass the named prerequisite before preparing and assigning the next task. Projects",
        "and checkpoints also gate advancement. Consult progress.md for current task states.", "",
        "Hours are planning ranges for study, exercises, assessment, and review; revision may",
        "add time. See [mentorship](../docs/mentorship.md) for pacing and [assessment](../docs/assessment.md)",
        "for checkpoint requirements. Repeat advanced topics deepen earlier foundations.", "",
    ]
    for level in catalog["levels"]:
        level_tasks = [task for task in catalog["tasks"] if task["level"] == level["id"]]
        hours = [sum(task["hours"][index] for task in level_tasks) for index in (0, 1)]
        roadmap += [f"## Level {level['id']} — {level['title']}", "",
                    f"Budget: {hours[0]}–{hours[1]} hours. Folder: `{level['folder']}/`.", "",
                    "| ID | Topic | Type | Prerequisite | Hours | Git location |",
                    "|---|---|---|---|---|---|"]
        for task in level_tasks:
            deps = ", ".join(task["prerequisites"]) or "Mentor approvals"
            roadmap.append(f"| {task['id']} | {task['topic']} | {task['kind']} | {deps} | "
                           f"{task['hours'][0]}–{task['hours'][1]} | `{task['path']}/` |")
        roadmap.append("")
    total = [sum(task["hours"][index] for task in catalog["tasks"]) for index in (0, 1)]
    roadmap += [f"Total planned budget: **{total[0]}–{total[1]} hours**, excluding additional revision.", ""]
    (root / "curriculum/roadmap.md").write_text("\n".join(roadmap), encoding="utf-8")
    counts = {status: sum(item["status"] == status for item in progress["tasks"].values())
              for status in sorted(STATUSES)}
    lines = ["# Learning progress", "", "Generated from `progress.json`; do not edit this table directly.", "",
             f"Mentor: **{progress['mentor']}**. Learner: **{progress['learner']}**.", "",
             f"System approved: **{'yes' if progress['system_approved'] else 'no'}**. "
             f"First task authorized: **{'yes' if progress['first_task_authorized'] else 'no'}**.", "",
             next_task(catalog, progress), "",
             "; ".join(f"{status}: {count}" for status, count in counts.items()) + ".", "",
             "A dash means not verified. Checks are confirmed by Naresh from submission evidence.",
             "An eligible but unassigned task remains LOCKED. Scores alone cannot produce PASSED.", "",
             "| ID | Topic | Status | Theory | Hands-on | Test | Review | Score |",
             "|---|---|---|---|---|---|---|---|"]
    for task in catalog["tasks"]:
        state = progress["tasks"][task["id"]]
        checks = " | ".join("✓" if state["checks"][name] else "-" for name in CHECKS)
        score = "-" if state["score"] is None else str(state["score"])
        lines.append(f"| {task['id']} | {task['topic']} | {state['status']} | {checks} | {score} |")
    (root / "progress.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("show", "next", "validate", "render"):
        commands.add_parser(name)
    for name in ("approve-system", "authorize-first-task"):
        command = commands.add_parser(name)
        command.add_argument("--by", required=True)
    command = commands.add_parser("record")
    command.add_argument("task_id")
    command.add_argument("status", choices=sorted(STATUSES))
    command.add_argument("--by", required=True)
    command.add_argument("--commit")
    command.add_argument("--review")
    command.add_argument("--score", type=int)
    command.add_argument("--check", action="append", choices=CHECKS, default=[])
    command.add_argument("--mastery", action="append", choices=(*MASTERY, "all"), default=[])
    args = parser.parse_args()
    try:
        catalog, progress = read()
        if args.command == "validate":
            print(f"Valid: {len(catalog['tasks'])} catalog tasks and matching progress records.")
        elif args.command == "next":
            print(next_task(catalog, progress))
        elif args.command == "show":
            print(next_task(catalog, progress))
            for task_id, state in progress["tasks"].items():
                if state["status"] != "LOCKED":
                    print(f"{task_id}: {state['status']}")
        else:
            if args.command in {"approve-system", "authorize-first-task"}:
                approve(progress, args.command, args.by)
            elif args.command == "record":
                record(catalog, progress, args)
            if args.command != "render":
                validate(catalog, progress)
                write_progress(progress)
            render(catalog, progress)
            print("Updated generated roadmap and progress." if args.command == "render"
                  else "Recorded decision and updated progress. Review the Git diff before committing.")
    except (ValueError, KeyError, TypeError, OSError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
