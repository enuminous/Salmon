# SALMON Architecture

## Pipeline

1. State/Event Ingestor
2. Transition Linker
3. Contribution Weight Assigner
4. Provenance Validator
5. Backward Ancestry Walker
6. Path Aggregator
7. Origin Entropy Calculator
8. Residual-Origin Tracker
9. Explanation Generator

## Inputs

- historical nodes
- state transitions
- contribution edges
- provenance confidence
- target state/output

## Outputs

```json
{
  "target": "n42",
  "top_origins": [
    ["n3", 0.41],
    ["n8", 0.27]
  ],
  "origin_entropy": 0.91,
  "unresolved_origin": 0.12,
  "max_depth": 6
}
```

## Design principle

SALMON separates:
- temporal proximity
from
- causal contribution.

The most recent event is not necessarily the origin.

## Integration

ELEPHANT provides durable longitudinal history.

MAGPIE can audit provenance quality.

WOLF can use origin traces to identify which precursor source produced a later alert.

BEAVER can trace repair outcomes back to specific interventions.
