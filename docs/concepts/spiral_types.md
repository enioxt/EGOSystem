# Listening Spiral: Type Library

**@cross-references:**
- **Parent:** [[docs/concepts/listening_spiral.md]]
- **Related:** [[docs/use_cases/UC_05_contract_analysis.md]]

While the core mechanics of the Listening Spiral are consistent, the protocol is not one-size-fits-all. Spirals are configured into different **types**, each optimized for a specific purpose, timescale, and level of rigor. This library defines the standard Spiral types within the EGOS ecosystem.

## Summary of Spiral Types

| Type | Description | Typical Timescale | Quorum Rules | Default Output |
| :--- | :--- | :--- | :--- | :--- |
| **Alert** | Rapidly validate or reject urgent, simple claims (e.g., harmful content). | Minutes to Hours | Low (e.g., 3-5 validators) | Boolean Flag (Valid/Invalid) |
| **Validation** | General-purpose dispute resolution for transactions or service claims. | Hours to Days | Medium (e.g., 5-10 validators) | Resolution Certificate (NFT) |
| **Contract** | Clause-by-clause analysis and negotiation of a legal document. | Days | Medium, role-based | Annotated & Signed Document |
| **Investigation** | In-depth, long-term inquiry into complex claims (e.g., supply chain audit). | Days to Weeks | High, evidence-gated | Detailed Final Report |
| **Governance** | Formal community voting on proposals, rules, or budget allocations. | Weeks | High, stake-weighted | Binding Mandate |

---

## Detailed Type Specifications

### 1. Alert Spiral
-   **Purpose:** Designed for speed and immediate response. The goal is to quickly triage a high volume of simple, binary issues.
-   **Use Case:** Flagging a YouTube video for hate speech; reporting a bug in an application.
-   **Rules:**
    -   Evidence is usually limited to the initial report.
    -   Discussion is minimal.
    -   Coruja AI intervention is high to ensure rapid closure.
    -   ETHIK rewards are small but are bonused for speed and accuracy.

### 2. Validation Spiral
-   **Purpose:** The standard spiral for most peer-to-peer disputes, such as e-commerce or service disagreements.
-   **Use Case:** A buyer claims an item arrived damaged; a client disputes a freelancer's delivered work.
-   **Rules:**
    -   Requires submission of evidence from both parties (e.g., photos, chat logs).
    -   Quorum requires a mix of general community members and subject-matter experts if applicable.
    -   The outcome is often tied to an action (e.g., releasing funds from escrow).

### 3. Contract Spiral
-   **Purpose:** To collaboratively review, discuss, and agree upon the terms of a document.
-   **Use Case:** Reviewing a rental agreement; negotiating a freelance work contract.
-   **Rules:**
    -   The spiral is attached to a specific document.
    -   Participants can raise sub-spirals on individual clauses.
    -   Voting is often role-based (e.g., only Tenant and Landlord can vote on final terms, but a Legal Expert can advise).

### 4. Investigation Spiral
-   **Purpose:** For complex, long-running inquiries that require significant evidence gathering and analysis.
-   **Use Case:** Verifying a company's "100% organic" claim; auditing the ethical sourcing of a product.
-   **Rules:**
    -   Participation is often gated by reputation or proven expertise.
    -   The spiral may have multiple phases of evidence collection and review.
    -   The final output is a comprehensive report, co-authored by the participants.

### 5. Governance Spiral
-   **Purpose:** The most formal and high-stakes spiral type, used for making binding decisions on the EGOS platform itself.
-   **Use Case:** Voting on a change to the ETHIK point system; electing a new member to a governance council.
-   **Rules:**
    -   Strict, predefined timelines for discussion and voting.
    -   Voting power may be weighted by ETHIK score or other forms of stake (token-holding).
    -   Outcomes are automatically executed by the system where possible.
