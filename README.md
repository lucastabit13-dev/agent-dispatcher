# Agent Dispatcher

A skill-based plugin that handles small tasks directly and coordinates approved independent subagents. Version 0.1.0 uses one coordinator and at most three active workers, limited by user preference and host capacity.

Before launching or assigning workers, it presents concrete roles, ownership, deliverables, dependencies, and speed/usage tradeoffs, then waits for explicit confirmation. Workers cannot create workers. Shared edits and final evidence checks belong to the coordinator.

## Installation

This repository contains a supported catalog at `.agents/plugins/marketplace.json` and the plugin at `plugins/agent-dispatcher/`. Restart the desktop host, open the Plugins Directory, select **Agent Dispatcher Local**, and install **Agent Dispatcher**. Start a fresh chat and select the installed plugin through the host picker. Use the identifier shown by the host; no literal @ identifier is assumed here.

This machine's CLI help also supports these commands from this directory:

```powershell
codex plugin marketplace add .
codex plugin list --marketplace agent-dispatcher-local --available --json
codex plugin add agent-dispatcher@agent-dispatcher-local --json
```

Installation changes the host cache and plugin settings. Source changes require a supported refresh/reinstall and fresh discovery checks. See [verification evidence](docs/verification.md) for actual results, including limitations.

## Use

After selecting the plugin, describe the task, desired output, and constraints. Example:

> Assess whether separate frontend and backend changes would benefit from workers. Propose exact ownership and deliverables for my approval before starting them.

A simple rewrite should be completed directly. A useful parallel task should produce a proposal and wait. A general request for agents is not approval of an unseen proposal.

Plugin discovery and agent capability are separate: this skill does not add tools, capacity, or permissions. If agent tools are unavailable, it works sequentially and reports that limitation. Efficiency is unmeasured; parallel execution may use more tokens.

## Development and GitHub

Run `python scripts/validate.py` with Python 3.12 or newer. No dependencies are needed for these structural checks. GitHub Actions runs the same checks on pushes and pull requests. They verify package metadata and resource resolution, not model behavior or the complete upstream JSON schema.

See [behavioral scenarios](docs/validation.md), [project plan](PLAN.md), and [contribution guidance](CONTRIBUTING.md). The root `task-brief.md` is copied into the skill's references so the installed package is self-contained; validation checks that the copies match.

The distributable plugin folder is `plugins/agent-dispatcher/`. No remote repository has been created or published. No open-source license has been selected; choose one before representing the project as open-source software.

Full project acceptance also requires approved live worker scenarios and comparable sequential/delegated measurements from PLAN.md. Static review alone does not establish those results.

Packaging follows [official OpenAI plugin documentation](https://developers.openai.com/plugins/build/plugins), checked October 20, 2026, and the installed Progress Checklist root-manifest example. Installation commands were verified against local CLI help.
