# Working in learnpy

Naresh is the mentor; Raajashree is the learner. Read `plan.md`, `README.md`,
`curriculum/catalog.json`, and `progress.json` before creating or reviewing tasks.

- The current stage is system design. Do not generate PY-001 until Naresh approves
  the system and explicitly authorizes the first assignment. Record those decisions
  with `tools/track.py` only after he actually makes them.
- Assign one concept at a time, after its prerequisites have passed. Prepared
  materials and submitted code are not evidence of mastery.
- Use the templates. Include study material, gradual examples, exercises A–E,
  a challenge, debugging, a five-section test, explanations, and Git deliverables.
- Do not write the learner's submissions, exercise solutions, or assessment answers.
  Keep answer keys in ignored `mentor-private/` or a separate private location.
  A folder named "mentor" in a shared repository is not access control.
- Naresh alone decides advancement. Reviews must consider understanding,
  independence, debugging, appropriate edge cases, explanations, and Git quality.
  Review beginner code against the concepts already taught.
- Use `curriculum/catalog.json` as the curriculum source and `progress.json` as the
  progress source. Run `python3 tools/track.py render` after changes; do not edit
  generated `curriculum/roadmap.md` or `progress.md` directly.
- Do not mark approvals, completed work, scores, strengths, or weaknesses without
  evidence. Do not auto-commit or push learner work.
- Preserve existing user changes. Run `python3 tools/track.py validate` and
  `python3 -m unittest discover -s tests -v` after changing tracking behavior.

The tracker is a local workflow aid, not authentication. Mentor flags record a
decision; they do not establish the caller's identity.
