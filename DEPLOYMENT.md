# Deployment and release guide

Agent Dispatcher is a skill-based plugin. There is no web service, server deployment, API key, or database to configure. Deployment means installing the plugin into a supported host; publishing to GitHub distributes its source and optional release archive.

## 1. Check the source

Prerequisites: Git, Python 3.12 or newer for development checks, and a supported Codex host for installation. The plugin itself requires no Python runtime. Actual delegation additionally requires host-provided subagent tools and capacity.

From the repository root:

```powershell
python scripts/validate.py
python scripts/package.py
git diff --check
git status --short
```

Both Python commands must report success. Packaging writes `dist/agent-dispatcher-0.2.0.zip` for the current version. The archive has an explicit file allowlist and is checked against the source. It is ignored by Git; attach it separately to a GitHub release. Run these checks again after any changes.

## 2. Install locally

Use a host version whose `codex plugin --help` supports marketplace registration and installation. From the repository root:

```powershell
codex plugin marketplace add .
codex plugin list --marketplace agent-dispatcher-local --available --json
codex plugin add agent-dispatcher@agent-dispatcher-local --json
codex plugin list --marketplace agent-dispatcher-local --json
```

The final listing should report the plugin as installed and enabled. These commands write host settings and the plugin cache; use normal host approval prompts when required.

Alternatively, in the supported desktop Plugins Directory select **Agent Dispatcher Local** and install **Agent Dispatcher**. If the source is missing, register the repository with the first command above and restart the desktop app.

Restart or refresh the desktop host, open a fresh chat, and select Agent Dispatcher in the plugin picker. The picker identifier is host-defined. Installation does not add subagent tools.

## 3. Smoke-test the installation

1. Ask for a one-sentence rewrite. Expect a concrete multi-agent plan and explicit solo option, with no execution until you choose. Choose solo and verify a direct rewrite with no workers.
2. Ask for substantial independent research, such as comparing coffee shops, dinner restaurants, and evening activities in a town, with verified hours and prices. Expect concrete research roles and a solo alternative without having to request separate subtasks. The dispatcher must present a plan even if it recommends solo.
3. Before confirmation, verify that no workers start. Approve the concrete proposal only when you want those workers to run.
4. After approval, verify actual worker activity through the host, no more than three active workers, and a final integrated answer with evidence and limitations.

Do not mark steps 2–4 as passed merely because the skill text describes them. Record actual outcomes in `docs/verification.md`. Worker tests require the same concrete-proposal confirmation as normal use.

## 4. Publish the repository on GitHub

Review `git status` and the files being uploaded for secrets and local configuration. This repository has no open-source license grant; select a license before advertising it as open source. Public visibility alone does not supply a license.

Create an empty repository in your GitHub account using GitHub's **New repository** page. Avoid initializing a second README or unrelated history. Commit reviewed changes locally, then use the exact remote URL GitHub provides:

```powershell
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

`YOUR_GITHUB_REPOSITORY_URL` is a placeholder; replace it before running. If `origin` already exists, inspect it with `git remote -v` and use the intended remote rather than adding another. Do not force-push to resolve unrelated remote history.

Check the **Actions** tab: **Validate plugin** must pass on both Windows and Linux. Local checks do not prove that the remote workflow has run.

## 5. Publish an early release

In GitHub, choose **Releases → Draft a new release**. For the initial version:

- Create tag `v0.2.0` targeting the reviewed `main` commit.
- Title it `Agent Dispatcher 0.2.0 — early release`.
- Copy the corresponding changelog entry and state that live worker orchestration and efficiency measurements remain unverified until those tests have been recorded.
- Attach `dist/agent-dispatcher-0.2.0.zip` from the validated source.
- Select **Set as a pre-release**, then publish when ready.

GitHub publication does not submit or approve a listing in the universal plugin directory. The ZIP is a distribution artifact; do not assume a host supports installing it directly.

## 6. Install from a GitHub clone

Clone the published repository using the URL shown by GitHub, change into that clone, and follow step 2. The marketplace path is relative and does not rely on the original developer's filesystem.

For a Git-backed marketplace, the documented registration command is also supported:

```powershell
codex plugin marketplace add OWNER/REPOSITORY --ref v0.2.0
```

Replace `OWNER/REPOSITORY` and the tag with actual published values. Then list and install using the marketplace and plugin names in step 2. This remote installation path has not been tested before the repository exists on GitHub.

## 7. Update and roll back

For a new release, update the version in `plugins/agent-dispatcher/plugin.json`, update the changelog and versioned examples, run validation and packaging, and repeat smoke tests. Reinstall the new version using the host's supported plugin flow and verify its version with `codex plugin list`. Restart the app and use a fresh chat. Cached installations may not reflect source edits immediately.

To roll back, preserve any local work, use a separate clone of the previous reviewed release tag, register that clone, and reinstall through step 2. If the host reports a marketplace name conflict, resolve the existing registration through its supported marketplace controls before adding the rollback clone. Confirm the installed version and repeat the smoke test. Do not delete host caches by hand or overwrite uncommitted source changes.
