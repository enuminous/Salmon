# SALMON — EFMW Zoo #33

**State Attribution and Longitudinal Memory Origin Navigation**

SALMON is an experimental EFMW-inspired framework for tracing a present system state, output, or behavior backward through its historical dependencies to identify the states, events, memories, and transformations that actually contributed to it.

## Core question

> Where did this state come from?

SALMON is built for origin tracing, not just retrieval. It reconstructs causal ancestry across time.

## Primary outputs

- origin attribution
- causal-path confidence
- memory-source contribution
- state-transition lineage
- unresolved ancestry
- branch ambiguity
- origin depth

## Repository contents

- `theory.md`
- `architecture.md`
- `origin_model.md`
- `limitations.md`
- `salmon.py`
- `benchmark.py`
- `ablations.py`
- `test_salmon.py`
- `example.py`
- `paper.md`
- `CITATION.cff`
- `LICENSE`

## Quick start

```bash
python example.py
python benchmark.py
python ablations.py
python -m unittest test_salmon.py
```

## Zoo position

WEASEL #32 searches forward for weaknesses.

**SALMON #33 swims backward: from the current behavior toward the historical source that produced it.**
