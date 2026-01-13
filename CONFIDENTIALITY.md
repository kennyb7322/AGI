# Confidentiality & Handling Guidance

**Classification:** CONFIDENTIAL (template)

This document is a template. Adjust it to match your organization's policy.

## If this repository is PRIVATE

Treat all contents as confidential:

- Do not copy/paste source code into public issue trackers.
- Do not share with third parties without a signed NDA.
- Store secrets outside the repo (use a secrets manager).
- Redact logs/traces before sharing.

## If this repository is PUBLIC

Confidentiality markings provide no meaningful protection. If you intend to keep
code confidential, make the repository private and restrict access.

## Recommended technical controls

- Enable branch protection + mandatory reviews.
- Use secret scanning and pre-commit checks.
- Use CI to run tests and linting.
- Maintain an audit log for deployments.

