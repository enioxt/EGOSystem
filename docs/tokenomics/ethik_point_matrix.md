# ETHIK Point Matrix

**@cross-references:**
- **Parent:** [[docs/concepts/listening_spiral.md]]
- **Related:** [[docs/concepts/coruja_moderation.md]], [[docs/whitepaper/03_tokenomics.md]]

This matrix defines the standard ETHIK point rewards for participant actions within the EGOS Listening Spiral ecosystem. Values comply with **RULE-METRICS-01**; each point value is justified by maintaining a target Gini coefficient < 0.35 across active monthly users (see Appendix A for simulation details).

| Action Category | Action | Base Points | Bonus Modifiers | Daily Cap |
| :--- | :--- | :---: | :--- | :---: |
| **Signaling** | Create a new spiral that reaches quorum | 10 | +5 if quorum < 1 h | 50 |
|  | False-positive (spiral fails) | −5 | n/a | n/a |
| **Validation** | Cast a decisive vote in consensus majority | 8 | +2 if first validator; +2 if evidence attached | 80 |
|  | Vote in minority that proves correct after new evidence | 12 | +5 insight bonus | 80 |
| **Evidence** | Attach verifiable evidence (hash logged in KOIOS) | 6 | +4 if external source cross-referenced | 60 |
| **Mediation** | Propose compromise adopted as final outcome | 20 | +10 if reduces spiral duration > 30 % | 40 |
| **Expert Advice** | Provide domain-expert opinion (validated by credentials) | 15 | +5 if citation links to peer-reviewed source | 60 |
| **AI Oversight** | Override unwarranted Coruja intervention (community vote) | 5 | n/a | 25 |
| **Governance Participation** | Vote in Governance Spiral | 4 | +1 per 5 % stake weight (max +10) | 40 |
| **Education & Onboarding** | Complete Spiral tutorial | 20 | One-time | n/a |

## Decay & Anti-Gaming Mechanisms

1. **Linear Decay:** 1 % of a user’s total ETHIK score decays per 30 days of inactivity to encourage continuous engagement.
2. **Duplicate Evidence Penalty:** Submitting evidence already on-chain yields zero points; spam is auto-flagged for potential deduction.
3. **Sybil Guard:** Points from new accounts (<30 d) have a weighting factor of 0.5 until account maturity.

## Metric Justification (Rule-Metrics-01)

We target:
- **Engagement Ratio ≥ 0.42** (active participants / total registered)  
- **Average Time-to-Resolution reduction of 15 % YoY**

Monte-Carlo simulations (n = 10 000) project Gini ≈ 0.31 with the above matrix, satisfying equity goals. See `notebooks/ethik_point_sim.ipynb` for full methodology.

## Appendix A – Simulation Summary (abridged)

| Parameter | Value |
| :--- | :--- |
| Iterations | 10 000 |
| Avg Spirals / user / month | 4.2 |
| Evidence attach rate | 0.57 |
| Validation majority rate | 0.81 |
| Resulting Gini | 0.308 |

