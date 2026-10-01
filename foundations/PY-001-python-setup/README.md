# PY-001 — Python setup

**Learner:** Raajashree  **Mentor:** Naresh  **Level:** 0 — Programming Foundations (beginner)
**Prerequisites:** none (this is your first task)  **Estimated time:** 1–2 hours study and practice, plus the test

## Learning objectives

By the end you can:

1. Explain what "installing Python" gives your computer and why we need it.
2. Install Python 3 on your computer and prove it works.
3. Tell which Python version you have and where it lives on your disk.
4. Explain the difference between `python`, `python3` (and `py` on Windows) and `pip`.
5. Run a tiny Python instruction from the terminal and explain what happened.
6. Read an unfamiliar setup error message and decide what it probably means.
7. Save your work in Git with a clear commit message and push it to `learnpy`.

Work independently. Write every answer in your own words. If you get a hint from anyone
or anything, write it down in `notes/submission.md` — asking for help is not a failure.

---

## Study material

### What is Python setup?

Python is a **programming language**: a set of rules for writing instructions a computer can follow.
Your computer cannot understand those rules by itself. It needs a program called the
**Python interpreter** that reads Python instructions and carries them out.
"Setting up Python" means putting that interpreter (plus a few helper tools) on your computer
and checking that you can start it.

### Why do we need it?

A recipe written in English is useless without a cook who understands English. Python code is
the recipe and the interpreter is the cook. No interpreter, no cooking. (How the interpreter
works inside is a later topic — PY-003. For now, just know it must exist on your machine.)

### Problem it solves

Without a correct setup, nothing else in this course works. Most beginner "my code is broken"
problems in the first week are really setup problems: Python is missing, an old version
is being used, or the computer cannot find it.

### Real-world use

Every developer, data analyst and DevOps engineer who uses Python begins every new computer
or server with the same two questions: *Is Python installed? Which version?*
Teams write the required version in their project notes because code written for one version can
break on another.

---

## Concept explanation

Three things get installed together:

| Piece | What it is | Simple picture |
|---|---|---|
| **Interpreter** | The program that runs Python instructions | The cook |
| **Standard library** | Ready-made Python tools that ship with the interpreter | The cook's built-in kitchen tools |
| **pip** | A helper that downloads extra Python tools written by others | A delivery service for more tools |

**Versions.** Python versions look like `3.12.4`: *major.minor.patch*. This course uses
**Python 3** (any 3.10 or newer is fine; newest stable release is best). Python 2 is retired — if you
ever see "Python 2.7", that is the wrong one.

**Which operating system?** This task has instructions for **Windows** and **Ubuntu (Linux)**. Follow the lines marked for your computer and ignore the other. Wherever an example says `python3`, Windows users type `py` instead.

**Command names.** To start the interpreter you type a command in the terminal:

- Ubuntu: `python3`
- Windows: `py` (sometimes `python` also works)

On some machines `python` means an old or missing Python, which is why we check carefully.
`pip` is run the same way as a command, or safely as `python3 -m pip` (Windows: `py -m pip`).

**The terminal (just enough for today).** A terminal is a window where you *type a command and
press Enter*, and the computer types the result back. You will learn the terminal properly in
PY-005. Today you only need to open it, type exactly what is shown, press Enter, and read the reply.
Lines beginning with `$` below show what to type; **do not type the `$`**.

Open a terminal:
- Windows: press the Windows key, type `PowerShell`, press Enter.
- Ubuntu: press Ctrl+Alt+T.

**How to install** (follow the one for your computer):

- **Windows:** download the installer from <https://www.python.org/downloads/windows/>. On the first screen **tick "Add python.exe to PATH"**, then click Install Now. Close the terminal and open a new one afterwards.
- **Ubuntu:** Python 3 is normally already installed. Check first (Example 1). If it is missing, or `pip` is missing, run:
  ```text
  $ sudo apt update
  $ sudo apt install python3 python3-pip
  ```
  `sudo` means "run as administrator"; it asks for your password and shows nothing while you type it — that is normal. `apt` is Ubuntu's built-in installer for software.

**What is PATH?** Your computer keeps a list of folders where it looks for commands. That list is called
**PATH**. If Python's folder is not on it, typing `py` or `python3` gives "command not found". Ticking the PATH box on Windows fixes this.

---

## Syntax

Every command has the same shape:

```text
command  option  value
```

- **command** — the program to start (`python3`).
- **option** — a switch that changes behaviour, starting with `-` or `--` (`--version`).
- **value** — extra input some options need (the text after `-c`).

---

## Examples

Use `python3` on Ubuntu and `py` on Windows in every example. Replies below are from Ubuntu unless marked Windows; yours will differ in numbers and folders.

### Example 1 — very simple: ask the version

```text
$ python3 --version
Python 3.12.4
```

Windows version of the same example:

```text
PS C:\Users\raaja> py --version
Python 3.12.4
```

`PS C:\Users\raaja>` is the Windows prompt (like `$` on Ubuntu) — you do not type it. `--version` tells the interpreter "just report your version, then stop." Your number will differ.

### Example 2 — slight variation: ask pip

```text
$ python3 -m pip --version
pip 24.0 from /usr/lib/python3/dist-packages/pip (python 3.12)
```

Windows reply looks like `pip 24.0 from C:\Users\raaja\AppData\Local\Programs\Python\Python312\Lib\site-packages\pip (python 3.12)`.

`-m pip` means "run the helper called pip using this interpreter". The reply tells you pip's version, where it lives, and which Python it belongs to. Changing `--version` for `-m pip --version` changed *which program answered*.

### Example 3 — run one Python instruction

```text
$ python3 -c "print('Setup works')"
Setup works
```

On Windows PowerShell type `py -c "print('Setup works')"`. Use double quotes on the outside and single quotes on the inside; the other way round behaves differently on different terminals.

`-c` means "run the Python text that follows." `print(...)` is a Python instruction that shows text on the screen. The quotes tell Python the words inside are plain text. (Writing real programs is PY-002 onward; this one line is only a health check.)

### Example 4 — real-world scenario: a teammate's onboarding check

A new teammate says "the project doesn't run". The first thing you ask them to do:

```text
$ python3 --version
Command 'python3' not found
```

(On Windows the matching reply is `py : The term 'py' is not recognized as the name of a cmdlet...`.)

From that single reply you can tell Python is not installed (or not on PATH) — you don't need to look at any project code. Compare with a reply of `Python 2.7.18`, which would mean the wrong version is answering.

---

## Example execution explanation

For `python3 -c "print('Setup works')"`, in order:

1. The terminal finds the command `python3` by searching the folders on PATH.
2. It starts the interpreter and gives it the option `-c` and the text `print('Setup works')`.
3. The interpreter reads that text as one Python instruction.
4. `print` sends the text between the quotes to the screen — without the quotes.
5. The interpreter has nothing more to do, so it stops, and the terminal is ready for your next command.

---

## Common mistakes

| Mistake | Typical symptom | How to recognise it |
|---|---|---|
| Typing the `$` | `$: command not found` | The error mentions `$` itself |
| Python not on PATH (Windows) | `'py' is not recognized…` or `python` opens the Microsoft Store | Reinstall and tick the PATH box, then open a *new* terminal |
| `pip` missing (Ubuntu) | `No module named pip` | Run `sudo apt install python3-pip` |
| Wrong password feeling (Ubuntu `sudo`) | Nothing appears as you type the password | Type it anyway and press Enter |
| Opening an old terminal after installing | Command still not found | New installs show up only in terminals opened afterwards |
| Wrong quotes or missing quote in `-c` | `SyntaxError` or the terminal waits for more input | The reply mentions quotes/unterminated text; press Ctrl+C to escape |
| Using `python` when only `python3` exists | `python: command not found` | `python3` works but `python` doesn't |
| Reading a Python 2 version as correct | Version starts with `2.` | Look at the first number |

## Best practices

- Always read the **whole** reply of a command, including the first line.
- Copy your version into your notes — "it works" is weaker evidence than the exact text.
- After changing anything, close and reopen the terminal and test again.
- Change one thing at a time when something fails.
- When asking for help, include the exact command you typed and the exact reply.

---

## Guided practice

1. Open a terminal.
2. **Predict:** write in `notes/study.md` what you expect `python3 --version` (or `py --version`) to print, and why.
3. Run it. Write the real output below your prediction without altering the prediction.
4. If they differ, write one sentence on why.

---

## Hands-on exercises

Details, filenames and rules are in [exercises/README.md](exercises/README.md).
Exercises A–E, the challenge in [hands-on/README.md](hands-on/README.md) and the test in [test/README.md](test/README.md) are all required.

## Debugging exercise

Included in [exercises/README.md](exercises/README.md) (Exercise F) — you diagnose broken terminal replies.
Explain what is wrong, why it happens, how you would repair it, how you would verify the repair, and how it could have been prevented.

## Concept questions (answer in `notes/study.md`, in your own words)

1. What is the Python interpreter, and what would happen if your computer had none?
2. Why does a computer need the interpreter if Python code is already text it can store?
3. What does PATH do? What symptom tells you something is wrong with it?
4. What are the three parts of a version like `3.12.4`? Which part matters most for this course?
5. What is the difference between Python and pip?
6. Why is the terminal reply "Python 2.7.18" a problem?

## Expected deliverables

Everything lives in this folder, `foundations/PY-001-python-setup/`:

- `notes/study.md` — your predictions, observed outputs, and concept-question answers
- `exercises/answers.md` — your answers to Exercises A–F
- `hands-on/challenge.md` — your challenge write-up (plan first, then evidence)
- `test/answers.md` — your test answers
- `notes/explanation.md` — explain what you did and why (what, why, edge cases, problems, fixes)
- `notes/submission.md` — use [../../templates/submission.md](../../templates/submission.md); list deliverables, tests/runs, and any help you received

Screenshots are fine as extra evidence, but typed text of the commands and replies is required.

## Git location and commits

Folder: `foundations/PY-001-python-setup/`

- Exercises and notes: `learn(PY-001): complete Python setup exercises`
- Test: a separate commit such as `learn(PY-001): complete Python setup test`
- Corrections: `fix(PY-001): correct <specific issue>`

Push to `learnpy` and send Naresh the final commit ID. Do not copy answers from anywhere.
Because Git has its own task later (PY-009), your Git steps today are only: `git add <your folder>`, `git commit -m "<message>"`, `git push`. Naresh will show you if you need help the first time.

## Evaluation criteria (100 points)

| Area | Points |
|---|---|
| Exercises A–F | 25 |
| Challenge and planning | 15 |
| Concept test (A–E) | 30 |
| Explanations and notes in your own words | 15 |
| Independence and verbal check with Naresh | 10 |
| Git quality (clear commits, pushed, tidy folder) | 5 |

## Pass criteria

At least **80/100**; theory, hands-on, test and review all complete; no unresolved core misconception; all work committed and pushed; and Naresh's final approval. A submission is not a pass. Revisions must be reassessed before PY-002.
