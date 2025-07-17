# GitHub Actions Optimization Plan

**Date:** 2025-07-08  
**Status:** Implemented  
**Author:** Cascade AI  

## Overview

This document outlines the optimization strategy for GitHub Actions workflows in the EGOS repository to address the spending limit issue. The plan drastically reduces the number of active workflows while maintaining essential functionality through manual alternatives.

## Problem Statement

The EGOS repository has reached its GitHub Actions spending limit due to the large number of workflows (68 total) and their frequent execution. This has resulted in workflow failures, including the critical X daily post workflow.

## Solution

### 1. Workflow Reduction Strategy

We've implemented a three-part strategy:

1. **Workflow Controller**: A new workflow (`workflow_controller.yml`) that manages which workflows are enabled/disabled based on a configuration file
2. **Configuration File**: A central configuration (`workflow_config.yml`) that defines which workflows are essential
3. **Manual Alternatives**: Scripts for executing critical tasks locally when GitHub Actions is unavailable

### 2. Essential Workflows (Kept Active)

| Workflow | Purpose | Optimization |
|----------|---------|-------------|
| X Daily Post | Posts daily updates to X.com | Removed schedule/push triggers, manual only |
| Health Report | System health monitoring | Removed schedule trigger, manual only |
| API Deployment Checks | Validates API deployments | Manual trigger only |
| ATRiAN Ethics Gate | Security checks for PRs | Reduced scope |

### 3. Disabled Workflows

All other workflows (60+) have been disabled to conserve GitHub Actions minutes. These include:
- CI/CD pipelines
- Automated tests
- Documentation checks
- Deployment workflows
- Code quality checks

## Manual Alternatives

### Daily X.com Posting

A new script has been created to manually post daily updates to X.com:

```bash
# Run the script
./scripts/manual_daily_post.sh
```

This script:
1. Finds today's daily update file
2. Extracts a summary from the highlights or social media snippet
3. Prompts for X API credentials if not set in the environment
4. Posts to X.com using the same logic as the GitHub Action

### Required Environment Variables

To run the manual posting script, you'll need:

```bash
export X_API_KEY='your_api_key'
export X_API_SECRET='your_api_secret'
export X_ACCESS_TOKEN='your_access_token'
export X_ACCESS_SECRET='your_access_secret'
```

## Re-enabling Workflows

When GitHub Actions minutes are available again, you can re-enable workflows using:

```bash
# Check which workflows would be enabled/disabled
gh workflow run workflow_controller --field mode=check

# Apply the changes
gh workflow run workflow_controller --field mode=apply
```

## API Deployment Strategy

Based on the current API deployment approach (using Render.com), we recommend:

1. Continue using the production-first deployment approach for APIs
2. Maintain the existing AgentCore API deployment on Render.com
3. Use manual deployment scripts for new API versions
4. Keep the minimal test API pattern for validating environments before full deployment

## References

- [EGOS API Testing Standard](../standards/rules_api_testing.md)
- [AgentCore API Unification Process](../../.windsurf/workflows/agentcore_api_unification.md)
- [Render Deployment Workflow](../../.windsurf/workflows/render_api_deployment.md)

## Cross-References

- @references(level=0):
  - MQP.md
  - .windsurfrules
  - .github/workflows/workflow_config.yml

- @references(level=1):
  - scripts/manual_daily_post.sh
  - scripts/utils/post_to_x.py
