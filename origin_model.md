# Origin Model

## Node schema

```json
{
  "id": "n17",
  "time": 17,
  "kind": "memory",
  "content": "Pressure sensor was recalibrated",
  "confidence": 0.92,
  "provenance_quality": 0.95
}
```

## Edge schema

```json
{
  "source": "n17",
  "target": "n24",
  "weight": 0.35,
  "relation": "contributed_to"
}
```

## Target attribution

For target `t`, SALMON recursively accumulates weighted ancestry.

## Root origins

A root is a node with no incoming attribution edges.

The framework should distinguish:
- strong root attribution
- distributed ancestry
- unknown/residual origin

## Ambiguity

A target may have several plausible origins.

SALMON reports this explicitly rather than forcing a single answer.

## Navigation

Backward navigation follows the highest contribution paths first, while preserving alternative branches.
