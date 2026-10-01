# Recording progress

`curriculum/catalog.json` is the curriculum source; `progress.json` is the state
source. `curriculum/roadmap.md` and `progress.md` are generated views. Use the
tracker from the repository root and commit state plus generated views together.
Read-only commands never alter progress.

```bash
python3 tools/track.py show
python3 tools/track.py next
python3 tools/track.py validate
python3 tools/track.py render
```

`render` refreshes documentation but never issues lessons, passes tasks, or changes
knowledge ratings. If catalog IDs change, update progress IDs explicitly too;
validation rejects mismatches. Preserve issued IDs and reviewed history.

## Approval records

These commands are for **after Naresh has actually approved the system and
explicitly requested PY-001**. They have not been executed in this implementation.

```bash
python3 tools/track.py approve-system --by Naresh
python3 tools/track.py authorize-first-task --by Naresh
```

This is a local cooperative workflow, not user authentication. `--by Naresh`
records an assertion about the decision maker. Repository permissions and Naresh's
review provide authority; the script cannot prove the caller's identity.

## State transitions

```text
LOCKED → ASSIGNED → IN PROGRESS → SUBMITTED → REVIEW → PASSED
                                                 └→ REVISION
                                                      └→ IN PROGRESS → ...
```

| Status | Meaning and gate |
|---|---|
| LOCKED | Unassigned; `next` distinguishes eligible preparation from unmet prerequisites |
| ASSIGNED | Both approvals recorded, prerequisites passed, learner README prepared, Naresh assigns |
| IN PROGRESS | Learner is doing the assignment or its focused revision |
| SUBMITTED | Learner names a full commit SHA available in the mentor's local repository |
| REVIEW | Naresh reviews that commit and may record verified evidence |
| REVISION | Naresh provides a task-local review file with corrections and reassessment requirements |
| PASSED | Threshold, all checks, all mastery criteria, submission commit, review file, Naresh's decision |

Only one assignment can be active. PASSED has no transition that silently revokes
history. If retention problems appear later, record them in `knowledge.md` and
the current task's revision work, keeping earlier evidence intact.

## Example future task workflow

The following commands are documentation, not a current assignment. They will
fail until the approvals and complete task material exist.

```bash
python3 tools/track.py record PY-001 ASSIGNED --by Naresh
python3 tools/track.py record PY-001 'IN PROGRESS' --by Raajashree
```

After Raajashree has committed and pushed, Naresh obtains the reviewed commit
locally. Replace `FULL_SUBMISSION_SHA` with its real 40-character SHA.

```bash
python3 tools/track.py record PY-001 SUBMITTED --by Raajashree --commit FULL_SUBMISSION_SHA
python3 tools/track.py record PY-001 REVIEW --by Naresh
```

Prepare `foundations/PY-001-python-setup/notes/review.md` using the review template,
including the commit, actual findings, verbal verification, score, and decision.
The file must be nonempty and inside the task folder. Feedback is learner-visible;
keep private answers elsewhere. Verify the score against the rubric and confirm
the complete submission has been pushed.

For a genuine pass, replace `VERIFIED_SCORE` with the actual integer score:

```bash
python3 tools/track.py record PY-001 PASSED --by Naresh \
  --review foundations/PY-001-python-setup/notes/review.md \
  --score VERIFIED_SCORE \
  --check theory --check hands_on --check test --check review \
  --mastery all
```

`--mastery all` is a mentor assertion that all eight criteria were demonstrated;
do not use it as a shortcut. Alternatively repeat `--mastery` with individual
names: `explain`, `read`, `predict`, `write`, `find_mistakes`, `debug`, `combine`,
and `solve_independently`. `record ... REVIEW` can be repeated to record partial
evidence while review remains open. `--check` records mentor-verified completion.

For a demonstrated gap:

```bash
python3 tools/track.py record PY-001 REVISION --by Naresh \
  --review foundations/PY-001-python-setup/notes/review.md
```

Issue the focused revision in `notes/revisions/`, then record IN PROGRESS. This
resets checks, score, mastery, and current submission/review references. The
previous commit, review, and evidence remain in history. The new SUBMITTED action
requires a different commit; Naresh verifies that it contains the corrections.
The tracker rejects reusing an earlier submission commit for the same task.

## Evidence limits and errors

The tracker verifies local Git commit existence but does not run learner programs,
inspect submission contents, verify push success, authenticate authors, or infer
mastery. Review actual deliverables and explanations before recording checks.
It rejects missing prerequisites, unsupported status jumps, incomplete evidence,
low scores, non-mentor decisions, paths outside the task, and inconsistent state.
A rejected CLI action does not save progress.

Decision timestamps are stored in UTC with an explicit offset; use local time when
discussing review sessions. No calendar reminders or external messages are created.
`knowledge.md` is deliberately edited by Naresh/AI from actual review evidence;
status or score alone cannot automatically classify a concept as Strong or Weak.
