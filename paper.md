# SALMON: State Attribution and Longitudinal Memory Origin Navigation

## Abstract

SALMON is an experimental framework for tracing present outputs and system states backward through historical contribution graphs. It combines weighted ancestry, provenance quality, recursive path aggregation, and unresolved-origin accounting to distinguish causal contribution from mere temporal proximity.

## 1. Motivation

A system may know what happened recently without knowing what actually produced its present state.

SALMON addresses this distinction.

## 2. Model

History is represented as:

`G=(V,E)`

with weighted contribution edges.

For ancestor `a` and target `z`:

`A(a->z)=sum_paths product(w_e)`

Origin score:

`O(a,z)=A(a->z)*confidence(a)*provenance_quality(a)`

## 3. Metrics

- origin attribution accuracy
- top-k origin recall
- path confidence
- origin entropy
- unresolved ancestry
- maximum origin depth
- attribution stability

## 4. Baselines

- recency ranking
- flat provenance lookup
- nearest-memory retrieval
- graph reachability
- unweighted ancestry
- influence-function-like attribution where applicable

## 5. Ablations

- remove weights
- remove provenance quality
- remove recursive path aggregation
- truncate ancestry depth
- collapse all memory nodes
- discard unresolved mass

## 6. Falsification

If simple provenance tracing matches SALMON on known-origin held-out tasks, the additional weighting and recursive structure are not justified.

## 7. Claim boundary

SALMON estimates origin only with respect to the instrumented contribution graph. It is not independent proof of causality.
