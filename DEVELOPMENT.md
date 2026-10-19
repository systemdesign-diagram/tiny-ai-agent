# Development Checklist

Statuses reflect the initial repository scaffold on creation. Update them only when there is evidence in code, tests, or documentation.

| ID | Task | Initial status | Evidence / next action |
|---|---|---|---|
| T1 | Define the agent's goal and scope | In progress | Review and approve the scope in `README.md`. |
| T2 | Set up the project structure | In progress | Add the scaffold files and verify imports. |
| T3 | Integrate an LLM API | Not started | Implement the provider client and add a testable configuration path. |
| T4 | Implement tool calling | Not started | Define allowed tools and validate tool arguments before execution. |
| T5 | Add conversation memory | In progress | Start with a simple in-process message history and tests. |
| T6 | Implement error handling | In progress | Define clear errors for missing configuration and provider failures. |
| T7 | Test the agent | In progress | Add tests for memory and tool behavior; run the test suite. |
| T8 | Prepare the newsletter tutorial | In progress | Draft the outline and align topics with verified implementation progress. |

## Milestones

1. **M1 — Scope and scaffold:** project purpose, structure, and initial tests.
2. **M2 — First LLM response:** provider integration works locally.
3. **M3 — Tool use:** the agent can select and safely execute an allowed tool.
4. **M4 — Memory and reliability:** conversation history and error handling are tested.
5. **M5 — Tutorial ready:** newsletter accurately explains the implementation.

## Blockers

Record each blocker with:
- What is blocked
- Evidence / reproduction steps
- Owner
- Next action
- Status

## Update rule

Do not change a task to `Complete` unless there is evidence (a merged code change, a passing test, or a reviewed document). Record uncertain items as `Needs verification`.
