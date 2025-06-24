@references(level=0):
 - .windsurfrules
 - CODE_OF_CONDUCT.md
 - MQP.md
 - ROADMAP.md
 - CROSSREF_STANDARD.md

# ðŸŒŒ EGOS - Ethical Governance Operating System

> "Building the infrastructure for transparent, ethical AI governance with blockchain-backed validation"

![License: MIT](https://opensource.org/licenses/MIT)
![Status: Active](https://github.com/enioxt/EGOS)
!Ethical Framework: ETHIK
![GitHub Stars](https://github.com/enioxt/EGOS)

## ðŸ” What is EGOS?

**EGOS** is an integrated ecosystem for ethical AI governance that combines:

- **ðŸ§  Ethics as a Service (EaaS)**: API-driven ethical evaluations through ATRiAN
- **â›“ï¸ Decentralized Validation**: Blockchain-backed ethical verification via DEV
- **ðŸ› ï¸ Modular Components**: Purpose-built subsystems working in concert
- **ðŸ“Š Transparency Tools**: Visual dashboards for oversight and accountability

EGOS stands apart from other AI ethics platforms by implementing a practical, actionable governance system rather than just theoretical guidelines.

> **Coming Soon – EGOS Dashboard MVP**  
> A public, Streamlit-powered dashboard that showcases real-time ethical metrics, prompt governance and system health. Follow the Dashboard MVP Plan and the Roadmap section for progress.

## ðŸ’Ž Core Features

| Feature | Description |
|---------|-------------|
| **ATRiAN Module** | The system's ethical core, providing intuitive guidance and context management |
| **ETHIK Framework** | Comprehensive methodology for evaluating AI systems against ethical principles |
| **TaskMaster AI** | Structured task management system aligned with MQP principles |
| **Distributed Ethical Validator (DEV)** | Decentralized consensus mechanism for ethical validation |
| **Blockchain Integration** | $ETHIK token across multiple chains enables transparent governance |
| **Ethik Engine (Central Nervous System)** | Real-time ethical intelligence & crowdsourced validation layer; rewards Nodes with Ethik Points for issue triage |
| **ATRiAN: Proactive Ethical Incident Avoidance** | ATRiAN doesn't just react to ethical breaches; it proactively identifies potential incidents and provides mechanisms for their avoidance. This unique capability is crucial for building trustworthy AI systems. Learn more about our methodology and proof of concept. |
| **Dashboard System** | Visual monitoring of ethical metrics and system performance |
| **Ethical Constitution Validator (MVP)** | Upload KOIOS PDD → ATRiAN risk report (JSON + PDF). Private beta Q3 2025 |
| **Relation Extraction Service** | FastAPI + spaCy microservice that surfaces entity relationships for dashboard graph view (v0.2) |
| **Standardized Workflows** | Pre-built processes for research, code refinement, and documentation |
| **Script Policy Enforcement Tooling** | Advanced checker (`scripts/script_management_policy.py`) enforces naming, placement, duplicate-filename, and sparse-directory rules; auto-fixes safe issues; respects archive exemptions; and produces detailed Markdown/HTML reports. Integrated in CI alongside workflows `/file_duplication_guard` and `/sparse_directory_management`. |
| **Script Header Compliance Automation** | One-click fixer (`scripts/utils/apply_policy_header.py`) plus validator (`scripts/ci_script_policy_check.py`) guarantee a single, standardized EGOS/KOIOS metadata header in every script. Integrated via the `/script_header_compliance_cycle` workflow and nightly CI. |
| **PromptVault** | System for capturing, distilling, validating, and reusing high-quality prompts. |
| **AutoCrossRef System** | Automatically creates and maintains a knowledge graph of your codebase and documentation by injecting reference links. See the full documentation for details.
| **Dataset Inventory** | Comprehensive catalogue of all ATRiAN datasets and snapshots. See [`ATRIAN/docs/DATA_INVENTORY.md`](ATRIAN/docs/DATA_INVENTORY.md) | |
| **MSAK v4.2** | Multiverse Strategic Analysis Kernel; a comprehensive prompt framework for advanced AI-augmented transdisciplinary strategic analysis. See PDD: `pdd_egos_ultra_v4.2_msak.yaml` |
| **KOIOS PDD System** | Standardized Prompt Design Document (PDD) creation, validation, and management |
| **Automated Link Hygiene** | A CI/CD workflow and associated scripts (`link_checker.py`, `fix_broken_links.py`) that automatically detect and repair broken Markdown links, ensuring documentation integrity. See the workflow file for details. |
| **Financial ROI Analytics** | Quantifies risk-mitigation savings with real incident cost data and ATRiAN score-driven ROI calculations |

## ðŸ’Ž Core Subsystems

| Subsystem | Description |
|-----------|-------------|
| **NEXUS** | Integrations Gateway & Monitoring (absorbs KARDIA, ORION) |
| **ETHIK** | ATRiAN Ethics & Governance (absorbs TRUST_WEAVER) |
| **KOIOS** | Prompt Engineering & Knowledge Orchestration (absorbs SOPHIA, TRANSLATOR) |
| **MYCELIUM** | Modular Yet Connected Event & Logic Integration Unit Manager |
| **CRONOS** | CI/CD & Time-based Automation (absorbs MASTER, SYNC) |
| **CASCADE** | AI Assistant & Strategic Analysis Kernel |
| **DEV** | Decentralized Ethical Validator |
| **ATRiAN** | Ethics as a Service & Proactive Incident Avoidance |
| **TaskMaster AI** | Structured Task Management & MQP Alignment |
| **AutoCrossRef** | Automated Knowledge Graphing & Reference Linking |
| **PromptVault** | Master Prompt Library & Reuse Platform |
| **Dashboard** | Real-time Ethical Metrics & System Performance Monitoring |

## ðŸ”„ Why Choose EGOS?

Unlike theoretical ethics frameworks or general-purpose AI platforms, EGOS provides:

- **Practical Implementation**: Ready-to-use tools and APIs for embedding ethics in AI systems
- **Decentralized Trust**: Not reliant on a single authority for ethical validation
- **Blockchain Transparency**: Every ethical evaluation is transparent and immutable
- **Modular Integration**: Components can be adopted individually based on your needs
- **Living Documentation**: Continuously evolving best practices and standards

## Stable vs Dev workflow

EGOS now follows a **single-tree, dual-maturity** layout:

| Location | Purpose | Branch |
|----------|---------|--------|
| `subsystems/<module>/src` | 📦 **Stable** production-ready code mounted by `docker-compose.yml` | `main` |
| `subsystems/<module>/dev` | 🧪 Experimental / WIP code hot-reloaded by `docker-compose.dev.yml` | feature branches |

Promotion path:
1. Develop in `dev/` on a feature branch.
2. Open PR → CI runs Ruff, Pytest (coverage ≥ 80 %), ATRiAN ethics scan.
3. Use `scripts/git_promote.ps1` to move vetted files to `src/` within the PR.
4. Merge into `main` — prod containers rebuild automatically.

Guard rails:
* Pre-commit hook prevents direct edits to `src/` outside `main`.
* CI blocks merges on lint/test/coverage failures.

---

## ðŸš€ Getting Started

### Prerequisites
- Python 3.8+
- Node.js 16+
- Git

### Quick Installation
```bash
# Clone the repository
git clone https://github.com/enioxt/EGOS

# Navigate to project directory
cd EGOS

# Install dependencies
pip install -r requirements.txt

# Launch the dashboard
streamlit run dashboard/streamlit_app.py
```

### Spin up the lightweight API & monitoring stack (Docker)
For a one-command local environment that launches all core EGOS services (APIs, Prometheus, Grafana, Postgres) in a lightweight configuration suitable for WSL2:

```powershell
# from repo root
PS C:\EGOS> docker compose -f docker-compose.light.yml up -d
```

Access points:
- Prometheus → `http://localhost:9090`
- Grafana → `http://localhost:3000` (user `admin`, pwd `egos`)
- ATRiAN EaaS API → `http://localhost:8001/docs`
- Script-Metadata API → `http://localhost:8002/docs`
- Postgres DB → `localhost:5432`

See **[docs/infra/local_dev_api_stack.md](docs/infra/local_dev_api_stack.md)** for details, troubleshooting and extending the stack.
## ðŸ’° Blockchain Integration

EGOS integrates with the BASE blockchain through the $ETHIK token:

* **BASE**: <a href="https://gmgn.ai/base/token/0x633b346b85c4877ace4d47f7aa72c2a092136cb5" target="_blank">`0x633b346b85c4877ace4d47f7aa72c2a092136cb5`</a>

## ðŸ“œ KOIOS: Prompt Design & Validation Subsystem

The **KOIOS subsystem** is central to EGOS's commitment to high-quality, consistent, and reusable AI prompts. It provides a comprehensive framework for Prompt Design Documents (PDDs), ensuring that all prompts used within the EGOS ecosystem are well-defined, validated, and managed.

**Key Capabilities of KOIOS:**

*   **Hierarchical PDD Schema (`pdd_schema.py`):**
    *   A robust Pydantic-based schema defines the structure for PDDs, ensuring all necessary metadata and prompt components are present.
    *   Supports a base schema for common fields and specialized schemas (e.g., `SpecializedHandlerPddSchema`) for advanced prompt types, selected via a `pdd_type` field in the PDD YAML.
    *   Enforces strict validation (`extra = 'forbid'`) to maintain schema integrity.
*   **Automated Validation (`validate_pdd.py`):**
    *   A dedicated script validates PDD YAML files against the defined schemas, providing clear success/failure feedback and detailed error reporting. This ensures PDDs are syntactically correct and complete before use.
*   **Standardized Prompt Engineering:**
    *   Promotes a consistent approach to designing and documenting prompts, enhancing clarity, reusability, and maintainability.
    *   Facilitates the creation of complex prompts by providing a structured template.
*   **Foundation for Advanced AI Operations:**
    *   Validated PDDs serve as reliable inputs for automated prompt execution frameworks, AI model interactions, and integration with other EGOS subsystems like ATRiAN (for ethical reviews) and Mycelium (for knowledge graphing).
*   **Workflow Integration:**
    *   PDD validation is integrated into core EGOS workflows, such as the `/distill_and_vault_prompt` process, ensuring prompts are associated with valid PDDs before being stored in the PromptVault.

The KOIOS subsystem, through its PDD standard and validation tools, underpins the quality and reliability of all prompt-driven operations within EGOS, aligning with the MQP principles of clarity, context, and precision in AI interactions. Refer to the **KOIOS Prompt Design Document (PDD) Standard** for detailed specifications.


* **Distillation & Vaulting:** Prompts are distilled from effective LLM interactions via the `/distill_and_vault_prompt` workflow and automatically stored in JSON format.
* **Versioning & Searchability:** Each entry is timestamped, schema-validated, and searchable—building a living library of best-practice prompts.
* **Reverse Prompt Engineering:** Facilitates analysis and refinement of master prompts to continuously improve AI output quality.

Current vaulted prompts include:

* `2025-06-09_103100_explicacao_python_iniciante.json`
* `ultimate_multidisciplinary_strategic_analysis_v3.json`

Refer to PromptVault when designing new kernels or tasks to avoid duplicating work and ensure consistency across the ecosystem.

## 🔗 AutoCrossRef: Your Project's Living Knowledge Graph

The **AutoCrossRef** system is a powerful internal tool that acts as the connective tissue for the entire EGOS project. It automatically scans every file, understands its location, and injects a self-referencing link. This simple action is the foundation for a powerful, interconnected knowledge management system.

### How It Works & Technologies Used

-   **Core Technology**: A robust Python script (`subsystems/AutoCrossRef/src/ref_injector.py`) handles all the logic. It's built to be lightweight and has no external dependencies beyond standard Python libraries.
-   **Process**:
    1.  A master script (`scripts/regen_references.py`) is run.
    2.  It traverses all specified project directories (like `docs/` and `subsystems/`).
    3.  For each file, it creates a secure, timestamped backup.
    4.  It intelligently finds the correct insertion point (e.g., after shebangs/encoding lines in Python files).
    5.  It injects a commented-out `@references` block containing the file's own path.
-   **CI/CD Integration**: The system is backed by a GitHub Actions workflow (`.github/workflows/autocrossref_ci.yml`) that runs comprehensive unit and integration tests on every change, guaranteeing its stability.

### Practical Benefits & Real-World Utility

-   **Instant Context & Impact Analysis**: By creating a machine-readable map of the project, we can instantly answer questions like, "If I change this file, what other parts of the system might be affected?" This dramatically reduces development risks.
-   **Accelerated Onboarding**: New developers can understand the relationships between different parts of the code and documentation much faster, navigating the project as if it were a wiki.
-   **Living Documentation**: It prevents documentation from becoming stale and isolated. Every document is an active node in the project's knowledge graph.
-   **Foundation for Advanced Tooling**: This reference system is the prerequisite for future tools, such as automated diagram generation, dependency analysis dashboards, and advanced semantic code search.

The AutoCrossRef system transforms a static collection of files into a dynamic, interconnected, and intelligent knowledge base, embodying the EGOS principle of systemic coherence. The newly implemented hierarchical reference standard enforcement ensures consistent cross-referencing across all project files, with support for different operational modes (diagnose, fix-core, full) and detailed compliance reporting.

## ðŸ“š Documentation

| Resource | Description |
|----------|-------------|
| **ðŸ“˜ Core Concepts** | Foundational principles and architecture |
| **ðŸš¶ Beginner's Guide** | Step-by-step introduction for new users |
| **ðŸ’» API Reference** | Complete technical documentation |
| [**ðŸ§© Integration Examples**](sdks/atrian-sdk/docs/examples.md) | Code samples for common use cases |
| [**ðŸ”­ Roadmap**](ROADMAP.md) | Future development plans and priorities |
| [**🛠️ Top Incidents Case Studies**](ATRIAN/docs/case_studies/top_incidents.md) | Diagnostics of five high-severity AI incidents & ATRiAN mitigation patterns |

## ðŸŒŸ Use Cases

- **Healthcare AI**: Ensure patient data ethics and unbiased diagnostic algorithms
- **Financial Services**: Implement fair lending practices and transparent credit scoring
- **Content Moderation**: Balance freedom of expression with harm prevention
- **Public Sector AI**: Accountable decision-making in government applications
- **Research Oversight**: Ethical guardrails for advanced AI research

## ðŸ‘¥ Community & Contribution

We welcome contributors of all skill levels! Check out our [**CONTRIBUTING.md**](CONTRIBUTING.md) guide to get started.

- **Good First Issues**: Look for issues tagged with `good-first-issue` for newcomers
- **Feature Requests**: Share ideas in GitHub Discussions
- **Bug Reports**: Submit via GitHub Issues
- **Documentation**: Help improve our guides and references

## ðŸ“ž Contact

- **Creator**: Enio Rocha
- **Email**: <eniodind@protonmail.com>
- **Telegram**: <https://t.me/ethikin>

## ðŸ“„ License

This project is licensed under the MIT License - see the [LICENSE](tools/nats-server/nats-server-v2.10.11-windows-amd64/LICENSE) file for details.

---

<p align="center">âœ§à¼ºâ€à¼»âˆž EGOS âˆžà¼ºâ€à¼»âœ§</p>