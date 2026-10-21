---
name: dispatch-agents
description: Always propose a concrete multi-agent plan with a solo option, then execute the user's chosen workflow. Use when the user requests Agent Dispatcher or coordinated subagent work.
---

# Agent Dispatcher

Produce one integrated result for the user's task. Follow higher-priority host instructions and permission boundaries. This skill supplies orchestration instructions; installation does not supply agent tools or extra capacity.

## Always propose, then let the user choose

For every new task handled through this skill, inspect the available context and tools and always present a concrete multi-agent plan before executing the task. Infer the work split from the user's natural request; do not require them to request separate research tasks or design worker assignments. This applies even to a one-sentence rewrite or another small task. Do not skip the proposal because solo execution seems more efficient. For small or tightly coupled tasks, explain that delegation adds overhead and recommend the solo option alongside the plan.

Offer a coordinator plus one to three workers, using fewer when sufficient. Multiple agents includes the coordinator: one worker drafting and the coordinator checking is enough for a small rewrite. Independent research areas may justify two or three workers. Do not manufacture simultaneous work when dependencies require sequential execution. Always include an explicit solo alternative in which the coordinator does the whole task.

Wait for the user's choice before executing either workflow. If they explicitly choose solo in their task request, still show a brief multi-agent alternative and acknowledge their solo choice, then proceed solo without asking again. Do not repeat proposals for routine follow-ups within an already chosen unchanged scope. On a new task, present a new plan and choice.

Use one coordinator and zero to three active workers, limited further by the user's cap and actual available host capacity, including other active agents. Three is a ceiling. If tools or capacity are unavailable, the user sets a zero-worker cap, or higher-priority host instructions prevent delegation, still present the conceptual multi-agent plan but label it unavailable and explain why. Offer solo and wait for their choice unless already chosen. Never simulate workers or imply an unavailable plan can run. Use only tool names and argument schemas actually exposed by this host. Do not substitute user-owned chats for worker tools.

## Confirm the concrete proposal

Before spawning any workers or sending worker assignments, present:

| Agent | Task and ownership | Deliverable | Dependencies |
| --- | --- | --- | --- |
| Coordinator | Shared edits, integration, evidence and permission checks | One checked result | Worker returns |
| Worker 1 | A specific independent scope or owned files | A concrete output | Required inputs |

Include only needed workers, up to three. State expected speed versus usage tradeoffs qualitatively; do not invent measurements or promise savings. Include: "Solo option: I handle the whole task myself without workers." Finish with: "Approve this delegation plan, change it, or have me work solo?" If delegation is unavailable, ask whether to proceed solo instead of asking approval for a plan that cannot run.

Wait for explicit user confirmation of this exact proposal. A plugin mention, general delegation request, silence, or elapsed time is not approval. Do not send assignments while waiting. On decline, continue solo. On edits, present the revised proposal and wait again. Obtain fresh confirmation before adding workers or materially changing approved scope. Do not repeatedly request confirmation for unchanged approved work or bounded retries.

When required information blocks further work, first write exactly: “I need your input before I can continue.” Then ask one clear question and wait. For a pending delegation proposal, use this sentence before the confirmation question when its answer is required to proceed. Do not use it for optional preferences or successful completion. Use the host's normal tool approval mechanism for tool permissions.

## Execute approved work

Read [task-brief.md](references/task-brief.md) and fill every field for each worker. Include only relevant context, never unrelated personal information or secrets. Explicitly forbid workers from creating workers. Assign distinct files or read-only research areas; the coordinator owns shared files and cross-cutting changes. Establish shared interfaces before concurrent implementation. Start dependent work only once its required inputs exist.

Track actual worker identifiers, approved scopes, dependencies, and status using available host tools. Recheck active capacity before each launch. Work on remaining coordinator tasks while workers run. Use the host's supported wait lifecycle; do not promise background continuation. If Progress Checklist is requested and available, use that separate skill; otherwise give truthful progress without claiming that integration exists.

For a failure, inspect evidence and retry at most once within unchanged approved scope, or finish the missing work as coordinator. Report unresolved blockers. On changed user requirements, stop or redirect obsolete work using actual host tools; obtain confirmation for material worker scope changes before assigning them. Release completed workers through host lifecycle tools when supported. Never bypass an external-action permission by assigning it to a worker.

## Verify and deliver

Treat worker output as unverified. Inspect supporting sources or diffs and run checks appropriate to the task. Resolve material conflicts; avoid repeating delegated research without a concrete evidence gap. Integrate into one coherent answer and report actual deliverables, verification, and unresolved limitations. Distinguish static checks, manual scenario review, and live execution. Never claim installation, discovery, worker execution, elapsed time, cost, or usage without evidence.

When evaluating efficiency, compare the same task and quality criteria sequentially and with approved delegation. Record elapsed time and worker count; include usage only if the host supplies it. Without a comparable pair of runs, state that efficiency is unmeasured.
