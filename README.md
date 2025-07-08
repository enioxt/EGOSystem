# EGOS: The Ethical & Generative Operating System

<p align="center">
  <img src="https://raw.githubusercontent.com/EnioGPT/EGOS/main/docs/assets/logo/egos_logo_splash_text.png" alt="EGOS Logo" width="600"/>
</p>

<p align="center">
    <em>A new paradigm for creating intelligent systems that are powerful, purposeful, and profoundly aligned with human values.</em>
</p>

---

## Table of Contents

1. [Welcome](#welcome-to-egos)
2. [Vision & Whitepaper](#vision--whitepaper)
3. [Quick Start](#quick-start)
4. [Repository Map](#repository-map)
5. [Core Subsystems](#core-subsystems)
6. [Key Workflows](#key-workflows)
7. [Contributing](#contributing)
8. [License](#license)

---

## Welcome to EGOS

EGOS is an advanced, open-source framework for building, deploying, and managing sophisticated AI agents and services. It is designed from the ground up with a core philosophy that integrates ethics, modularity, and human-centric design into every layer of its architecture.

Our mission is to provide developers with the tools to build the next generation of AI applications while facilitating **"Ocio Criativo" (Creative Leisure)**—freeing human ingenuity from mundane tasks to focus on creativity and innovation.

## Vision & Whitepaper

To understand the philosophy, architecture and long-term roadmap, start with our central knowledge base:

- 🏛️ **Documentation Hub** — [`docs/README.md`](./docs/README.md)
- 📖 **Official Whitepaper** — [`docs/whitepaper/`](./docs/whitepaper/)

### Documentation Map *(auto-generated)*
<!-- DOC-MAP:BEGIN -->
| Section | Purpose | Landing page |
|---------|---------|--------------|
| Quick-Start & CLI | Install, activation | `docs/getting-started/README.md` |
| Vision & Whitepaper | Strategic narrative | `docs/whitepaper/` |
| System Architecture | Diagrams, interfaces | `docs/architecture/README.md` |
| Knowledge Liberation / REEV | Schema, templates, consent | `docs/reev/README.md` |
| Standards & Rules | Coding, docs, ethics | `docs/standards/README.md` |
| Workflows | Slash-command catalog | `.windsurf/workflows/_index.md` |
| Roadmap & Tasks | Live epics & YAML | `ROADMAP.md` |
| APIs | OpenAPI & SDKs | `docs/api/README.md` |
<!-- DOC-MAP:END -->


## Quick Start (WSL, Linux & macOS)

```bash
# 1. Clone repository
$ git clone https://github.com/enioxt/EGOS.git && cd EGOS

# 2. Install the EGOS CLI wrapper (one-time)
$ ./scripts/egos install          # copies 'egos' into /usr/local/bin

# 3. First-run doctor & activation
$ egos activate full              # runs pre-flight checks then full activation

# 4. (Optional) bring up the full Docker stack
$ docker compose -f docker/stack/docker-compose.yml up -d

# 5. Browse the dashboard
$ windsurf open http://localhost:8000
```

Tips:
- On Windows use WSL 2 and run the commands **inside** the Linux shell.
- If the doctor highlights missing tools, follow its install suggestions, then rerun `egos activate full`.
- For a lighter dev path: `egos activate fast` or `egos activate lite`.


Need something lighter? Use `egos_light_backup_<date>.tar.gz` for a minimal core.

---

## Repository Map

| Path | Purpose |
|------|---------|
| `subsystems/` | Core libraries (ATRiAN, Ethik Engine, AgentCore, KOIOS, …) |
| `apps/` | User-facing applications (dashboards, demos) |
| `services/` | Independent micro-services (e.g. `plugin_registry`) |
| `docker/stack/` | Docker-Compose orchestration & container configs |
| `scripts/` | Automation, CI helpers & maintenance scripts |
| `docs/` | Standards, guides, strategy & reference docs |
| `.windsurf/workflows/` | Re-usable developer workflows |

---

## Repository Map

This repository is organized to be highly modular and discoverable. Here is a map of the most important directories. For a complete guide to our standards, see the **[Documentation Hub](./docs/README.md)**.

| Path | Purpose |
| :--- | :--- |
| **`/docs`** | **Single Source of Truth.** All project-wide documentation, standards, guides, and architectural decisions live here. |
| **`/subsystems`** | The core functional components of EGOS. Each subsystem is a self-contained module with its own logic, APIs, and tests. |
| **`/apps`** | User-facing applications, such as web UIs or dashboards, that consume services from the subsystems. |
| **`/.windsurf`** | Configuration and automation for the Windsurf AI development environment, including all slash-command workflows. |
| **`/docker`** | Contains all Dockerfiles and `docker-compose.yml` configurations for building and running the EGOS service stack. |
| **`/scripts`** | General-purpose helper and utility scripts for repository maintenance and automation. |
| **`/tasks`** | A log of all development tasks, tracked in a structured YAML format. |

> **Note for AI Agents:**
> You **must** adhere to this structure. Before creating or modifying any file, consult the **[Documentation Hub (`/docs/README.md`)](./docs/README.md)** and the relevant standards in **[`/docs/standards/rules/`](./docs/standards/rules/)** to determine the correct location and format. Do not create new top-level directories without explicit user instruction and a corresponding update to the project standards.

## Core Subsystems

| Name | Description | Path |
|------|-------------|------|
| **ATRiAN** | Ethics-as-a-Service API & validator | `subsystems/atrian/` |
| **Ethik Engine** | Real-time rule evaluation & incentive ledger | `subsystems/ethik_engine/` |
| **AgentCore** | DAG orchestrator & workflow planner | `subsystems/agentcore/` |
| **KOIOS** | Prompt design, validation & knowledge graphs | `subsystems/koios/` |
| **REEV** | Knowledge record schema & consent workflows | `docs/reev/` |


---

## Microservice APIs

| Name | Purpose | Tech | Deploy Status | URL |
|------|---------|------|---------------|-----|
| **egos-taskmaster-api** | Task CRUD & metadata | FastAPI + Supabase | Live ✅ | https://egos-taskmaster-api.onrender.com |
| **egos-eaas-api** | Ethics-as-a-Service validator | FastAPI + ATRiAN | Live ✅ | https://egos-eaas-api.onrender.com |
| **egos-script-meta-api** | Script metadata & insights | FastAPI | Live ✅ | https://egos-script-meta-api.onrender.com |
| **egos-agentcore-api** | DAG orchestrator & workflow runner | FastAPI | In Dev 🛠️ | – |
| **egos-koios-api** | PromptVault & knowledge graphs | FastAPI | Planned | – |
| **egos-metrics-api** | Quantitative metrics gateway | FastAPI | Planned | – |
| **egos-health-api** | System health reports | FastAPI | Planned | – |
| **egos-taskmaster-ui** | Web UI for task management | Next.js | Planned | – |

*Legend: Live = deployed on Render; In Dev = local skeleton exists; Planned = not yet started.*

---

## Key Workflows

These high-level workflows orchestrate all routine tasks. Use them instead of individual legacy flows.

| Slash Command | Purpose |
|---------------|---------|
| `/setup_environment` | Unified environment setup & WSL optimisation |
| `/governance_central` | Repository & standards governance hub |
| `/docs_hub_flow` | Central documentation governance & sync |
| `/crossref_cycle` | Cross-reference hygiene & nightly refresh |
| `/deploy_api_stack` | End-to-end API scaffold, launch & cloud deploy |
| `/quality_pipeline` | Comprehensive quality gates & CI tuning |
| `/task_ops` | Task management, bounty, daily summary |
| `/ai_operations` | AI-centric R&D, prompt ops, autonomous runner |
| `/agentcore_unify` | AgentCore API unification (subsystem-specific) |

Run a workflow from VS Code Windsurf palette *or* CLI:

```bash
windsurf run-workflow /add_new_component --auto
```

---

## Contributing

See **[Contributing Guide](./docs/guides/contributing.md)** for branching strategy, code standards and PR checklist.

---

## License

© 2025 EGOS Contributors — MIT License (see [`LICENSE`](./LICENSE)).



---

<p align="center">
✧༺❀༻∞ EGOS ∞༺❀༻✧
