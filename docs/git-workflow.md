# Git workflow

Git is part of the learning, and every completed task must be committed and pushed
to `learnpy`. Naresh initially sets up Python, Git credentials, the existing local
checkout, and the repository's current branch. Raajashree learns only these five
Git operations first: `status`, `pull`, `add`, `commit`, and `push`.

## Raajashree's first workflow

Run from the repository root. Replace the task path below with the assigned
catalog location; these are workflow instructions, not a current assignment.

```bash
git status
git pull
```

Pull before editing when the working tree is clean. Read the task, complete work,
run each program, record the expected and observed results, and explain solutions.

```bash
git status
git add foundations/PY-001-python-setup/
git commit -m "learn(PY-001): complete setup exercises"
git push
git status
```

Use the actual task ID and deliverables in the message. Push success matters;
a local commit is not yet available to Naresh's remote checkout. If Git reports
conflicts or a rejected push, stop and ask Naresh for help. Do not use force push,
discard local files, or repeatedly retry unfamiliar commands. Do not stage the
whole repository or edit progress records on the learner's behalf.

## Commit conventions

| Change | Format |
|---|---|
| Concept exercises | `learn(PY-XXX): complete <topic> exercises` |
| Concept assessment | `test(PY-XXX): complete <topic> assessment` |
| Corrections | `fix(PY-XXX): correct <specific issue>` |
| Project milestone | `project(PRJ-XXX): implement <milestone>` |
| Checkpoint work | `test(CP-XX): complete level <n> checkpoint` |
| Capstone milestone | `project(CAP-001): complete <milestone>` |
| Mentor assignment | `mentor(PY-XXX): assign <topic>` |
| Mentor review | `review(PY-XXX): record pass or revision evidence` |
| System changes | `docs: define mentorship workflow` or `chore: update tracker` |

Avoid `update`, `done`, `final`, or `test` alone. Separate unrelated work. A
submission may contain multiple useful commits; Naresh records the final full
40-character commit SHA being reviewed. Corrections get new commits so feedback
and the learner's response remain visible.

## Naresh's workflow

1. Prepare the eligible task and a private evaluation guide. Inspect shared files
   for accidental solutions. Commit and push the assignment and tracker update.
2. Receive the learner's submission SHA and push confirmation. Fetch/pull the
   submission into the mentor checkout without overwriting local changes.
3. Review that specific revision, run relevant scripts, inspect reasoning, and
   ask verbal verification questions. Distinguish code execution from reasoning.
4. Save feedback inside the task folder, record the decision, update `knowledge.md`,
   inspect the diff and staged files, then commit and push the review.
5. Prepare the next task only after a pass; otherwise issue focused revision.

The tracker records local evidence; it does not push, check the remote, or prove
who authored a commit. Naresh verifies the pushed revision and independent work.
Choose the repository's existing branch; this system does not rename it or commit
anything automatically.

## Later Git progression

After the basic workflow is reliable, teach `.gitignore` and commit hygiene during
modules/project structure; branches and pull requests during the CLI project;
merge and resolving a small supervised conflict during testing;
rebase basics after merge is understood; and GitHub Actions during DevOps. These
have separate task IDs and prerequisite records in the catalog. The `PY-` prefix
identifies a concept in this Python mentorship program, including supporting Git
skills. Never introduce advanced Git as a prerequisite for PY-001.
