# Agent Dispatcher

A skill-based plugin that always proposes a concrete multi-agent plan and offers an explicit solo alternative for each new task. Version 0.2.0 uses one coordinator and at most three active workers, limited by user preference and host capacity.

**Status: early release.** Version 0.1.0 installation, picker discovery, and simple invocation were confirmed. Version 0.2.0 changes task routing to always propose a plan; fresh-chat behavioral checks must be repeated. Live delegated execution and efficiency comparisons remain untested. See [verification evidence](docs/verification.md).

Before executing a new task, it presents concrete roles, ownership, deliverables, dependencies, and speed/usage tradeoffs, then waits for you to choose the proposed plan, revisions, or solo execution. Small tasks still receive a plan, with an honest explanation when solo would be more efficient. An explicit solo choice in your request is honored without asking again. Workers cannot create workers. Shared edits and final evidence checks belong to the coordinator.

## Install through npm

Published on npm as [@lucastabit13/agent-dispatcher](https://www.npmjs.com/package/@lucastabit13/agent-dispatcher), version 0.2.0. Registry installation and packaged marketplace files have been verified.

Requires Node.js 20 or newer and a Codex CLI with plugin support on PATH.

```sh
npm install -g @lucastabit13/agent-dispatcher
agent-dispatcher install
```

The explicit install command registers the marketplace inside the npm package, then installs the plugin. Restart the desktop app and open a fresh chat to use it. On Windows the installer uses codex.exe; set CODEX_BIN to the full Codex executable path if it is not on PATH.

To update, run the same two commands again. Keep the npm package installed while using its local marketplace. Run `agent-dispatcher path` to print the marketplace root for manual registration. npm installation alone does not activate the plugin.

To remove the plugin, run `codex plugin remove agent-dispatcher@agent-dispatcher-local`, then `codex plugin marketplace remove agent-dispatcher-local` and `npm uninstall -g @lucastabit13/agent-dispatcher`.


## Installation

See [DEPLOYMENT.md](DEPLOYMENT.md) for complete installation, GitHub publishing, prerelease, update, and rollback steps.

This repository contains a supported catalog at `.agents/plugins/marketplace.json` and the plugin at `plugins/agent-dispatcher/`. Restart the desktop host, open the Plugins Directory, select **Agent Dispatcher Local**, and install **Agent Dispatcher**. Start a fresh chat and select the installed plugin through the host picker. Use the identifier shown by the host; no literal @ identifier is assumed here.

This machine's CLI help also supports these commands from this directory:

```powershell
codex plugin marketplace add .
codex plugin list --marketplace agent-dispatcher-local --available --json
codex plugin add agent-dispatcher@agent-dispatcher-local --json
```

Installation changes the host cache and plugin settings. Source changes require a supported refresh/reinstall and fresh discovery checks. See [verification evidence](docs/verification.md) for actual results, including limitations.

## Use

After selecting the plugin, describe the task, desired output, and constraints naturally. You do not need to divide it into worker assignments. Example:

> Plan an evening in Richboro, Pennsylvania: compare coffee shops, dinner restaurants, and activities after dinner. Verify hours and prices, then combine the findings into an itinerary.

Even a simple rewrite should produce a concrete multi-agent plan plus a solo option and wait for your choice. You do not need to ask for separate research tasks. Routine follow-ups within an already chosen scope do not restart the choice. A general request for agents is not approval of an unseen proposal.

Plugin discovery and agent capability are separate: this skill does not add tools, capacity, or permissions. If agent tools are unavailable, it labels the proposed multi-agent plan unavailable and offers solo execution; it never pretends to launch workers. Efficiency is unmeasured; parallel execution may use more tokens.

## Development and GitHub

Run `python scripts/validate.py` with Python 3.12 or newer. No dependencies are needed for these structural checks. GitHub Actions runs the same checks on pushes and pull requests. They verify package metadata and resource resolution, not model behavior or the complete upstream JSON schema.

See [behavioral scenarios](docs/validation.md), [project plan](PLAN.md), and [contribution guidance](CONTRIBUTING.md). The root `task-brief.md` is copied into the skill's references so the installed package is self-contained; validation checks that the copies match.

The distributable plugin folder is `plugins/agent-dispatcher/`. The source repository is https://github.com/lucastabit13-dev/agent-dispatcher. No open-source license has been selected; choose one before representing the project as open-source software.

To create a validated plugin archive, run `python scripts/package.py`. It writes `dist/agent-dispatcher-0.2.0.zip`, containing the manifest and self-contained skill at the archive root. The archive is a distribution artifact, not a claim that every host supports ZIP installation. Install through the supported marketplace flow above.

Before publishing to GitHub, run validation and packaging, review the staged files, create your GitHub repository, and upload this repository. The included marketplace uses relative paths, so it can be registered from another clone. Mark the first GitHub release as a prerelease and include [CHANGELOG.md](CHANGELOG.md) and the verification limitations in its description. Do not claim universal plugin directory approval or measured speed savings.

Full project acceptance also requires approved live worker scenarios and comparable sequential/delegated measurements from PLAN.md. Static review alone does not establish those results.

Packaging follows [official OpenAI plugin documentation](https://developers.openai.com/plugins/build/plugins), checked October 20, 2026, and the installed Progress Checklist root-manifest example. Installation commands were verified against local CLI help.
