# Agent Dispatcher implementation plan

## Product contract

Input: a user task supplied with the plugin selected, plus optional output requirements, worker cap, and priority (speed, thoroughness, or lower usage).

Output: one integrated result, concise verification evidence, unresolved limitations, and truthful progress. Require explicit confirmation of the concrete delegation proposal before starting workers. Otherwise ask only when missing information materially blocks useful work.

Default policy: one coordinator, zero to three active workers, no recursive delegation, bounded by available host capacity. Three is a maximum, not a default team size. Keep small tasks local and advise against unnecessary delegation. After approval, run independent research or separately owned implementation tasks concurrently. Wait for prerequisites before starting dependent work.

## Delegation approval gate

1. Assess whether parallel work offers a meaningful benefit. Recommend solo execution with a brief reason if delegation is unnecessary or inefficient.
2. If useful or specifically requested, show a proposal listing each worker's role, scope or owned files, deliverable, and dependencies. Explain what the coordinator will do and the expected speed/usage tradeoffs without inventing estimates.
3. Ask for confirmation of this concrete plan. Wait for explicit approval before spawning workers or sending assignments. A plugin mention, general instruction to use agents, silence, or elapsed time is not confirmation of the plan.
4. If declined, continue solo. If the user edits the plan, show the revised proposal and wait for confirmation.
5. Execute the approved scope. Obtain fresh confirmation before adding workers or materially changing their scope. Routine execution and bounded retries within unchanged approved scope do not require repeated confirmation.

Proposal format:

| Agent | Task and ownership | Deliverable | Dependencies |
| --- | --- | --- | --- |
| Coordinator | Integration and verification | Final checked result | Worker returns |
| Worker 1 | Specific independent assignment | Concrete output | Required inputs |

Add rows only for proposed workers, up to three. Finish with the benefit/tradeoff explanation and: "Approve this delegation plan, change it, or have me work solo?"

## Architecture

The plugin skill supplies task triage, advice, the confirmation gate, and delegation instructions. The host supplies agent tools, permissions, available slots, and execution lifecycle. The coordinator creates focused briefs, gets confirmation, starts approved workers, does useful remaining work, checks returns, and integrates them. Progress Checklist remains a separate optional skill; do not silently modify or require it.

## Milestone 1: confirm packaging and capabilities

- Inspect supported installed plugin examples and current official documentation as needed.
- Identify the required manifest, skill location, metadata, and registration path.
- Verify the host exposes subagent tools and determine session limits.
- Record the supported installation procedure and fallback behavior.

Acceptance: a minimal plugin can be discovered and invoked using the supported host flow. Do not label a folder or draft skill as installed.

## Milestone 2: implement the orchestration skill

- Write concise triggering metadata and the routing policy, including advice against unnecessary delegation and the mandatory confirmation gate.
- Use task-brief.md as the worker contract.
- Implement instructions for useful delegation, ownership, dependencies, worker failure, integration, and evidence checking.
- Keep user requests and host permission rules authoritative.
- Add a final response contract and optional Progress Checklist integration.

Acceptance: a simple request gets a brief recommendation to work solo and stays with the coordinator; an independent task produces a concrete proposal and no workers until approval, then bounded assignments and one checked result.

## Milestone 3: validate behavior

Run realistic cases using the same tool availability and permissions as normal use:

| Case | Expected behavior |
| --- | --- |
| One-sentence rewrite | Coordinator handles it directly |
| Simple task with a general request for agents | Advise against unnecessary delegation; show a proposal only if still requested; wait for approval before launching |
| Useful parallel task, no confirmation yet | Show each worker's role and deliverable; start zero workers |
| User is silent or declines | Silence: no workers; decline: continue solo |
| User edits the proposed roles | Present revised proposal and wait for confirmation |
| Three useful independent workstreams | Propose up to three workers; launch only after approval and within host capacity |
| Four proposed simultaneous workers | Reduce to at most three active workers or use approved sequential assignments |
| Material scope change or extra worker | Obtain fresh confirmation before executing the change |
| Compare two products | Independent research workers; coordinator verifies sources and compares |
| Change separate frontend and backend files | Distinct ownership, agreed interface, integration check |
| Task B needs output from task A | Start B only after A's required output exists |
| Two workers need one shared file | Coordinator owns the shared edit |
| One worker fails | Bounded retry or coordinator completes the missing work |
| No agent tools available | Truthful sequential execution |
| User changes requirements | Redirect or stop obsolete assignments; preserve completed useful work |
| External action needs permission | Prepare reviewable output and follow the applicable permission requirement |

Acceptance: no invented workers, overlapping edits, unsupported claims of completion, or permission bypasses.

## Milestone 4: measure efficiency and install

- Compare sequential and delegated runs on the same representative tasks.
- Record elapsed time, worker count, available usage metrics, and output correctness.
- Avoid unsupported cost estimates if usage data is unavailable.
- Tune the worker cap and delegation threshold based on results.
- Validate packaging, persist skill source through its required Git workflow, and test actual @ discovery in a fresh session.

Acceptance: installation is confirmed and the usage example works. Report measured tradeoffs; parallel execution may use more tokens even when it reduces elapsed time.

## Definition of done

The plugin is discoverable, routes simple and parallel tasks correctly, respects host limits, integrates and verifies worker outputs, handles failures, and has passed the validation cases. This setup scaffold alone does not meet that definition.
