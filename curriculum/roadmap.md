# Python roadmap

Generated from `catalog.json` with `python3 tools/track.py render`.

This is the complete planned curriculum, not a set of issued assignments. Each concept
gets its own learner task when eligible. The sequence is deliberately conservative:
pass the named prerequisite before preparing and assigning the next task. Projects
and checkpoints also gate advancement. Consult progress.md for current task states.

Hours are planning ranges for study, exercises, assessment, and review; revision may
add time. See [mentorship](../docs/mentorship.md) for pacing and [assessment](../docs/assessment.md)
for checkpoint requirements. Repeat advanced topics deepen earlier foundations.

## Level 0 — Programming Foundations

Budget: 12–23 hours. Folder: `foundations/`.

| ID | Topic | Type | Prerequisite | Hours | Git location |
|---|---|---|---|---|---|
| PY-001 | Python setup | concept | Mentor approvals | 1–2 | `foundations/PY-001-python-setup/` |
| PY-002 | Programming as step-by-step instructions | concept | PY-001 | 1–2 | `foundations/PY-002-programming-as-step-by-step-instructions/` |
| PY-003 | Python and interpreters versus compilers | concept | PY-002 | 1–2 | `foundations/PY-003-python-and-interpreters-versus-compilers/` |
| PY-004 | Source code and .py files | concept | PY-003 | 1–2 | `foundations/PY-004-source-code-and-py-files/` |
| PY-005 | Terminal basics | concept | PY-004 | 1–2 | `foundations/PY-005-terminal-basics/` |
| PY-006 | Python REPL | concept | PY-005 | 1–2 | `foundations/PY-006-python-repl/` |
| PY-007 | Running Python scripts | concept | PY-006 | 1–2 | `foundations/PY-007-running-python-scripts/` |
| PY-008 | Editor basics | concept | PY-007 | 1–2 | `foundations/PY-008-editor-basics/` |
| PY-009 | Basic Git workflow | concept | PY-008 | 1–2 | `foundations/PY-009-basic-git-workflow/` |
| CP-00 | Level 0 checkpoint — Programming Foundations | checkpoint | PY-009 | 3–5 | `assessments/CP-00/` |

## Level 1 — Python Fundamentals

Budget: 57–87 hours. Folder: `fundamentals/`.

| ID | Topic | Type | Prerequisite | Hours | Git location |
|---|---|---|---|---|---|
| PY-010 | Syntax and indentation | concept | CP-00 | 2–3 | `fundamentals/PY-010-syntax-and-indentation/` |
| PY-011 | Comments | concept | PY-010 | 2–3 | `fundamentals/PY-011-comments/` |
| PY-012 | Variables and assignment | concept | PY-011 | 2–3 | `fundamentals/PY-012-variables-and-assignment/` |
| PY-013 | Naming conventions | concept | PY-012 | 2–3 | `fundamentals/PY-013-naming-conventions/` |
| PY-014 | Keywords | concept | PY-013 | 2–3 | `fundamentals/PY-014-keywords/` |
| PY-015 | Literals | concept | PY-014 | 2–3 | `fundamentals/PY-015-literals/` |
| PY-016 | Integers | concept | PY-015 | 2–3 | `fundamentals/PY-016-integers/` |
| PY-017 | Floating-point numbers | concept | PY-016 | 2–3 | `fundamentals/PY-017-floating-point-numbers/` |
| PY-018 | Strings as values | concept | PY-017 | 2–3 | `fundamentals/PY-018-strings-as-values/` |
| PY-019 | Booleans | concept | PY-018 | 2–3 | `fundamentals/PY-019-booleans/` |
| PY-020 | None | concept | PY-019 | 2–3 | `fundamentals/PY-020-none/` |
| PY-021 | Inspecting types with type() | concept | PY-020 | 2–3 | `fundamentals/PY-021-inspecting-types-with-type/` |
| PY-022 | Type conversion | concept | PY-021 | 2–3 | `fundamentals/PY-022-type-conversion/` |
| PY-023 | Output with print() | concept | PY-022 | 2–3 | `fundamentals/PY-023-output-with-print/` |
| PY-024 | Input with input() | concept | PY-023 | 2–3 | `fundamentals/PY-024-input-with-input/` |
| PY-025 | Arithmetic operators | concept | PY-024 | 2–3 | `fundamentals/PY-025-arithmetic-operators/` |
| PY-026 | Comparison operators | concept | PY-025 | 2–3 | `fundamentals/PY-026-comparison-operators/` |
| PY-027 | Logical operators | concept | PY-026 | 2–3 | `fundamentals/PY-027-logical-operators/` |
| PY-028 | Assignment operators | concept | PY-027 | 2–3 | `fundamentals/PY-028-assignment-operators/` |
| PY-029 | Identity operators | concept | PY-028 | 2–3 | `fundamentals/PY-029-identity-operators/` |
| PY-030 | Membership operators | concept | PY-029 | 2–3 | `fundamentals/PY-030-membership-operators/` |
| PY-031 | Operator precedence | concept | PY-030 | 2–3 | `fundamentals/PY-031-operator-precedence/` |
| PY-032 | String operations | concept | PY-031 | 2–3 | `fundamentals/PY-032-string-operations/` |
| PY-033 | F-strings | concept | PY-032 | 2–3 | `fundamentals/PY-033-f-strings/` |
| PRJ-001 | Calculator | project | PY-033 | 6–10 | `projects/PRJ-001-calculator/` |
| CP-01 | Level 1 checkpoint — Python Fundamentals | checkpoint | PRJ-001 | 3–5 | `assessments/CP-01/` |

## Level 2 — Control Flow

Budget: 35–66 hours. Folder: `control-flow/`.

| ID | Topic | Type | Prerequisite | Hours | Git location |
|---|---|---|---|---|---|
| PY-034 | If statements | concept | CP-01 | 2–4 | `control-flow/PY-034-if-statements/` |
| PY-035 | Elif branches | concept | PY-034 | 2–4 | `control-flow/PY-035-elif-branches/` |
| PY-036 | Else branches | concept | PY-035 | 2–4 | `control-flow/PY-036-else-branches/` |
| PY-037 | Nested conditions | concept | PY-036 | 2–4 | `control-flow/PY-037-nested-conditions/` |
| PY-038 | For loops | concept | PY-037 | 2–4 | `control-flow/PY-038-for-loops/` |
| PY-039 | Range | concept | PY-038 | 2–4 | `control-flow/PY-039-range/` |
| PY-040 | While loops | concept | PY-039 | 2–4 | `control-flow/PY-040-while-loops/` |
| PY-041 | Break | concept | PY-040 | 2–4 | `control-flow/PY-041-break/` |
| PY-042 | Continue | concept | PY-041 | 2–4 | `control-flow/PY-042-continue/` |
| PY-043 | Pass | concept | PY-042 | 2–4 | `control-flow/PY-043-pass/` |
| PY-044 | Loop else | concept | PY-043 | 2–4 | `control-flow/PY-044-loop-else/` |
| PY-045 | Nested loops | concept | PY-044 | 2–4 | `control-flow/PY-045-nested-loops/` |
| PRJ-002 | Number guessing game | project | PY-045 | 8–12 | `projects/PRJ-002-number-guessing-game/` |
| CP-02 | Level 2 checkpoint — Control Flow | checkpoint | PRJ-002 | 3–6 | `assessments/CP-02/` |

## Level 3 — Data Structures

Budget: 48–92 hours. Folder: `data-structures/`.

| ID | Topic | Type | Prerequisite | Hours | Git location |
|---|---|---|---|---|---|
| PY-046 | String indexing | concept | CP-02 | 2–4 | `data-structures/PY-046-string-indexing/` |
| PY-047 | String slicing | concept | PY-046 | 2–4 | `data-structures/PY-047-string-slicing/` |
| PY-048 | Lists | concept | PY-047 | 2–4 | `data-structures/PY-048-lists/` |
| PY-049 | List indexing and slicing | concept | PY-048 | 2–4 | `data-structures/PY-049-list-indexing-and-slicing/` |
| PY-050 | List methods | concept | PY-049 | 2–4 | `data-structures/PY-050-list-methods/` |
| PY-051 | Tuples | concept | PY-050 | 2–4 | `data-structures/PY-051-tuples/` |
| PY-052 | Sets | concept | PY-051 | 2–4 | `data-structures/PY-052-sets/` |
| PY-053 | Set operations | concept | PY-052 | 2–4 | `data-structures/PY-053-set-operations/` |
| PY-054 | Dictionaries | concept | PY-053 | 2–4 | `data-structures/PY-054-dictionaries/` |
| PY-055 | Dictionary access and iteration | concept | PY-054 | 2–4 | `data-structures/PY-055-dictionary-access-and-iteration/` |
| PY-056 | Mutability and immutability | concept | PY-055 | 2–4 | `data-structures/PY-056-mutability-and-immutability/` |
| PY-057 | Packing | concept | PY-056 | 2–4 | `data-structures/PY-057-packing/` |
| PY-058 | Unpacking | concept | PY-057 | 2–4 | `data-structures/PY-058-unpacking/` |
| PY-059 | Nested structures | concept | PY-058 | 2–4 | `data-structures/PY-059-nested-structures/` |
| PY-060 | List comprehensions | concept | PY-059 | 2–4 | `data-structures/PY-060-list-comprehensions/` |
| PY-061 | Dictionary comprehensions | concept | PY-060 | 2–4 | `data-structures/PY-061-dictionary-comprehensions/` |
| PY-062 | Set comprehensions | concept | PY-061 | 2–4 | `data-structures/PY-062-set-comprehensions/` |
| PY-063 | Choosing data structures | concept | PY-062 | 2–4 | `data-structures/PY-063-choosing-data-structures/` |
| PRJ-003 | Contact manager | project | PY-063 | 8–14 | `projects/PRJ-003-contact-manager/` |
| CP-03 | Level 3 checkpoint — Data Structures | checkpoint | PRJ-003 | 4–6 | `assessments/CP-03/` |

## Level 4 — Functions

Budget: 65–108 hours. Folder: `functions/`.

| ID | Topic | Type | Prerequisite | Hours | Git location |
|---|---|---|---|---|---|
| PY-064 | Defining and calling functions | concept | CP-03 | 3–5 | `functions/PY-064-defining-and-calling-functions/` |
| PY-065 | Parameters and arguments | concept | PY-064 | 3–5 | `functions/PY-065-parameters-and-arguments/` |
| PY-066 | Return values | concept | PY-065 | 3–5 | `functions/PY-066-return-values/` |
| PY-067 | Positional arguments | concept | PY-066 | 3–5 | `functions/PY-067-positional-arguments/` |
| PY-068 | Keyword arguments | concept | PY-067 | 3–5 | `functions/PY-068-keyword-arguments/` |
| PY-069 | Default arguments | concept | PY-068 | 3–5 | `functions/PY-069-default-arguments/` |
| PY-070 | Variable positional arguments (*args) | concept | PY-069 | 3–5 | `functions/PY-070-variable-positional-arguments-args/` |
| PY-071 | Variable keyword arguments (**kwargs) | concept | PY-070 | 3–5 | `functions/PY-071-variable-keyword-arguments-kwargs/` |
| PY-072 | Scope and LEGB | concept | PY-071 | 3–5 | `functions/PY-072-scope-and-legb/` |
| PY-073 | Global names | concept | PY-072 | 3–5 | `functions/PY-073-global-names/` |
| PY-074 | Nonlocal names | concept | PY-073 | 3–5 | `functions/PY-074-nonlocal-names/` |
| PY-075 | Recursion | concept | PY-074 | 3–5 | `functions/PY-075-recursion/` |
| PY-076 | Lambda expressions | concept | PY-075 | 3–5 | `functions/PY-076-lambda-expressions/` |
| PY-077 | Functions as objects | concept | PY-076 | 3–5 | `functions/PY-077-functions-as-objects/` |
| PY-078 | Higher-order functions | concept | PY-077 | 3–5 | `functions/PY-078-higher-order-functions/` |
| PY-079 | Closures | concept | PY-078 | 3–5 | `functions/PY-079-closures/` |
| PY-080 | Decorator foundations | concept | PY-079 | 3–5 | `functions/PY-080-decorator-foundations/` |
| PRJ-004 | Student marks system | project | PY-080 | 10–16 | `projects/PRJ-004-student-marks-system/` |
| CP-04 | Level 4 checkpoint — Functions | checkpoint | PRJ-004 | 4–7 | `assessments/CP-04/` |

## Level 5 — Modules and Project Structure

Budget: 32–63 hours. Folder: `modules/`.

| ID | Topic | Type | Prerequisite | Hours | Git location |
|---|---|---|---|---|---|
| PY-081 | Modules | concept | CP-04 | 2–4 | `modules/PY-081-modules/` |
| PY-082 | Imports | concept | PY-081 | 2–4 | `modules/PY-082-imports/` |
| PY-083 | Packages | concept | PY-082 | 2–4 | `modules/PY-083-packages/` |
| PY-084 | __init__.py | concept | PY-083 | 2–4 | `modules/PY-084-init-py/` |
| PY-085 | __name__ and main entry points | concept | PY-084 | 2–4 | `modules/PY-085-name-and-main-entry-points/` |
| PY-086 | Standard library discovery | concept | PY-085 | 2–4 | `modules/PY-086-standard-library-discovery/` |
| PY-087 | Virtual environments | concept | PY-086 | 2–4 | `modules/PY-087-virtual-environments/` |
| PY-088 | Pip | concept | PY-087 | 2–4 | `modules/PY-088-pip/` |
| PY-089 | Dependencies | concept | PY-088 | 2–4 | `modules/PY-089-dependencies/` |
| PY-090 | Requirements files | concept | PY-089 | 2–4 | `modules/PY-090-requirements-files/` |
| PY-091 | Pyproject metadata | concept | PY-090 | 2–4 | `modules/PY-091-pyproject-metadata/` |
| PY-092 | Project structure | concept | PY-091 | 2–4 | `modules/PY-092-project-structure/` |
| PY-093 | Git ignore rules | concept | PY-092 | 2–4 | `modules/PY-093-git-ignore-rules/` |
| PY-094 | Git commit hygiene | concept | PY-093 | 2–4 | `modules/PY-094-git-commit-hygiene/` |
| CP-05 | Level 5 checkpoint — Modules and Project Structure | checkpoint | PY-094 | 4–7 | `assessments/CP-05/` |

## Level 6 — Files and Data

Budget: 47–76 hours. Folder: `files/`.

| ID | Topic | Type | Prerequisite | Hours | Git location |
|---|---|---|---|---|---|
| PY-095 | Reading files | concept | CP-05 | 3–5 | `files/PY-095-reading-files/` |
| PY-096 | Writing files | concept | PY-095 | 3–5 | `files/PY-096-writing-files/` |
| PY-097 | With statements and resource cleanup | concept | PY-096 | 3–5 | `files/PY-097-with-statements-and-resource-cleanup/` |
| PY-098 | Paths with pathlib | concept | PY-097 | 3–5 | `files/PY-098-paths-with-pathlib/` |
| PY-099 | Directory operations | concept | PY-098 | 3–5 | `files/PY-099-directory-operations/` |
| PY-100 | JSON | concept | PY-099 | 3–5 | `files/PY-100-json/` |
| PY-101 | CSV | concept | PY-100 | 3–5 | `files/PY-101-csv/` |
| PY-102 | YAML | concept | PY-101 | 3–5 | `files/PY-102-yaml/` |
| PY-103 | Configuration files | concept | PY-102 | 3–5 | `files/PY-103-configuration-files/` |
| PY-104 | Serialization choices | concept | PY-103 | 3–5 | `files/PY-104-serialization-choices/` |
| PRJ-005 | Expense tracker | project | PY-104 | 12–18 | `projects/PRJ-005-expense-tracker/` |
| CP-06 | Level 6 checkpoint — Files and Data | checkpoint | PRJ-005 | 5–8 | `assessments/CP-06/` |

## Level 7 — Exception Handling

Budget: 35–64 hours. Folder: `exceptions/`.

| ID | Topic | Type | Prerequisite | Hours | Git location |
|---|---|---|---|---|---|
| PY-105 | Errors versus exceptions | concept | CP-06 | 2–4 | `exceptions/PY-105-errors-versus-exceptions/` |
| PY-106 | Reading tracebacks | concept | PY-105 | 2–4 | `exceptions/PY-106-reading-tracebacks/` |
| PY-107 | Try and except | concept | PY-106 | 2–4 | `exceptions/PY-107-try-and-except/` |
| PY-108 | Exception else | concept | PY-107 | 2–4 | `exceptions/PY-108-exception-else/` |
| PY-109 | Finally | concept | PY-108 | 2–4 | `exceptions/PY-109-finally/` |
| PY-110 | Raise | concept | PY-109 | 2–4 | `exceptions/PY-110-raise/` |
| PY-111 | Custom exceptions | concept | PY-110 | 2–4 | `exceptions/PY-111-custom-exceptions/` |
| PY-112 | Exception hierarchy | concept | PY-111 | 2–4 | `exceptions/PY-112-exception-hierarchy/` |
| PY-113 | Production error handling | concept | PY-112 | 2–4 | `exceptions/PY-113-production-error-handling/` |
| PRJ-006 | File organizer | project | PY-113 | 12–20 | `projects/PRJ-006-file-organizer/` |
| CP-07 | Level 7 checkpoint — Exception Handling | checkpoint | PRJ-006 | 5–8 | `assessments/CP-07/` |

## Level 8 — Object-Oriented Programming

Budget: 88–169 hours. Folder: `oop/`.

| ID | Topic | Type | Prerequisite | Hours | Git location |
|---|---|---|---|---|---|
| PY-114 | Classes | concept | CP-07 | 3–6 | `oop/PY-114-classes/` |
| PY-115 | Objects | concept | PY-114 | 3–6 | `oop/PY-115-objects/` |
| PY-116 | Constructors | concept | PY-115 | 3–6 | `oop/PY-116-constructors/` |
| PY-117 | Attributes | concept | PY-116 | 3–6 | `oop/PY-117-attributes/` |
| PY-118 | Methods | concept | PY-117 | 3–6 | `oop/PY-118-methods/` |
| PY-119 | Instance variables | concept | PY-118 | 3–6 | `oop/PY-119-instance-variables/` |
| PY-120 | Class variables | concept | PY-119 | 3–6 | `oop/PY-120-class-variables/` |
| PY-121 | Instance methods | concept | PY-120 | 3–6 | `oop/PY-121-instance-methods/` |
| PY-122 | Class methods | concept | PY-121 | 3–6 | `oop/PY-122-class-methods/` |
| PY-123 | Static methods | concept | PY-122 | 3–6 | `oop/PY-123-static-methods/` |
| PY-124 | Encapsulation | concept | PY-123 | 3–6 | `oop/PY-124-encapsulation/` |
| PY-125 | Inheritance | concept | PY-124 | 3–6 | `oop/PY-125-inheritance/` |
| PY-126 | Composition | concept | PY-125 | 3–6 | `oop/PY-126-composition/` |
| PY-127 | Polymorphism | concept | PY-126 | 3–6 | `oop/PY-127-polymorphism/` |
| PY-128 | Abstraction | concept | PY-127 | 3–6 | `oop/PY-128-abstraction/` |
| PY-129 | Properties | concept | PY-128 | 3–6 | `oop/PY-129-properties/` |
| PY-130 | Dunder methods | concept | PY-129 | 3–6 | `oop/PY-130-dunder-methods/` |
| PY-131 | Dataclass foundations | concept | PY-130 | 3–6 | `oop/PY-131-dataclass-foundations/` |
| PY-132 | Abstract classes | concept | PY-131 | 3–6 | `oop/PY-132-abstract-classes/` |
| PY-133 | Method resolution order | concept | PY-132 | 3–6 | `oop/PY-133-method-resolution-order/` |
| PY-134 | SOLID principles | concept | PY-133 | 3–6 | `oop/PY-134-solid-principles/` |
| PY-135 | Git branches | concept | PY-134 | 2–4 | `oop/PY-135-git-branches/` |
| PY-136 | Git pull requests | concept | PY-135 | 2–4 | `oop/PY-136-git-pull-requests/` |
| PY-137 | Git code review | concept | PY-136 | 2–4 | `oop/PY-137-git-code-review/` |
| PRJ-007 | CLI application | project | PY-137 | 14–22 | `projects/PRJ-007-cli-application/` |
| CP-08 | Level 8 checkpoint — Object-Oriented Programming | checkpoint | PRJ-007 | 5–9 | `assessments/CP-08/` |

## Level 9 — Advanced Python

Budget: 51–99 hours. Folder: `advanced/`.

| ID | Topic | Type | Prerequisite | Hours | Git location |
|---|---|---|---|---|---|
| PY-138 | Iterables | concept | CP-08 | 3–6 | `advanced/PY-138-iterables/` |
| PY-139 | Iterators | concept | PY-138 | 3–6 | `advanced/PY-139-iterators/` |
| PY-140 | Generators and yield | concept | PY-139 | 3–6 | `advanced/PY-140-generators-and-yield/` |
| PY-141 | Generator expressions | concept | PY-140 | 3–6 | `advanced/PY-141-generator-expressions/` |
| PY-142 | Advanced decorators | concept | PY-141 | 3–6 | `advanced/PY-142-advanced-decorators/` |
| PY-143 | Closure patterns | concept | PY-142 | 3–6 | `advanced/PY-143-closure-patterns/` |
| PY-144 | Custom context managers | concept | PY-143 | 3–6 | `advanced/PY-144-custom-context-managers/` |
| PY-145 | Type hints | concept | PY-144 | 3–6 | `advanced/PY-145-type-hints/` |
| PY-146 | Generics | concept | PY-145 | 3–6 | `advanced/PY-146-generics/` |
| PY-147 | Enums | concept | PY-146 | 3–6 | `advanced/PY-147-enums/` |
| PY-148 | Dataclass patterns | concept | PY-147 | 3–6 | `advanced/PY-148-dataclass-patterns/` |
| PY-149 | Structural pattern matching | concept | PY-148 | 3–6 | `advanced/PY-149-structural-pattern-matching/` |
| PY-150 | Collections | concept | PY-149 | 3–6 | `advanced/PY-150-collections/` |
| PY-151 | Functools | concept | PY-150 | 3–6 | `advanced/PY-151-functools/` |
| PY-152 | Itertools | concept | PY-151 | 3–6 | `advanced/PY-152-itertools/` |
| CP-09 | Level 9 checkpoint — Advanced Python | checkpoint | PY-152 | 6–9 | `assessments/CP-09/` |

## Level 10 — Python Internals

Budget: 51–85 hours. Folder: `internals/`.

| ID | Topic | Type | Prerequisite | Hours | Git location |
|---|---|---|---|---|---|
| PY-153 | CPython basics | concept | CP-09 | 3–5 | `internals/PY-153-cpython-basics/` |
| PY-154 | Python execution model | concept | PY-153 | 3–5 | `internals/PY-154-python-execution-model/` |
| PY-155 | Bytecode | concept | PY-154 | 3–5 | `internals/PY-155-bytecode/` |
| PY-156 | Stack frames | concept | PY-155 | 3–5 | `internals/PY-156-stack-frames/` |
| PY-157 | Namespaces | concept | PY-156 | 3–5 | `internals/PY-157-namespaces/` |
| PY-158 | Object model | concept | PY-157 | 3–5 | `internals/PY-158-object-model/` |
| PY-159 | References | concept | PY-158 | 3–5 | `internals/PY-159-references/` |
| PY-160 | Identity and object lifetime | concept | PY-159 | 3–5 | `internals/PY-160-identity-and-object-lifetime/` |
| PY-161 | Mutability and aliasing | concept | PY-160 | 3–5 | `internals/PY-161-mutability-and-aliasing/` |
| PY-162 | Memory management | concept | PY-161 | 3–5 | `internals/PY-162-memory-management/` |
| PY-163 | Reference counting | concept | PY-162 | 3–5 | `internals/PY-163-reference-counting/` |
| PY-164 | Garbage collection | concept | PY-163 | 3–5 | `internals/PY-164-garbage-collection/` |
| PY-165 | Shallow copying | concept | PY-164 | 3–5 | `internals/PY-165-shallow-copying/` |
| PY-166 | Deep copying | concept | PY-165 | 3–5 | `internals/PY-166-deep-copying/` |
| PY-167 | GIL and interpreter build differences | concept | PY-166 | 3–5 | `internals/PY-167-gil-and-interpreter-build-differences/` |
| CP-10 | Level 10 checkpoint — Python Internals | checkpoint | PY-167 | 6–10 | `assessments/CP-10/` |

## Level 11 — Testing

Budget: 40–68 hours. Folder: `testing/`.

| ID | Topic | Type | Prerequisite | Hours | Git location |
|---|---|---|---|---|---|
| PY-168 | Assertions | concept | CP-10 | 3–5 | `testing/PY-168-assertions/` |
| PY-169 | Unit testing | concept | PY-168 | 3–5 | `testing/PY-169-unit-testing/` |
| PY-170 | Pytest | concept | PY-169 | 3–5 | `testing/PY-170-pytest/` |
| PY-171 | Fixtures | concept | PY-170 | 3–5 | `testing/PY-171-fixtures/` |
| PY-172 | Parameterization | concept | PY-171 | 3–5 | `testing/PY-172-parameterization/` |
| PY-173 | Mocking | concept | PY-172 | 3–5 | `testing/PY-173-mocking/` |
| PY-174 | Integration testing | concept | PY-173 | 3–5 | `testing/PY-174-integration-testing/` |
| PY-175 | Coverage | concept | PY-174 | 3–5 | `testing/PY-175-coverage/` |
| PY-176 | Test organization | concept | PY-175 | 3–5 | `testing/PY-176-test-organization/` |
| PY-177 | Test-driven thinking | concept | PY-176 | 3–5 | `testing/PY-177-test-driven-thinking/` |
| PY-178 | Git merge | concept | PY-177 | 2–4 | `testing/PY-178-git-merge/` |
| PY-179 | Git conflict resolution | concept | PY-178 | 2–4 | `testing/PY-179-git-conflict-resolution/` |
| CP-11 | Level 11 checkpoint — Testing | checkpoint | PY-179 | 6–10 | `assessments/CP-11/` |

## Level 12 — Debugging and Code Quality

Budget: 61–99 hours. Folder: `code-quality/`.

| ID | Topic | Type | Prerequisite | Hours | Git location |
|---|---|---|---|---|---|
| PY-180 | Traceback-led debugging | concept | CP-11 | 3–5 | `code-quality/PY-180-traceback-led-debugging/` |
| PY-181 | Debugging methodology | concept | PY-180 | 3–5 | `code-quality/PY-181-debugging-methodology/` |
| PY-182 | Pdb | concept | PY-181 | 3–5 | `code-quality/PY-182-pdb/` |
| PY-183 | Logging | concept | PY-182 | 3–5 | `code-quality/PY-183-logging/` |
| PY-184 | Log levels | concept | PY-183 | 3–5 | `code-quality/PY-184-log-levels/` |
| PY-185 | Structured logging | concept | PY-184 | 3–5 | `code-quality/PY-185-structured-logging/` |
| PY-186 | PEP 8 | concept | PY-185 | 3–5 | `code-quality/PY-186-pep-8/` |
| PY-187 | Linting | concept | PY-186 | 3–5 | `code-quality/PY-187-linting/` |
| PY-188 | Formatting | concept | PY-187 | 3–5 | `code-quality/PY-188-formatting/` |
| PY-189 | Type checking | concept | PY-188 | 3–5 | `code-quality/PY-189-type-checking/` |
| PY-190 | Refactoring | concept | PY-189 | 3–5 | `code-quality/PY-190-refactoring/` |
| PY-191 | Clean code | concept | PY-190 | 3–5 | `code-quality/PY-191-clean-code/` |
| PY-192 | Git rebase basics | concept | PY-191 | 2–4 | `code-quality/PY-192-git-rebase-basics/` |
| PRJ-008 | Log analyzer | project | PY-192 | 16–24 | `projects/PRJ-008-log-analyzer/` |
| CP-12 | Level 12 checkpoint — Debugging and Code Quality | checkpoint | PRJ-008 | 7–11 | `assessments/CP-12/` |

## Level 13 — Databases

Budget: 73–123 hours. Folder: `databases/`.

| ID | Topic | Type | Prerequisite | Hours | Git location |
|---|---|---|---|---|---|
| PY-193 | SQL fundamentals | concept | CP-12 | 4–7 | `databases/PY-193-sql-fundamentals/` |
| PY-194 | SQLite | concept | PY-193 | 4–7 | `databases/PY-194-sqlite/` |
| PY-195 | Python database connections | concept | PY-194 | 4–7 | `databases/PY-195-python-database-connections/` |
| PY-196 | CRUD | concept | PY-195 | 4–7 | `databases/PY-196-crud/` |
| PY-197 | Transactions | concept | PY-196 | 4–7 | `databases/PY-197-transactions/` |
| PY-198 | Parameterized queries | concept | PY-197 | 4–7 | `databases/PY-198-parameterized-queries/` |
| PY-199 | SQL injection prevention | concept | PY-198 | 4–7 | `databases/PY-199-sql-injection-prevention/` |
| PY-200 | PostgreSQL | concept | PY-199 | 4–7 | `databases/PY-200-postgresql/` |
| PY-201 | Connection pooling | concept | PY-200 | 4–7 | `databases/PY-201-connection-pooling/` |
| PY-202 | ORM concepts | concept | PY-201 | 4–7 | `databases/PY-202-orm-concepts/` |
| PY-203 | SQLAlchemy | concept | PY-202 | 4–7 | `databases/PY-203-sqlalchemy/` |
| PY-204 | Database migrations | concept | PY-203 | 4–7 | `databases/PY-204-database-migrations/` |
| PRJ-009 | Database-backed application | project | PY-204 | 18–28 | `projects/PRJ-009-database-backed-application/` |
| CP-13 | Level 13 checkpoint — Databases | checkpoint | PRJ-009 | 7–11 | `assessments/CP-13/` |

## Level 14 — HTTP and APIs

Budget: 107–184 hours. Folder: `api/`.

| ID | Topic | Type | Prerequisite | Hours | Git location |
|---|---|---|---|---|---|
| PY-205 | Networking fundamentals | concept | CP-13 | 4–7 | `api/PY-205-networking-fundamentals/` |
| PY-206 | HTTP | concept | PY-205 | 4–7 | `api/PY-206-http/` |
| PY-207 | Requests and responses | concept | PY-206 | 4–7 | `api/PY-207-requests-and-responses/` |
| PY-208 | Headers | concept | PY-207 | 4–7 | `api/PY-208-headers/` |
| PY-209 | HTTP methods | concept | PY-208 | 4–7 | `api/PY-209-http-methods/` |
| PY-210 | Status codes | concept | PY-209 | 4–7 | `api/PY-210-status-codes/` |
| PY-211 | JSON over HTTP | concept | PY-210 | 4–7 | `api/PY-211-json-over-http/` |
| PY-212 | REST | concept | PY-211 | 4–7 | `api/PY-212-rest/` |
| PY-213 | Authentication | concept | PY-212 | 4–7 | `api/PY-213-authentication/` |
| PY-214 | API keys | concept | PY-213 | 4–7 | `api/PY-214-api-keys/` |
| PY-215 | Tokens | concept | PY-214 | 4–7 | `api/PY-215-tokens/` |
| PY-216 | Pagination | concept | PY-215 | 4–7 | `api/PY-216-pagination/` |
| PY-217 | Rate limiting | concept | PY-216 | 4–7 | `api/PY-217-rate-limiting/` |
| PY-218 | Retries | concept | PY-217 | 4–7 | `api/PY-218-retries/` |
| PY-219 | Requests library | concept | PY-218 | 4–7 | `api/PY-219-requests-library/` |
| PY-220 | Httpx | concept | PY-219 | 4–7 | `api/PY-220-httpx/` |
| PY-221 | FastAPI foundations | concept | PY-220 | 4–7 | `api/PY-221-fastapi-foundations/` |
| PY-222 | FastAPI validation | concept | PY-221 | 4–7 | `api/PY-222-fastapi-validation/` |
| PY-223 | FastAPI dependency injection | concept | PY-222 | 4–7 | `api/PY-223-fastapi-dependency-injection/` |
| PY-224 | FastAPI testing | concept | PY-223 | 4–7 | `api/PY-224-fastapi-testing/` |
| PRJ-010 | API client and REST API | project | PY-224 | 20–32 | `projects/PRJ-010-api-client-and-rest-api/` |
| CP-14 | Level 14 checkpoint — HTTP and APIs | checkpoint | PRJ-010 | 7–12 | `assessments/CP-14/` |

## Level 15 — Concurrency

Budget: 92–156 hours. Folder: `concurrency/`.

| ID | Topic | Type | Prerequisite | Hours | Git location |
|---|---|---|---|---|---|
| PY-225 | Sequential execution | concept | CP-14 | 4–7 | `concurrency/PY-225-sequential-execution/` |
| PY-226 | CPU-bound versus I/O-bound work | concept | PY-225 | 4–7 | `concurrency/PY-226-cpu-bound-versus-i-o-bound-work/` |
| PY-227 | Threads | concept | PY-226 | 4–7 | `concurrency/PY-227-threads/` |
| PY-228 | Threading primitives | concept | PY-227 | 4–7 | `concurrency/PY-228-threading-primitives/` |
| PY-229 | Locks | concept | PY-228 | 4–7 | `concurrency/PY-229-locks/` |
| PY-230 | Race conditions | concept | PY-229 | 4–7 | `concurrency/PY-230-race-conditions/` |
| PY-231 | Deadlocks | concept | PY-230 | 4–7 | `concurrency/PY-231-deadlocks/` |
| PY-232 | Thread pools | concept | PY-231 | 4–7 | `concurrency/PY-232-thread-pools/` |
| PY-233 | Processes | concept | PY-232 | 4–7 | `concurrency/PY-233-processes/` |
| PY-234 | Multiprocessing | concept | PY-233 | 4–7 | `concurrency/PY-234-multiprocessing/` |
| PY-235 | Process pools | concept | PY-234 | 4–7 | `concurrency/PY-235-process-pools/` |
| PY-236 | Async programming | concept | PY-235 | 4–7 | `concurrency/PY-236-async-programming/` |
| PY-237 | Event loop | concept | PY-236 | 4–7 | `concurrency/PY-237-event-loop/` |
| PY-238 | Async and await | concept | PY-237 | 4–7 | `concurrency/PY-238-async-and-await/` |
| PY-239 | Asyncio tasks | concept | PY-238 | 4–7 | `concurrency/PY-239-asyncio-tasks/` |
| PY-240 | Async HTTP | concept | PY-239 | 4–7 | `concurrency/PY-240-async-http/` |
| PRJ-011 | Concurrent API collector | project | PY-240 | 20–32 | `projects/PRJ-011-concurrent-api-collector/` |
| CP-15 | Level 15 checkpoint — Concurrency | checkpoint | PRJ-011 | 8–12 | `assessments/CP-15/` |

## Level 16 — Systems and Automation

Budget: 82–139 hours. Folder: `automation/`.

| ID | Topic | Type | Prerequisite | Hours | Git location |
|---|---|---|---|---|---|
| PY-241 | Linux automation | concept | CP-15 | 4–7 | `automation/PY-241-linux-automation/` |
| PY-242 | Operating-system processes | concept | PY-241 | 4–7 | `automation/PY-242-operating-system-processes/` |
| PY-243 | Subprocesses | concept | PY-242 | 4–7 | `automation/PY-243-subprocesses/` |
| PY-244 | Environment variables | concept | PY-243 | 4–7 | `automation/PY-244-environment-variables/` |
| PY-245 | Signals | concept | PY-244 | 4–7 | `automation/PY-245-signals/` |
| PY-246 | Sockets | concept | PY-245 | 4–7 | `automation/PY-246-sockets/` |
| PY-247 | TCP | concept | PY-246 | 4–7 | `automation/PY-247-tcp/` |
| PY-248 | UDP | concept | PY-247 | 4–7 | `automation/PY-248-udp/` |
| PY-249 | SSH | concept | PY-248 | 4–7 | `automation/PY-249-ssh/` |
| PY-250 | Remote execution | concept | PY-249 | 4–7 | `automation/PY-250-remote-execution/` |
| PY-251 | File automation | concept | PY-250 | 4–7 | `automation/PY-251-file-automation/` |
| PY-252 | Log processing | concept | PY-251 | 4–7 | `automation/PY-252-log-processing/` |
| PY-253 | Scheduling | concept | PY-252 | 4–7 | `automation/PY-253-scheduling/` |
| PY-254 | Monitoring | concept | PY-253 | 4–7 | `automation/PY-254-monitoring/` |
| PRJ-012 | Linux server checker and SSH tool | project | PY-254 | 18–28 | `projects/PRJ-012-linux-server-checker-and-ssh-tool/` |
| CP-16 | Level 16 checkpoint — Systems and Automation | checkpoint | PRJ-012 | 8–13 | `assessments/CP-16/` |

## Level 17 — Python for DevOps

Budget: 80–149 hours. Folder: `devops/`.

| ID | Topic | Type | Prerequisite | Hours | Git location |
|---|---|---|---|---|---|
| PY-255 | Linux operational scripts | concept | CP-16 | 4–8 | `devops/PY-255-linux-operational-scripts/` |
| PY-256 | Git automation | concept | PY-255 | 4–8 | `devops/PY-256-git-automation/` |
| PY-257 | GitHub APIs | concept | PY-256 | 4–8 | `devops/PY-257-github-apis/` |
| PY-258 | Docker automation | concept | PY-257 | 4–8 | `devops/PY-258-docker-automation/` |
| PY-259 | Kubernetes automation | concept | PY-258 | 4–8 | `devops/PY-259-kubernetes-automation/` |
| PY-260 | Jenkins integration | concept | PY-259 | 4–8 | `devops/PY-260-jenkins-integration/` |
| PY-261 | GitHub Actions | concept | PY-260 | 4–8 | `devops/PY-261-github-actions/` |
| PY-262 | AWS APIs | concept | PY-261 | 4–8 | `devops/PY-262-aws-apis/` |
| PY-263 | Ansible integration | concept | PY-262 | 4–8 | `devops/PY-263-ansible-integration/` |
| PY-264 | Terraform integration | concept | PY-263 | 4–8 | `devops/PY-264-terraform-integration/` |
| PY-265 | Database operations | concept | PY-264 | 4–8 | `devops/PY-265-database-operations/` |
| PY-266 | Monitoring integration | concept | PY-265 | 4–8 | `devops/PY-266-monitoring-integration/` |
| PY-267 | Secrets management | concept | PY-266 | 4–8 | `devops/PY-267-secrets-management/` |
| PRJ-013 | Docker and Kubernetes health checker | project | PY-267 | 20–32 | `projects/PRJ-013-docker-and-kubernetes-health-checker/` |
| CP-17 | Level 17 checkpoint — Python for DevOps | checkpoint | PRJ-013 | 8–13 | `assessments/CP-17/` |

## Level 18 — Production Python

Budget: 197–338 hours. Folder: `production/`.

| ID | Topic | Type | Prerequisite | Hours | Git location |
|---|---|---|---|---|---|
| PY-268 | Application architecture | concept | CP-17 | 4–8 | `production/PY-268-application-architecture/` |
| PY-269 | Configuration management | concept | PY-268 | 4–8 | `production/PY-269-configuration-management/` |
| PY-270 | Dependency management in production | concept | PY-269 | 4–8 | `production/PY-270-dependency-management-in-production/` |
| PY-271 | Application logging | concept | PY-270 | 4–8 | `production/PY-271-application-logging/` |
| PY-272 | Error handling at service boundaries | concept | PY-271 | 4–8 | `production/PY-272-error-handling-at-service-boundaries/` |
| PY-273 | Retry policies | concept | PY-272 | 4–8 | `production/PY-273-retry-policies/` |
| PY-274 | Exponential backoff | concept | PY-273 | 4–8 | `production/PY-274-exponential-backoff/` |
| PY-275 | Caching | concept | PY-274 | 4–8 | `production/PY-275-caching/` |
| PY-276 | Application security | concept | PY-275 | 4–8 | `production/PY-276-application-security/` |
| PY-277 | Testing strategy | concept | PY-276 | 4–8 | `production/PY-277-testing-strategy/` |
| PY-278 | Packaging | concept | PY-277 | 4–8 | `production/PY-278-packaging/` |
| PY-279 | Dockerization | concept | PY-278 | 4–8 | `production/PY-279-dockerization/` |
| PY-280 | Deployment | concept | PY-279 | 4–8 | `production/PY-280-deployment/` |
| PY-281 | Performance measurement | concept | PY-280 | 4–8 | `production/PY-281-performance-measurement/` |
| PY-282 | Scalability | concept | PY-281 | 4–8 | `production/PY-282-scalability/` |
| PY-283 | Maintainability | concept | PY-282 | 4–8 | `production/PY-283-maintainability/` |
| PRJ-014 | AWS inventory and deployment planner | project | PY-283 | 24–36 | `projects/PRJ-014-aws-inventory-and-deployment-planner/` |
| CP-18 | Level 18 checkpoint — Production Python | checkpoint | PRJ-014 | 9–14 | `assessments/CP-18/` |
| CAP-001 | Infrastructure Automation Platform | capstone | CP-18 | 100–160 | `projects/CAP-001-infrastructure-automation-platform/` |

Total planned budget: **1253–2188 hours**, excluding additional revision.
