@references(level=0):
 - .windsurfrules
 - CODE_OF_CONDUCT.md
 - MQP.md
 - ROADMAP.md
 - CROSSREF_STANDARD.md

# Test Synchronization File

This file was created to test the automatic synchronization between the private EGOS repository and the public EGOSystem repository.

## Synchronization Process

1. This file is created in the `docs-public` directory of the private repository.
2. When committed and pushed to the private repository, it should trigger:
   - The local post-commit hook (immediate sync)
   - The GitHub Action workflow (cloud-based sync)
3. Both mechanisms should copy this file to the public repository.

## Timestamp

This test was performed on: 2025-06-24 10:01
