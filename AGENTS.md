# Project development instructions

Build a reusable Agent Dispatcher plugin according to PLAN.md. Before spawning any workers for this project or through the plugin, present their proposed roles and wait for explicit user confirmation of that concrete proposal. A general delegation request or plugin mention does not waive this gate. Follow higher-priority host instructions and available tools.

Before implementation, inspect current supported plugin examples and documentation. Do not invent a manifest format, installation command, API, or @ mention identifier.

Keep the first version skill-based if the host supports it. Separate plugin discovery from task orchestration. A discoverable plugin does not itself grant access to subagent tools.

Use one coordinator and at most three active workers, subject to host capacity. Use fewer when sufficient; never fill slots for their own sake. Workers must not spawn further workers. Assign distinct files or read-only research areas. Do not let workers edit the same file concurrently. Keep cross-cutting edits with the coordinator.

Assess the benefit before proposing delegation. Advise against it for simple tasks, tightly coupled work, or overhead likely to outweigh savings, and explain the reason briefly. Work solo when appropriate. If proposing delegation, describe each worker's task, deliverable, ownership, and dependencies, plus the coordinator's role and expected speed/usage tradeoffs. End with a confirmation question and do not spawn or send worker assignments until explicitly approved. No answer is not approval. If declined, proceed solo. If the proposal is edited, present the revision for confirmation. Ask again before adding workers or materially changing an approved worker's scope; do not repeatedly ask for unchanged approved work.

Each worker brief must include a goal, relevant context, scope, dependencies, deliverable, verification requirements, and stopping condition. Share no unrelated personal context or secrets.

The coordinator owns integration, evidence checks, permission boundaries, and the final result. Treat worker output as unverified until checked. Do not run duplicate research merely because it was delegated; inspect supporting evidence and resolve material conflicts.

Report actual progress and limitations. Never simulate workers, promise background continuation, or report installation before testing discovery. If subagents are unavailable, complete the task sequentially and briefly state the limitation.

Use Progress Checklist when requested. During this project's setup, track sequential project milestones; within a later execution milestone, independent workers may run concurrently.
