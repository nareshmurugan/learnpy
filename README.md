# learnpy

A Python mentorship repository for **Naresh (mentor)** and
**Raajashree (learner)**, from programming foundations to production applications.
The goal is independent understanding and problem solving, not fast completion.

**Current stage: mentorship system prepared for review.** No learner task has been
assigned, no understanding has been assessed, and PY-001 has not been generated.
The original requirements remain in [plan.md](plan.md).

Start with the [complete roadmap](curriculum/roadmap.md),
[mentorship workflow](docs/mentorship.md), and [progress tracker](progress.md).
The [repository guide](docs/repository.md) describes where future work belongs.

## How the program works

1. Naresh reviews and approves this system, then explicitly authorizes PY-001.
2. A complete learner task is prepared using [the task template](templates/task.md).
3. Naresh assigns it after prerequisite checks.
4. Raajashree studies, practices, answers the assessment independently, explains
   her code, and commits and pushes her work.
5. Naresh reviews a specific commit with AI assistance, verifies understanding,
   and decides PASSED or REVISION.
6. Only a pass makes the next dependent task eligible. Revisions come first.

## Mentorship tools

The tracker uses only the Python standard library. Run these mentor-side commands
from the repository root; Raajashree does not need to learn the tool yet.

```bash
python3 tools/track.py show
python3 tools/track.py next
python3 tools/track.py validate
python3 -m unittest discover -s tests -v
```

`next` explains the current gate; it never creates an assignment or advances the
learner. See [the tracking guide](docs/tracking.md) for recording real approvals,
submissions, reviews, and revision decisions.

## Repository map

| Location | Purpose |
|---|---|
| `curriculum/` | Full catalog, prerequisites, generated roadmap |
| `docs/` | Mentorship, Git, assessment, tracking, capstone guides |
| `templates/` | Blank task, submission, review, revision, checkpoint, project templates |
| `progress.json`, `progress.md` | Authoritative state and generated readable tracker |
| `knowledge.md` | Evidence-backed strengths, weaknesses, and revision queue |
| `tools/`, `tests/` | Mentor-side tracking and workflow checks |
| Topic folders | Created when tasks are actually prepared |
| `assessments/`, `projects/` | Checkpoints and milestone work, prepared when eligible |
| `mentor-private/` | Ignored local answer keys; use a separate private store for backups |

Learner documents and examples are shared. Answer keys must stay outside tracked
files. All important learning work, feedback, and corrections belong in Git.
Actual commits and pushes remain deliberate actions by their authors.
