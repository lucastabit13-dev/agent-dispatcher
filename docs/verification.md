# Verification evidence

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

Not verified: desktop picker discovery after refresh, fresh-chat invocation, live approved worker execution, and comparable sequential/delegated speed or usage. No workers were spawned. The current chat's loaded skill list cannot establish fresh-session discovery. GitHub CI has been prepared but has not run remotely. No remote repository or publication was created. No license grant was selected.

Next acceptance check: restart or refresh the desktop app, start a fresh chat, select Agent Dispatcher in the host picker, and request a one-sentence rewrite. Confirm that it completes directly. Test a useful parallel task next: it should propose concrete roles and wait for approval before any workers start.
