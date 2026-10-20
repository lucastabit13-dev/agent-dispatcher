# Contributing

Read AGENTS.md and PLAN.md before changing the workflow. Keep the plugin self-contained and skill-based. Do not introduce new runtime dependencies without a demonstrated need.

Run `python scripts/validate.py` before submitting a change. For instruction changes, run the relevant scenarios in `docs/validation.md` and record observed behavior separately from expected behavior. Workers require explicit confirmation of their concrete roles, including during testing.

Do not commit credentials, local host configuration, caches, or generated archives. Public publication and licensing are maintainer decisions; this initial source has no open-source license grant.
