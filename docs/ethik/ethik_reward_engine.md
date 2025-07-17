---
title: ETHIK Reward Engine
description: Fair-cap algorithm, proportional distribution formulas, and integration points for the ETHIK Reward Engine
updated: 2025-07-07
status: draft
@references(level=0):
 - /docs/standards/rules/rules_doc_std.md
 - /docs/standards/rules/rules_metrics.md
 - /docs/ethik/ethik_engine_overview.md
 - /subsystems/ethik_engine/docs/README.md
---

# ETHIK Reward Engine

## Overview

The ETHIK Reward Engine is the core algorithmic component of the ETHIK Engine that calculates and distributes rewards based on contributions, market benchmarks, and ethical principles. It implements the FairCap algorithm and ensures proportional, transparent distribution of value across the EGOS ecosystem.

## Core Algorithms

### FairCap Algorithm

The FairCap algorithm ensures that rewards are proportional to contribution value while maintaining ethical caps and preventing excessive concentration of rewards.

#### Mathematical Model

For a given contribution `C` with market value `V`:

1. Calculate the base reward: `R_base = V * contribution_factor`
2. Apply the cap: `R_capped = min(R_base, V * cap_percentage)`
3. Calculate overflow: `O = R_base - R_capped` (if positive)
4. Allocate overflow to Genki-Dama Fund

```python
def calculate_reward(contribution, market_value, contribution_factor, cap_percentage):
    """
    Calculate the reward for a contribution using the FairCap algorithm.
    
    Parameters:
    - contribution: Contribution metrics (quality, impact, etc.)
    - market_value: Benchmark market value for this type of contribution
    - contribution_factor: Factor based on contribution quality (0.0-1.0)
    - cap_percentage: Maximum percentage of market value to reward (0.0-1.0)
    
    Returns:
    - reward: The calculated reward amount
    - overflow: Amount redirected to Genki-Dama Fund
    """
    base_reward = market_value * contribution_factor
    capped_reward = min(base_reward, market_value * cap_percentage)
    overflow = max(0, base_reward - capped_reward)
    
    return capped_reward, overflow
```

#### Contribution Factor Calculation

The contribution factor is calculated based on multiple dimensions:

```python
def calculate_contribution_factor(quality, impact, complexity, collaboration):
    """
    Calculate the contribution factor based on multiple dimensions.
    
    Parameters:
    - quality: Quality score (0.0-1.0)
    - impact: Impact score (0.0-1.0)
    - complexity: Complexity score (0.0-1.0)
    - collaboration: Collaboration score (0.0-1.0)
    
    Returns:
    - factor: Combined contribution factor (0.0-1.0)
    """
    # Base weights (can be adjusted based on contribution type)
    weights = {
        'quality': 0.4,
        'impact': 0.3,
        'complexity': 0.2,
        'collaboration': 0.1
    }
    
    factor = (
        quality * weights['quality'] +
        impact * weights['impact'] +
        complexity * weights['complexity'] +
        collaboration * weights['collaboration']
    )
    
    return factor
```

### Proportional Distribution Algorithm

For collaborative contributions involving multiple participants, the reward is distributed proportionally:

```python
def distribute_reward(total_reward, contributions):
    """
    Distribute a reward among multiple contributors.
    
    Parameters:
    - total_reward: Total reward amount to distribute
    - contributions: Dictionary mapping contributor IDs to contribution scores
    
    Returns:
    - distributions: Dictionary mapping contributor IDs to reward amounts
    """
    total_contribution = sum(contributions.values())
    distributions = {}
    
    for contributor_id, contribution in contributions.items():
        if total_contribution > 0:
            proportion = contribution / total_contribution
            distributions[contributor_id] = total_reward * proportion
        else:
            distributions[contributor_id] = 0
    
    return distributions
```

## System Architecture

```
┌────────────────┐     ┌────────────────┐     ┌────────────────┐
│                │     │                │     │                │
│  Contribution  │────▶│  FairCap       │────▶│  Distribution  │
│  Evaluation    │     │  Algorithm     │     │  Module        │
│                │     │                │     │                │
└────────────────┘     └────────────────┘     └────────────────┘
        ▲                      │                      │
        │                      ▼                      ▼
┌────────────────┐     ┌────────────────┐     ┌────────────────┐
│                │     │                │     │                │
│  Benchmarking  │     │  Genki-Dama    │     │  Reward        │
│  Module        │     │  Fund          │     │  Ledger        │
│                │     │                │     │                │
└────────────────┘     └────────────────┘     └────────────────┘
```

### Key Components

1. **Contribution Evaluation**: Assesses the quality, impact, complexity, and collaborative nature of contributions
2. **FairCap Algorithm**: Implements the core reward calculation logic
3. **Distribution Module**: Handles the allocation of rewards to contributors
4. **Benchmarking Module**: Provides market value references
5. **Genki-Dama Fund**: Receives overflow allocations
6. **Reward Ledger**: Maintains a transparent record of all reward calculations and distributions

## Integration Points

### TaskMaster Integration

The Reward Engine integrates with TaskMaster to calculate rewards for completed tasks:

```python
# Example integration with TaskMaster
@router.post("/api/v1/tasks/{task_id}/complete")
async def complete_task(
    task_id: str,
    completion_data: TaskCompletionData,
    reward_engine: RewardEngine = Depends(get_reward_engine)
):
    # Validate task completion
    task = await task_service.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    # Get benchmark for task type
    benchmark = await benchmark_service.get_benchmark(task.category, task.subcategory)
    
    # Calculate contribution factors
    contribution_factor = reward_engine.calculate_contribution_factor(
        quality=completion_data.quality_score,
        impact=completion_data.impact_score,
        complexity=task.complexity,
        collaboration=completion_data.collaboration_score
    )
    
    # Calculate reward
    reward, overflow = reward_engine.calculate_reward(
        contribution=completion_data,
        market_value=benchmark.market_value.amount,
        contribution_factor=contribution_factor,
        cap_percentage=benchmark.ethik.cap_percentage
    )
    
    # Distribute reward if collaborative
    if len(completion_data.contributors) > 1:
        distributions = reward_engine.distribute_reward(
            total_reward=reward,
            contributions=completion_data.contribution_scores
        )
        await reward_service.distribute_rewards(distributions)
    else:
        await reward_service.issue_reward(task.assignee, reward)
    
    # Allocate overflow to Genki-Dama Fund
    if overflow > 0:
        await genki_dama_service.allocate(overflow, source=f"task:{task_id}")
    
    # Update task status
    await task_service.update_task_status(task_id, TaskStatus.COMPLETED)
    
    return {
        "task_id": task_id,
        "reward": reward,
        "overflow": overflow,
        "distributions": distributions if len(completion_data.contributors) > 1 else None
    }
```

### AgentCore Integration

The Reward Engine integrates with AgentCore for automated ethical evaluations:

```python
# Example integration with AgentCore
@router.post("/api/v1/contributions/evaluate")
async def evaluate_contribution(
    contribution_data: ContributionData,
    agent_core: AgentCore = Depends(get_agent_core),
    reward_engine: RewardEngine = Depends(get_reward_engine)
):
    # Request ethical evaluation from AgentCore
    evaluation = await agent_core.evaluate_contribution(
        content=contribution_data.content,
        context=contribution_data.context,
        contribution_type=contribution_data.type
    )
    
    # Apply ethical adjustments to contribution factors
    adjusted_factors = reward_engine.apply_ethical_adjustments(
        contribution_data.factors,
        evaluation.ethical_score,
        evaluation.concerns
    )
    
    return {
        "contribution_id": contribution_data.id,
        "ethical_score": evaluation.ethical_score,
        "adjusted_factors": adjusted_factors,
        "concerns": evaluation.concerns if evaluation.concerns else None
    }
```

## API Endpoints

```
# Calculate reward for a contribution
POST /api/v1/ethik/rewards/calculate
Content-Type: application/json
{
  "contribution_id": "c123",
  "market_value": 250.00,
  "contribution_factors": {
    "quality": 0.85,
    "impact": 0.75,
    "complexity": 0.60,
    "collaboration": 0.90
  },
  "benchmark_id": "dev-code-review"
}

# Distribute reward among contributors
POST /api/v1/ethik/rewards/distribute
Content-Type: application/json
{
  "reward_id": "r456",
  "total_amount": 175.00,
  "contributions": {
    "user1": 0.6,
    "user2": 0.3,
    "user3": 0.1
  }
}

# Get reward history for a user
GET /api/v1/ethik/rewards/history/{user_id}

# Get reward details
GET /api/v1/ethik/rewards/{reward_id}
```

## Implementation

### Core Classes

```python
class RewardEngine:
    def __init__(
        self,
        benchmark_service: BenchmarkService,
        genki_dama_service: GenkiDamaService,
        reward_ledger: RewardLedger
    ):
        self.benchmark_service = benchmark_service
        self.genki_dama_service = genki_dama_service
        self.reward_ledger = reward_ledger
    
    def calculate_contribution_factor(
        self,
        quality: float,
        impact: float,
        complexity: float,
        collaboration: float
    ) -> float:
        # Implementation as shown in the algorithm section
        pass
    
    def calculate_reward(
        self,
        contribution: ContributionData,
        market_value: float,
        contribution_factor: float,
        cap_percentage: float
    ) -> Tuple[float, float]:
        # Implementation as shown in the algorithm section
        pass
    
    def distribute_reward(
        self,
        total_reward: float,
        contributions: Dict[str, float]
    ) -> Dict[str, float]:
        # Implementation as shown in the algorithm section
        pass
    
    def apply_ethical_adjustments(
        self,
        factors: Dict[str, float],
        ethical_score: float,
        concerns: List[str]
    ) -> Dict[str, float]:
        # Apply adjustments based on ethical evaluation
        pass
    
    async def process_reward(
        self,
        contribution_id: str,
        benchmark_id: str
    ) -> RewardResult:
        # End-to-end reward processing
        pass
```

### Database Schema

```sql
-- Reward records
CREATE TABLE ethik_rewards (
    id UUID PRIMARY KEY,
    contribution_id UUID NOT NULL,
    benchmark_id UUID NOT NULL,
    market_value DECIMAL(18,6) NOT NULL,
    contribution_factor DECIMAL(5,4) NOT NULL,
    cap_percentage DECIMAL(5,4) NOT NULL,
    reward_amount DECIMAL(18,6) NOT NULL,
    overflow_amount DECIMAL(18,6) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    FOREIGN KEY (contribution_id) REFERENCES contributions(id),
    FOREIGN KEY (benchmark_id) REFERENCES ethik_benchmarks(id)
);

-- Reward distributions
CREATE TABLE ethik_distributions (
    id UUID PRIMARY KEY,
    reward_id UUID NOT NULL,
    recipient_id UUID NOT NULL,
    amount DECIMAL(18,6) NOT NULL,
    proportion DECIMAL(5,4) NOT NULL,
    distributed_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    FOREIGN KEY (reward_id) REFERENCES ethik_rewards(id),
    FOREIGN KEY (recipient_id) REFERENCES users(id)
);

-- Overflow allocations
CREATE TABLE ethik_overflow_allocations (
    id UUID PRIMARY KEY,
    reward_id UUID NOT NULL,
    amount DECIMAL(18,6) NOT NULL,
    source VARCHAR(255) NOT NULL,
    allocated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    FOREIGN KEY (reward_id) REFERENCES ethik_rewards(id)
);
```

## Configuration Options

The Reward Engine supports various configuration options to adjust its behavior:

```yaml
# Example configuration
reward_engine:
  # Default cap percentages by contribution type
  default_caps:
    development: 0.75
    research: 0.80
    governance: 0.85
    support: 0.70
  
  # Contribution factor weights
  factor_weights:
    quality: 0.40
    impact: 0.30
    complexity: 0.20
    collaboration: 0.10
  
  # Ethical adjustment settings
  ethical_adjustments:
    enabled: true
    impact_factor: 0.25
    minimum_score: 0.60
  
  # Distribution settings
  distribution:
    minimum_proportion: 0.05
    rounding_precision: 2
```

## Implementation Plan

### Phase 1: Core Algorithm

1. Implement FairCap algorithm
2. Create contribution factor calculation
3. Develop basic distribution logic
4. Set up reward ledger

### Phase 2: Integration

1. Integrate with Benchmarking Module
2. Connect to Genki-Dama Fund
3. Implement TaskMaster integration
4. Create API endpoints

### Phase 3: Advanced Features

1. Implement ethical adjustments
2. Add collaborative distribution features
3. Create visualization components
4. Develop analytics and reporting

## Security & Ethics Considerations

- All reward calculations must be transparent and auditable
- Distribution algorithms must be fair and resistant to gaming
- Ethical concerns must be factored into reward calculations
- Privacy must be maintained for sensitive contribution data
- System must be resilient against manipulation attempts

## References

- [ETHIK Engine Overview](/docs/ethik/ethik_engine_overview.md)
- [ETHIK Benchmarking Module](/docs/ethik/ethik_benchmarking.md)
- [ETHIK Genki-Dama Fund](/docs/ethik/ethik_genki_dama.md)