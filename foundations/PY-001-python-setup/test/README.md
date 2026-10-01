# PY-001 — Concept test

Prerequisites: none. Time budget: about 45 minutes.
Operating systems: Windows and Ubuntu. Windows users replace `python3` with `py` in every command.
Assistance rules: **independent** — notes from your own study material are allowed; no generated answers; no copying. Write answers in `test/answers.md`.

## Section A — Theory (20 marks)

1. (5) In your own words: what does "installing Python" put on your computer?
2. (5) What is the job of the interpreter? Use an analogy that is not the cook.
3. (5) Compare Python and pip. How are they different and how do they work together?
4. (5) What is PATH and why can a correct install still show "command not found"?

## Section B — Predict the output (20 marks)

Write prediction and reasoning **before** running anything. Then run and record the observed output separately; do not change your prediction.

1. (5) `python3 -c "print('abc')"`
2. (5) `python3 -c "print(2 + 3)"` (no quotes around `2 + 3`)
3. (5) `python3 -c "print('2 + 3')"` (quotes around `2 + 3`)
4. (5) You run `python3 --version` and the reply is `Python 3.11.9`. Then you run `python3 -m pip --version`. Which Python version will the end of pip's reply mention, and why?

## Section C — Find the bug (20 marks)

For each: identify the behaviour, cause, correction, and one verification case.

1. (7) ```$ python3 -c "print("Hello")"``` prints an error on some computers or an odd result.
2. (7) A learner installed Python on Windows, then used the terminal window that was already open and typed `py --version`: *not recognized*.
3. (6) Ubuntu user: `$ python3 -m pip --versoin` → `No such option: --versoin`

## Section D — Write code (25 marks)

File: `test/answers.md` (commands and replies).

1. (10) Give a command that prints exactly `Level 0 started` and show its reply.
2. (15) Give a command that prints your age next year as a number computed by Python from your current age (use `+`; do not type the answer yourself) and show its reply. State your inputs and why the computed approach is better than typing the final number.

## Section E — Explain your code (15 marks)

Explain, for Section D: your approach, each important part of the command, input and output, edge cases you considered (for example quotes), one problem you hit and its fix, and how you verified it.

## Submission

Put all answers in `test/answers.md`. Commit with `learn(PY-001): complete Python setup test`, push, and give Naresh the commit ID.
Marks total 100: A 20 + B 20 + C 20 + D 25 + E 15.
