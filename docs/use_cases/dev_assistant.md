# Use case: Dev assistant

## Goal

Help developers by:

- reading repository files
- proposing changes
- generating diffs/patches
- running tests (optional tool)

## Safety posture

- DO NOT auto-push or merge code.
- Require explicit human review.
- Restrict filesystem writes to `workspace/data/` or a temp directory.

## Pattern

1. Read relevant files (file_read)
2. Plan change
3. Generate patch text
4. (Optional) run unit tests in CI, not locally

