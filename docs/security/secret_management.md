# EGOS Secret Management Guide

> **Status:** Draft v1.0 – 2025-07-08  
> **Audience:** All contributors  
> **Applies to:** _Entire EGOS repository_

## 1  Golden Rules

1. **No real secrets in git history**. Ever.  
2. **Exactly one** template file – `.env.example` – lives in the repo; every value is a placeholder.  
3. All runtime secrets are pulled from **provider dashboards**, **GitHub Secrets**, or **local untracked files** (e.g. `.env.local`).
4. Rotate production credentials at least **every 90 days**; development credentials every 180 days.

---

## 2  Where Secrets Live

| Environment | Storage | Retrieval |
|-------------|---------|-----------|
| GitHub Actions | **GitHub Secrets** (or _Environments_ for prod vs staging segmentation) | `${{ secrets.MY_KEY }}` |
| Render / Vercel / Fly | Provider → **Environment Variables** | Set via dashboard or `render.yaml` |
| Local development | Untracked file **`.env.local`** or **`direnv`** | Autoload via `direnv` or `dotenv` in tooling |
| Docker run (local) | `--env-file .env.runtime` (untracked) | `docker run --env-file …` |
| Documentation samples | `.env.example` (placeholders only) | Copy → rename → fill locally |

### Directory rules
```
.egos secrets layout
├── .env.example          # template – committed
├── .env.local            # developer-specific – NOT committed
└── subsystems/.../.env   # NEVER committed – ignore by pattern
```

---

## 3  Developer Workflow

```bash
# one-time
cp .env.example .env.local   # fill with real values

# make changes, commit as usual – hooks will run
pre-commit run ‑-all-files   # optional manual check
```

The **pre-commit hook** runs `gitleaks --redact` to block potential leaks before they reach the repository.

---

## 4  Automated Protection Layers

1. **.gitignore**
   ```gitignore
   # Secrets
   *.env
   *.env.*
   !*.env.example
   *.secret*
   ```
2. **Pre-commit** (`.pre-commit-config.yaml`)
   ```yaml
   - repo: https://github.com/zricethezav/gitleaks
     rev: v8.18.2
     hooks:
       - id: gitleaks
         args: ["--redact"]
         stages: [pre-commit, pre-push]
   ```
3. **CI gate** – _secret_scan.yml_ (disabled by default, enable when minutes allow):
   *Runs `gitleaks` on every PR and weekly on `main`.*
4. **GitHub Secret Scanning** – enable **Push Protection** in repo settings (Security → Code security and analysis).

---

## 5  Key Rotation Procedure

1. In provider dashboard, **generate new credentials**.  
2. **Update GitHub Secrets** and/or cloud env-vars.  
3. Redeploy services if necessary.  
4. Delete the old secret from provider.

Document the rotation in `ADRS_Log.md` (RULE-LOG_STD-001) with timestamp and reason.

---

## 6  Incident Response (Secret Leak)

1. **Revoke / rotate** the exposed credential immediately.  
2. Purge the secret from git history using `git filter-repo` or BFG.  
3. Force-push corrected history.  
4. Open a post-mortem; update this guide if needed.

---

_Last updated 2025-07-08 by Cascade AI_
