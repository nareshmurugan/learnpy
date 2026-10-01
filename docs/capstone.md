# CAP-001 — Infrastructure Automation Platform

This is a milestone plan, not an assigned implementation. Prerequisite: CP-18
PASSED. Budget: 100–160 hours before additional revision. Final pass: 90/100 plus
all mastery checks. Naresh approves each milestone's requirements and review
before the next milestone starts; overall CAP-001 remains active until all pass.

## Intended architecture

```text
                     Authenticated Python API
                               |
                 Inventory / health / job services
                     /          |          \
                AWS adapter  Kubernetes    Linux/SSH
                    |         adapter      adapter
                    +------------+------------+
                                 |
                            PostgreSQL
                                 |
                     Inventory and execution history
```

Possible technologies already studied: FastAPI, PostgreSQL, SQLAlchemy, async
HTTP, SDK clients, structured logging, pytest, Docker, and CI. Choose components
based on requirements rather than using every technique for its own sake.

## Milestone reviews

| Milestone | Deliverables | Acceptance evidence |
|---|---|---|
| M1 — Problem and design | Users, inputs/outputs, constraints, threat model, diagrams, pseudocode, API/data contracts | Naresh reviews scope, separation of responsibilities, and failure cases |
| M2 — Local inventory | Config, models, schema/migrations, local/mock adapters, CRUD | Unit/integration tests; migration and rollback/recovery reasoning |
| M3 — Authenticated API | Validation, authentication/authorization, pagination, error responses | Unauthorized/invalid requests fail appropriately; contract tests |
| M4 — Read-only integrations | AWS, Kubernetes, Linux/SSH inventory on fixtures and controlled systems | Mocked failure cases plus explicitly approved controlled integration runs |
| M5 — Concurrent collection | Bounded work, timeouts, retries/backoff, cancellation, persistence | Rate-limit, partial-failure, cancellation, and race-condition tests |
| M6 — Operational behavior | Logs, health endpoints, config handling, secret references, caching where justified | Diagnosis from logs; no secrets in repository or logs; documented restart behavior |
| M7 — Packaging and delivery | Dependency metadata, Docker, CI, deployment/runbook and recovery plan | Clean environment build; tests in CI; reviewed demonstration deployment |
| M8 — Final demonstration | User scenarios, architecture explanation, performance measurements, limitations | Independent unfamiliar change/debug task; all requirements and mastery verified |

## Requirements boundaries

Start with local fixtures and read-only adapters. If later milestones need cloud
resources or remote changes, Naresh sets an explicit test environment, scope,
credentials, and review step first. Deployment planning can use mocks; real
deployment is not required merely to pass a Python concept. Store credentials
outside the repository and test logs for redaction where needed.

Require a problem-solving plan, sample input/output, failure behavior, edge cases,
tests, and explanation per milestone. Raajashree designs and implements the work.
Provide progressive hints only when needed, then verify understanding on a new
problem. Do not distribute a full capstone solution.

The final review must consider architecture, correctness, error handling, security,
testing, observability, maintainability, performance evidence, Git history, and
independence. Save milestone reviews in `notes/milestones/` and final feedback in
`notes/review.md`; record CAP-001 PASSED only after all milestones and CP-18 pass.
