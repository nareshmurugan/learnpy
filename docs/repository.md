# Repository and task structure

The catalog determines each task's exact Git location. Topic folders are created
when a task is prepared, avoiding empty lesson directories that look like issued
work. The initial `projects/` and `assessments/` indexes explain future preparation.

```text
learnpy/
├── plan.md
├── README.md
├── AGENTS.md
├── curriculum/
│   ├── catalog.json       # Authoritative IDs, concepts, dependencies, time budgets
│   └── roadmap.md         # Generated readable roadmap
├── progress.json          # Authoritative decisions and task states
├── progress.md            # Generated table
├── knowledge.md           # Reviewed conceptual strengths and revision needs
├── docs/
├── templates/
├── tools/
├── tests/                 # Mentor tooling tests, not learner assessment answers
├── foundations/           # Created when PY-001 is prepared
│   └── PY-001-python-setup/
├── fundamentals/          # Then other topic folders listed in the catalog
├── assessments/
├── projects/
└── mentor-private/        # Ignored; not a shared or backed-up answer store
```

## Each concept task

```text
<catalog-task-path>/
├── README.md               # Learner assignment and complete study material
├── examples/               # Teaching examples, not exercise implementations
├── exercises/
│   ├── README.md           # A–E instructions and filenames
│   └── <learner scripts>
├── hands-on/
│   ├── README.md           # Practical challenge requirements
│   └── <learner implementation>
├── test/
│   ├── README.md           # Theory, prediction, debugging, coding, explanation
│   ├── answers.md          # Learner-written answers
│   └── <learner assessment scripts>
└── notes/
    ├── study.md            # Learner notes and unknowns
    ├── explanation.md      # Learner code reasoning and observed runs
    ├── submission.md       # Deliverables, testing, and assistance disclosure
    ├── review.md           # Mentor feedback; no reference answer key
    └── revisions/          # Focused correction tasks and review records
```

Use `.gitkeep` only when an assignment actually needs an otherwise empty folder.
Do not create completed learner answers, dummy runs, or placeholder code on her
behalf. Copy templates and fill assignment instructions; Raajashree writes answers.
The mentor creates a real, nonempty learner README before marking ASSIGNED.

Projects and checkpoints use a similar structure, with `requirements.md` and
`planning.md` as appropriate. Introduce packages and automated test directories
when those skills are taught; early work remains simple `.py` files.

## Private evaluation material

Tracked blank [mentor-guide templates](../templates/mentor-guide.md) contain no
answers. Filled answer keys go in `mentor-private/<task-id>/evaluation.md` or a
separate private mentor repository. Shared `notes/review.md` contains feedback,
evidence, scores, verbal verification results, and required corrections. Keep
future answers and complete reference implementations out of that feedback.

`.gitignore` prevents normal accidental addition; it is not access control and
cannot hide files already committed or deliberately force-added. Naresh should
keep the private working location inaccessible to the learner and back it up
separately. Check `git diff --cached` before committing to the shared repository.
