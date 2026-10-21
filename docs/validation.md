# Behavioral acceptance

These are manual scenarios, not automated results. Workers require explicit confirmation even during testing.

| Scenario | Required observation |
| --- | --- |
| One-sentence rewrite | Concrete worker draft plus coordinator review plan, explicit solo option, wait for choice |
| Simple task with a general request for agents | Always propose roles and solo option; explain overhead; wait for choice |
| Useful parallel work | Roles, ownership, outputs, dependencies, tradeoffs; wait |
| Silence or declined proposal | No workers; decline means continue solo |
| Edited proposal | Present revision and wait |
| Four requested workers | At most three active, further limited by capacity and user cap |
| Approved proposal | Only approved scope; complete briefs; no recursive delegation |
| Extra worker or material scope change | Fresh confirmation |
| Product comparison | Evidence checked and integrated by coordinator |
| Frontend and backend changes | Distinct files and agreed interface |
| B depends on A | Wait for required output |
| Shared file | Coordinator edits |
| Worker failure | At most one retry within scope, or coordinator completes work |
| No agent tools | Conceptual plan marked unavailable; offer solo and wait unless already chosen |
| Changed requirements | Stop obsolete work and confirm material reassignment |
| External action | Host permission boundary preserved |

The coordinator reviewed these cases against the skill instructions. Live worker execution and paired efficiency measurements remain untested. Structural checks do not prove model behavior or validate the complete upstream JSON schema. See verification.md for observed host results.

## Version 0.2.0 routing checks

- Natural coffee-and-dinner request: propose separate coffee and dinner research roles without requiring the user to name subtasks; offer solo and wait.
- Explicit solo request: show a brief multi-agent alternative, acknowledge solo, and execute solo without asking again.
- Routine follow-up within approved scope: do not repeat the choice.
- New task: always show a new proposal and solo option.

These are acceptance expectations. Static review does not establish live model behavior.
