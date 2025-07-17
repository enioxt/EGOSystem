# The Listening Spiral: A Protocol for Mediated Consensus

**@cross-references:**
- **Parent:** [[docs/intro/what_is_egos.md]]
- **Children:** [[docs/concepts/spiral_types.md]], [[docs/use_cases/UC_01_youtube_moderation.md]]
- **Related:** [[docs/concepts/coruja_moderation.md]], [[docs/tokenomics/ethik_point_matrix.md]], [[docs/design/listening_spiral_ui.md]]

**The Listening Spiral is the central interaction protocol of the EGOS ecosystem.** It is a structured, real-time, and gamified process designed to facilitate collective intelligence and achieve verifiable consensus on complex or contentious issues. It transforms chaotic disputes into transparent, evidence-based resolutions.

At its core, the Spiral is a state machine that guides participants through distinct phases of signaling, deliberation, and decision-making, all mediated by the Coruja AI and incentivized by the ETHIK Engine.

## The State Machine & Phases

The Listening Spiral progresses through a defined lifecycle, ensuring that every issue is handled with procedural fairness. The state transitions are managed by the system and can be influenced by participant actions or AI intervention.

```mermaid
stateDiagram-v2
    [*] --> Draft

    state Draft {
        description: An issue is identified and a spiral is initiated by a user.
    }
    Draft --> Magnetized: on_publish

    state Magnetized {
        description: The spiral is public. Notifications are sent to relevant experts or stakeholders to attract participation.
    }
    Magnetized --> Open: on_quorum_reached

    state Open {
        description: Quorum is met. The floor is open for evidence submission, debate, and voting.
    }
    Open --> Semi_Closed: on_consensus_achieved
    Open --> Stalled: on_timeout_or_impasse

    state Semi_Closed {
        description: A preliminary consensus is reached. A cool-down period allows for final objections before locking.
    }
    Semi_Closed --> Archived: on_finalization

    state Stalled {
        description: The discussion has stalled. Coruja AI may intervene with polls or summaries to restart dialogue.
    }
    Stalled --> Open: on_new_evidence
    Stalled --> Archived: on_admin_closure

    state Archived {
        description: The spiral is resolved and closed. The outcome and evidence are immutably stored in KOIOS.
    }
    Archived --> [*]
```

### Phases Explained:

1.  **Draft:** A user (the *Signaler*) creates a new Spiral, defining the initial problem, providing preliminary evidence, and suggesting relevant participants.
2.  **Magnetized:** The Spiral is published. The system uses topic tags and user reputation data to notify and attract relevant participants (*Responders* and *Validators*). The goal is to reach a participation quorum.
3.  **Open:** With enough participants, the Spiral opens for full deliberation. This is the core phase where evidence is presented, arguments are debated, and votes are cast. Coruja AI actively monitors the health of the discussion.
4.  **Semi-Closed:** A consensus has been detected (e.g., a supermajority vote is stable for a set period). This phase acts as a final review window before the decision is made permanent.
5.  **Stalled:** If discussion ceases or becomes circular without resolution, the Spiral enters a stalled state. This triggers automated interventions from Coruja to help break the impasse.
6.  **Archived:** The Spiral concludes. Its outcome is finalized, ETHIK points are distributed, and a permanent, auditable record of the entire process is logged to the KOIOS knowledge base, often minted as an NFT certificate.

## Real-Time Interaction via WebSockets

The Listening Spiral UI is a real-time application. All state changes and participant actions are broadcast via WebSockets to connected clients. This ensures all users have a synchronized view of the debate as it unfolds.

**Example WebSocket Event Schema:**
```json
{
  "event": "spiral.vote.cast",
  "payload": {
    "spiralId": "sp_abc123",
    "userId": "usr_xyz789",
    "vote": "agree",
    "evidenceHash": "0x...",
    "timestamp": "2025-07-06T23:30:00Z"
  }
}
```

Key events include:
- `spiral.signal.created`
- `spiral.participant.joined`
- `spiral.evidence.added`
- `spiral.comment.posted`
- `spiral.vote.cast`
- `spiral.state.changed`
- `coruja.intervention.triggered`
