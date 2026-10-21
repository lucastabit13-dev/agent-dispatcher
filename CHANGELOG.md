# Changelog

## 0.2.0 — always propose a plan

- Every new dispatcher task now gets a concrete multi-agent proposal and explicit solo option, including simple rewrites.
- Infer worker roles from natural requests; users do not need to divide research into subtasks.
- Wait for the user's choice before execution. Honor an explicit prior solo choice without asking again.
- Explain overhead and recommend solo when appropriate without omitting the multi-agent alternative.
- Label conceptual plans unavailable when host limits prevent workers. Keep the approval gate, worker cap, ownership rules, and verification requirements.
- Update project instructions, acceptance scenarios, and deployment steps to match the new routing policy.

Structural validation and package checks do not establish live model behavior. Repeat fresh-chat acceptance tests after refreshing the installation.

## 0.1.0 — early release

- Skill-based task triage, with solo execution for small or tightly coupled tasks.
- Concrete delegation proposals and explicit confirmation before assignments.
- One coordinator and at most three active workers, subject to host capacity.
- Bundled worker contract, dependency handling, shared-file ownership, and evidence checks.
- Repository marketplace, dependency-free structural validation, GitHub Actions, and archive packaging.

Local installation and enabled status were checked with Codex tools. Picker discovery and a simple invocation were confirmed by the user. Live worker orchestration and comparative efficiency are not yet verified. No performance claims are made.
