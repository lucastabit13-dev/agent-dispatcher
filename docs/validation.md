# Behavioral acceptance

These are manual scenarios, not automated results. Workers require explicit confirmation even during testing.

| Scenario | Required observation |
| --- | --- |
| One-sentence rewrite | Complete solo |
| Simple task with a general request for agents | Recommend solo; no launch without concrete approval |
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
| No agent tools | Truthful sequential fallback |
| Changed requirements | Stop obsolete work and confirm material reassignment |
| External action | Host permission boundary preserved |

The coordinator reviewed these cases against the skill instructions. Live worker execution and paired efficiency measurements remain untested. Structural checks do not prove model behavior or validate the complete upstream JSON schema. See verification.md for observed host results.
