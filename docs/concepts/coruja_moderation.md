# Coruja AI: Moderation & Governance in the Listening Spiral

**@cross-references:**
- **Parent:** [[docs/concepts/listening_spiral.md]]
- **Related:** [[docs/synthesis/notebooklm_sources/EthikEngine_README.md]], [[docs/standards/rules/rules_ethik.md]]

**Coruja is the AI-powered moderation and facilitation layer of the Listening Spiral.** Named after the Portuguese word for "owl," it serves as a wise, impartial observer that intervenes only when necessary to ensure discussions remain healthy, productive, and fair. Its primary directive is to guide spirals toward a clear resolution without interfering with the substance of the debate.

## Core Functions

Coruja's responsibilities can be broken down into three main categories:

1.  **Health Monitoring:** Continuously analyzes the discussion for negative patterns.
2.  **Facilitation & Intervention:** Proactively suggests actions to overcome impasse or improve clarity.
3.  **Summarization & Synthesis:** Distills complex conversations into digestible summaries for participants and for the final archival record.

## Automated Heuristics & Triggers

Coruja operates on a set of predefined heuristics to detect when an intervention might be necessary. These triggers are designed to be conservative to avoid over-moderation.

| Heuristic | Threshold / Condition | Coruja's Action |
| :--- | :--- | :--- |
| **Toxicity** | Sentiment analysis score > 0.85 (on a 0-1 scale) in multiple consecutive messages. | Issues a private warning to the user and a public, anonymized reminder about community guidelines. |
| **Overposting** | A single user posts > 5 messages in a 10-minute window without responses. | Suggests the user consolidate their thoughts and allow others to respond. |
| **Impasse Detection** | No new evidence or arguments for a set period (e.g., 12 hours) despite ongoing low-level discussion. | Triggers a **Dynamic Poll** on the last key points of disagreement to gauge current consensus. |
| **Circular Argument** | Key phrases or arguments are repeated by opposing sides without new evidence. | Generates a real-time summary of the arguments so far (`"Here's what we've established..."`) to help refocus the debate. |
| **Information Overload** | More than 20 pieces of evidence have been submitted. | Automatically groups evidence by theme or argument and presents it in a collapsible tree view. |

## Intervention Types

When a trigger condition is met, Coruja can deploy several types of interventions:

*   **Dynamic Polls:** If a debate is stuck on a specific point, Coruja can create a temporary, non-binding poll to quickly measure the group's current leaning. This can help identify areas of agreement and disagreement.
*   **Argument Summaries:** Coruja can be prompted by users (or automatically trigger) to provide a neutral summary of the debate so far, helping newcomers get up to speed or refocusing the conversation.
*   **Evidence Requests:** If an assertion is made without backing, Coruja can prompt the user to provide supporting evidence, reinforcing the evidence-based nature of the spiral.
*   **Escalation to Human Moderators:** In the rare case of persistent rule-breaking or complex ethical situations beyond its programming, Coruja can flag the spiral for review by a human moderator from the EGOS governance team.

## Governance & Human Oversight

Coruja is a tool, not the ultimate authority. All its actions are logged transparently within the spiral's record. Participants can vote to override a specific Coruja intervention if they feel it is unhelpful or biased, ensuring human-centric control is always maintained.
