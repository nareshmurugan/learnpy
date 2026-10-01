# Assessment and review

Each concept ends with a learner test and a private mentor guide. Test answers,
exercise solutions, and complete project implementations must not be included in
learner materials. Teaching examples should use different problems.

## Concept test structure

| Section | Evidence | Suggested marks |
|---|---|---|
| A — Theory | Own-word definitions, purpose, and a comparison | 20 |
| B — Predict output | Prediction and execution reasoning before running | 20 |
| C — Find the bug | Cause, repair, and prevention | 20 |
| D — Write code | New problem without implementation or solution hints | 25 |
| E — Explain your code | Approach, behavior, boundaries, alternatives | 15 |

Document per-question marks and acceptable alternatives in the private guide.
Use only taught concepts. During setup, prediction may involve terminal versus
REPL behavior or a tiny `print()` script; do not require later language features.
The section score informs understanding; it does not independently cause a pass.

## Overall review rubric

Use evidence from exercises, the independent test, the practical task, and verbal
questions. Record an overall score out of 100 using the weights below. Code may
have several valid beginner-level implementations.

| Dimension | Weight | What Naresh verifies |
|---|---|---|
| Concept understanding | 20 | Own-word explanation, code reading, output prediction |
| Correctness | 20 | Requirements and expected behavior on representative cases |
| Logic/problem solving | 10 | Chosen approach and independent problem decomposition |
| Debugging | 10 | Bug cause, repair, and verification of the repair |
| Code quality/Python practices | 10 | Meaningful names, clarity, practices already taught |
| Edge cases | 10 | Appropriate boundaries and failure behavior at this level |
| Explanation | 10 | Why the implementation works and how it was tested |
| Git quality | 5 | Correct location, useful commits, complete pushed submission |
| Independence | 5 | Assistance disclosure and successful fresh verbal/code variation |

Classify each area as Strong, Good, Needs Practice, or Weak and support it with a
file, run, answer, or verbal observation. Independence cannot be inferred from
formatting or an AI detector. Ask the learner to explain or adapt a small part.
Do not require generators, decorators, type hints, or frameworks before taught.

## Pass and revision criteria

A normal concept/project requires **at least 80/100 overall**; a level checkpoint
requires **85/100**; the capstone requires **90/100**. Naresh must also confirm all
four evidence checks (theory, hands-on, test, review) and all eight mastery criteria:

1. Explain in her own words.
2. Read unfamiliar code using the concept.
3. Predict its output and explain execution.
4. Write code using it.
5. Identify mistakes involving it.
6. Debug and verify fixes.
7. Combine it with earlier concepts (for PY-001, apply it with the guided setup).
8. Solve a new problem independently without copying the example.

There must be no unresolved core misconception, unfulfilled required behavior,
or unexplained copied solution. A high score does not override these conditions.
Confirm the learner has pushed the complete deliverables, record the reviewed
commit SHA, and save mentor feedback before recording PASSED. If evidence is
missing, request it; if a demonstrated gap remains, record REVISION and prescribe
focused corrections. A submission by itself never implies PASSED.

The tracker enforces status order, thresholds, prerequisites, evidence fields,
and mentor decision labels. It cannot evaluate the truth of explanations,
the completeness of feedback, remote push success, or actual independence.
Those remain Naresh's responsibilities.

## Testing progression

- From foundations onward: predict behavior before running, record the command,
  expected/actual result, and explain differences. Use small manual checks.
- Through fundamentals, control flow, and collections: include normal, boundary,
  and invalid inputs where taught; do not demand untaught exception handling.
- In functions: reason about inputs, returns, and isolated cases. Mentor-side
  checks may test behavior, but do not replace the learner's conceptual test.
- In files and exceptions: use disposable sample data, missing-file cases, and
  explicit error-path explanations.
- At Level 11: introduce assertions, unit tests, pytest, fixtures, parameterization,
  mocks, integration tests, coverage, and test-driven thinking as separate tasks.
- After Level 11: projects include appropriate automated tests. Prefer meaningful
  behavior checks over tests that merely repeat implementation. Coverage is a
  gap-finding tool, not proof of understanding or a stand-alone pass rule.
- At APIs/concurrency/DevOps: deterministic mocks plus controlled integration
  runs, timeouts, error paths, cancellation, and cleanup. Do not require paid
  infrastructure or production credentials to assess a concept.

## Checkpoint schedule

Prepare **CP-00 through CP-18**, one after each level's concepts and milestone
project. Each combines theory, prediction, debugging, coding, problem solving,
previous concepts, and a new mini project. Level 0's mini project is a simple
script/setup demonstration. Increase difficulty through unfamiliar scenarios,
integration, and reasoning; do not introduce untaught topics.

Checkpoint material is created only when its prerequisites pass. Each has its own
submission, mentor guide, rubric, verbal questions, and revision decision. A
failed checkpoint blocks the next level. Reassess weak areas with new examples
rather than memorized answers. Consult `knowledge.md` when choosing recall topics.

## Review output

Use [the review template](../templates/review.md). Lead with the task and reviewed
commit, then understanding, coding, problem solving, debugging, and code quality.
Include strengths, problems, concepts needing revision, required corrections,
mentor questions, evidence and scoring, and a proposed PASS or REVISION REQUIRED.
Record Naresh's final decision separately from the AI recommendation.
