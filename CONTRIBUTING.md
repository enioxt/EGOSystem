@references(level=0):
 - .windsurfrules
 - CODE_OF_CONDUCT.md
 - MQP.md
 - ROADMAP.md
 - CROSSREF_STANDARD.md

# Contributing to EGOS

First off, thank you for considering contributing to EGOS. It's people like you that make EGOS such a great project.

Following these guidelines helps to communicate that you respect the time of the developers managing and developing this open source project. In return, they should reciprocate that respect in addressing your issue or assessing patches and features.

## Code of Conduct

This project and everyone participating in it is governed by the EGOS Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior.

## How Can I Contribute?

Unsure where to begin contributing to EGOS? You can start by looking through these beginner-friendly issues: `good first issue`

## Development Setup

To ensure code quality and consistency, we use `pre-commit` hooks. These hooks run automatically before each commit to check for issues like syntax errors, formatting, and more.

### Keeping Your Workspace Fresh

Run `/activate_egos` at the start of every coding session (or anytime you suspect your local tree is stale).  It will:
1. Hard-reset to `main`
2. Install hooks
3. Run the Quality Pipeline (task sanitizer + README checks)
4. Refresh docs/cross-refs
5. Notify other agents that you’re up-to-date.

### Setting Up Pre-Commit

1.  **Install `pre-commit`:**

    ```bash
    pip install pre-commit
    ```

2.  **Install the Git hooks:**

    Navigate to the root of the EGOS repository and run:

    ```bash
    pre-commit install
    ```

That's it! Now, before you commit any changes, the hooks defined in `.pre-commit-config.yaml` will run on the files you've staged.

## Submitting Changes

Please send a GitHub Pull Request with a clear list of what you've done. When you send a pull request, we will imagine that you have considered these things.
