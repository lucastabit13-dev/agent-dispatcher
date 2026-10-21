# Verification evidence

## Version 0.2.0 update — October 21, 2026

- Changed routing to always present a concrete multi-agent proposal and solo alternative for each new task, including small tasks. User choice is required before execution unless solo was explicitly selected already.
- Project structural validation and release archive integrity checks passed.
- Refreshed the installed plugin through `codex plugin add agent-dispatcher@agent-dispatcher-local --json`.
- Host listing reports version 0.2.0, installed=true, enabled=true.
- Source and installed SKILL.md SHA256 both equal `774850BED716903BC8FA8C646BCDC5C3537CC7A164395EBC0952992E2A237DE9`.
- Reviewed routing for simple rewrites, natural coffee-and-dinner requests, prior solo choices, unavailable tools, and unchanged follow-ups. This was an instruction review, not live behavioral testing.
- No workers were started. Restart or refresh the host and open a fresh chat to test the new routing; prior 0.1.0 behavior is not evidence of the 0.2.0 policy.

## Version 0.1.0 history

Verified October 20, 2026, in the local Windows Codex environment.

| Check | Observed result |
| --- | --- |
| Official packaging documentation and installed Progress Checklist example | Root plugin.json and root skills directory supported |
| Local CLI help | Marketplace registration, list and plugin add commands supported |
| python scripts/validate.py | Passed: catalog resolution, manifest identity, skill metadata, bundled references, worker brief consistency |
| Skill Creator quick_validate.py | Could not run: PyYAML missing in default and bundled Python |
| Manual workflow review | Instructions cover the acceptance cases in validation.md; this is not a behavioral execution test |
| Initial discovery before registration | No available plugin returned |
| codex plugin marketplace add . | Local marketplace registered successfully |
| Marketplace listing after registration | agent-dispatcher@agent-dispatcher-local version 0.1.0 available |
| codex plugin add agent-dispatcher@agent-dispatcher-local --json | Installed into the Codex plugin cache successfully |
| Subsequent plugin list | installed=true, enabled=true, version=0.1.0 |
| Source versus installed SKILL.md SHA256 | Both 5845CC23C0176CCE4E4D87601BC93D28175C24D953E06936E6C735AB0DC58CB4 |

Registration and installation required normal host approval for writes to user settings/cache. No hand editing of those files was used.

The user subsequently confirmed that Agent Dispatcher appeared in the desktop picker and that a fresh-chat one-sentence rewrite completed directly. Those two checks are user-reported results, rather than independently observed tool runs.

Not verified: live approved worker execution and comparable sequential/delegated speed or usage. No workers were spawned during development. GitHub CI has been prepared but has not run remotely. No remote repository or publication was created. No license grant was selected.

The user also reported that a coffee-and-dinner request completed without workers. That outcome alone does not establish a failure: the dispatcher may choose solo execution for short tasks. Whether it explained its delegation decision was not recorded. Further behavioral testing should cover natural requests with independent work, proposal approval, and actual worker execution.

Next acceptance check: request a useful parallel task. It should assess delegation, propose concrete roles when worthwhile, and wait for approval before any workers start. Full PLAN.md acceptance remains open until live orchestration and efficiency evaluation have been performed.
