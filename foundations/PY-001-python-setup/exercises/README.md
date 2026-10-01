# PY-001 — Exercises A–F

Write your answers in `exercises/answers.md`. Give the **exact command you typed** and the **exact reply**
for every run. Use `python3` (Ubuntu) or `py` (Windows). Always say which operating system you used.

## Exercise A — Basic

Install Python 3 (if not already installed) and report the version.

- Requirements: the command you used, the exact reply, and the operating system you use (Windows or Ubuntu).
- Deliverable: `exercises/answers.md`, heading "A".

## Exercise B — Understanding

Run the pip version command (Example 2, `-m pip --version`).

- Requirements: the exact reply, then in your own words explain what each of the three parts of the reply tells you. Then explain what would be different if you ran `pip --version` without `python3 -m`, and why that might point at a different Python.
- Deliverable: heading "B".

## Exercise C — Problem solving

Your friend says: "I installed Python yesterday but my terminal says the command is not found." You can ask your friend to run **up to four** commands or actions, one at a time.

- Input: the friend's report. Output: an ordered list of up to four checks, each with what you would conclude if the reply is good and if it is bad.
- Constraint: no guessing — each step must follow from the previous reply.
- Deliverable: heading "C".

## Exercise D — Combination

There are no earlier tasks to combine with, so combine today's ideas: version, command name, and `-c`.
Run Python so that it prints your own first name using `-c`, then run it again so it prints your first name and the text `is learning Python` on **one** line.

- Requirements: both commands and replies, plus what you did to fix any quote or spelling mistake you made on the way (describe your real mistakes; if none, write "none").
- Deliverable: heading "D".

## Exercise E — Real world

You are writing a one-page "Python setup note" for a new teammate who has the same OS as you.

- Requirements: required version rule, install steps in your own words, three checks that prove it works, and the three most likely failures with their fixes. Maximum one page.
- Acceptance: someone who has never installed Python could follow it without asking you anything.
- Write it for your own OS, then add a short section "If you have the other OS" (Windows ↔ Ubuntu) with the differences you can find from the study material.
- Deliverable: heading "E".

## Exercise F — Debugging

Each is a real terminal session. For each, state what is wrong, the cause, a repair, how you would verify the repair, and how to prevent it.

```text
1)  $ python3 --version
    Python 2.7.18

2)  $ py --version
    'py' is not recognized as an internal or external command

3)  $ python3 -c "print('Hello)"
      File "<string>", line 1
        print('Hello)
              ^
    SyntaxError: unterminated string literal (detected at line 1)

4)  $ $ python3 --version
    $: command not found
```

Deliverable: heading "F" with four numbered answers.
Items 1, 3 and 4 can happen on either system; item 2 is a Windows message. For every item give the repair for **both Windows and Ubuntu** where the repair differs, even though you only own one of them.
