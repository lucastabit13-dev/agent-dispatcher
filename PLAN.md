# Agent Dispatcher implementation plan

## Product contract

Input: a user task supplied with the plugin selected, plus optional output requirements, worker cap, and priority (speed, thoroughness, or lower usage).

Output: one integrated result, concise verification evidence, unresolved limitations, and truthful progress. Require explicit confirmation of the concrete delegation proposal before starting workers. Otherwise ask only when missing information materially blocks useful work.

Default policy: one coordinator, zero to three active workers, no recursive delegation, bounded by available host capacity. Three is a maximum, not a default team size. Always show a concrete multi-agent proposal and explicit solo option for every new task, including small tasks; explain when solo is more efficient and let the user choose. After approval, run independent research or separately owned implementation tasks concurrently. Wait for prerequisites before starting dependent work.

## Delegation approval gate

1. Assess the task and infer concrete worker roles from the natural request. Always propose a multi-agent plan, even for simple tasks; explain overhead and recommend solo when appropriate without skipping the proposal.
2. Always show a proposal listing each worker's role, scope or owned files, deliverable, and dependencies. Explain what the coordinator will do and the expected speed/usage tradeoffs without inventing estimates.
3. Include an explicit solo alternative and ask the user to choose. If they already explicitly chose solo, show a brief multi-agent alternative and proceed solo without asking again. Otherwise wait before executing either workflow. Label conceptual plans unavailable if host tools or capacity prevent delegation. Ask for confirmation of this concrete plan before any delegation. Wait for explicit approval before spawning workers or sending assignments. A plugin mention, general instruction to use agents, silence, or elapsed time is not confirmation of the plan.
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

Acceptance: every new task produces a concrete multi-agent proposal and explicit solo option before execution. Small tasks may include a recommendation for solo, but the user chooses. An explicit prior solo choice does not need reconfirmation. No workers start without approval of their concrete roles.

## Milestone 3: validate behavior

Run realistic cases using the same tool availability and permissions as normal use:

| Case | Expected behavior |
| --- | --- |
| One-sentence rewrite | Propose a worker draft plus coordinator review, offer solo, and wait for choice |
| Simple task with a general request for agents | Always show a concrete plan plus solo option; explain overhead and wait for choice |
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
| No agent tools available | Label conceptual plan unavailable; offer solo and wait unless already chosen |
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
