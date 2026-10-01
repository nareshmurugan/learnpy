# Mentorship system

Naresh assigns and evaluates; Raajashree learns and writes her own work. AI prepares
materials and advises Naresh. **Naresh has final authority over advancement.**

## Current decision gate

The repository contains the complete system and planning catalog. It does not yet
contain PY-001 study material, exercises, or a concept test. Naresh must approve
this system and explicitly ask to start the first task before it is generated.
The tracker records those two real decisions separately. They may be given in one
message, but neither is assumed from the initial request to implement the system.

## Teaching cycle

For every concept: study → simple examples → execution explanation → guided
practice → independent exercises → hands-on task → concept test → Git submission
→ mentor review → pass or focused revision. Reading material alone is not mastery.

Prepare one task from [the task template](../templates/task.md) at a time. Explain
what the concept is, why it exists, what problem it solves, its syntax, execution,
real-world use, common mistakes, and best practices. Material should be sufficient
without another tutorial. Keep prerequisites visible and examples within the
learner's current knowledge. Walk through examples line by line and progress from
simple syntax to a practical scenario. Example programs may demonstrate a concept;
they must not solve the assigned exercises or assessment.

Each task includes exercises A–E: syntax, understanding, problem solving,
combination, and real-world use. At Level 0, programming can mean typing and running
a tiny script; do not require variables or loops before those tasks pass. Include
a separate challenge, a broken program, and a concept test. Raajashree predicts
output before running examples and records what differed from her prediction.

## Pacing and timeline

The full catalog allocates **1,253–2,188 hours** across 283 concepts, 14 projects,
19 checkpoints, and a 100–160-hour capstone. These are conservative planning
budgets, not deadlines or evidence that someone is production-ready. Revisions,
breaks, installation difficulties, and external-service setup add time.

| Weekly independent study budget | Approximate active study time for the full plan |
|---|---|
| 6 hours | 209–365 weeks (about 4–7 years) |
| 10 hours | 126–219 weeks (about 2.4–4.2 years) |
| 15 hours | 84–146 weeks (about 1.6–2.8 years) |
| 20 hours | 63–110 weeks (about 1.2–2.1 years) |

Start with two or three study sessions and one mentor review per week, adjusting
to Raajashree's availability. For a normal concept, reserve roughly 40% of time
for reading and guided practice, 40% for independent work, and 20% for assessment
and discussion. Checkpoint and project pacing is separate. A learner who already
knows a concept may demonstrate it sooner; do not skip evidence to meet a date.
Review the budgets after the foundations checkpoint using actual learning time.

## Dependency and assignment rules

The [roadmap](../curriculum/roadmap.md) is a conservative sequential dependency
chain. A concept's predecessor must pass. Milestone projects precede the level's
checkpoint; that checkpoint precedes the next level. The capstone follows Level 18.
Only one assignment is active. LOCKED means unassigned, including an eligible task
whose material has not yet been prepared. `next` reports eligibility separately.

Naresh may change the curriculum to fit demonstrated skills, but record the
reason and keep IDs stable. Update catalog and progress together, validate them,
and review the dependency change rather than overriding a failed prerequisite.

## Understanding and independence

Require explanations of purpose, approach, inputs, outputs, edge cases, failures,
and fixes. For a larger problem, require problem → inputs → outputs → constraints
→ edge cases → algorithm → pseudocode → implementation → tests → debugging →
refactoring. Early tasks need only a short, age-appropriate planning note.

Raajashree first tries independently, rereads material, checks documentation,
then asks for a conceptual hint. Escalate to a stronger hint, pseudocode, or a small
unrelated example only as needed. Record assistance. Naresh explicitly decides
whether AI assistance is allowed in an assessment; default is independent answers.
If assessment answers were supplied, use a fresh problem to verify independence.

## Revision and long-term retention

After REVISION, prepare [a revision task](../templates/revision.md): a short
explanation, different examples, two or three focused exercises, one debugging
problem, and one verification question. Preserve the original submission and
review in Git. Reassess a new commit. The tracker resets verified checks for the
new attempt and retains the earlier review in history.

Maintain [knowledge.md](../knowledge.md) only from reviewed evidence. Reuse weak
concepts in later exercises; do not invent a weakness because a topic is advanced.
After each pass, plan a small recall problem after roughly 1, 3, and 6 later tasks,
plus the next checkpoint. These are task intervals, not automatic calendar events.
Strong areas still appear in combined problems. If recall reveals a serious gap,
pause the active task and address it within its revision work before proceeding.

## Common mentor requests

| Request | Response/work |
|---|---|
| Create next task | Read state, check gates, prepare the eligible complete learner assignment |
| Create study material for PY-XXX | Prepare material at demonstrated prerequisite level |
| Create test for PY-XXX | Learner test plus separately private mentor guide, unless learner-only |
| Evaluate PY-XXX | Inspect the specified commit, run relevant work, review explanations, propose a decision |
| Create revision task | Use recorded gaps and a new focused problem |
| What's next? | Report current gate, active work, prerequisites, and retention needs |

Never claim a submission was inspected when its files or commit were unavailable.
An AI evaluation is advisory until Naresh makes and records the decision.
