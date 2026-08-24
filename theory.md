# SALMON Theory

## 1. Problem

A present output may depend on:
- previous system states,
- retrieved memories,
- user inputs,
- tool results,
- policy decisions,
- model transformations,
- corrections,
- external observations.

Ordinary logs preserve sequence. SALMON attempts to preserve and reconstruct contribution.

## 2. State graph

Represent system history as a directed acyclic or partially ordered graph:

`G = (V,E)`

Nodes may represent:
- observations,
- memory items,
- intermediate states,
- transformations,
- outputs.

An edge:

`u -> v`

means `u` contributed to `v`.

## 3. Attribution weights

Each edge has contribution weight:

`w_uv in [0,1]`

For child node `v`:

`sum_u w_uv <= 1`

Residual mass represents unresolved contribution.

## 4. Recursive ancestry

For target node `z`, ancestry contribution from ancestor `a` is:

`A(a -> z) = sum_paths product_edges(w_e)`

over admissible paths from `a` to `z`.

## 5. Origin score

Candidate origin score:

`O(a,z) = A(a->z) * confidence(a) * provenance_quality(a)`

## 6. Branch ambiguity

If several ancestors contribute similarly, define normalized ancestry probabilities `p_i`.

`H_origin = -sum_i p_i log p_i`

Higher entropy means origin attribution is less concentrated.

## 7. Unresolved ancestry

If incoming attribution mass at a node is less than one:

`U_v = 1 - sum_u w_uv`

Recursive unresolved origin should be propagated forward.

## 8. State transition lineage

For transition:

`x_t = F(x_{t-1}, m_t, o_t, a_t)`

SALMON preserves separate contribution channels from:
- previous state
- memory
- observation
- action/tool result.

## 9. EFMW interpretation

The EFMW-inspired element is recursive preservation of relational ancestry through time.

The goal is not simply:
"what was nearby in context?"

It is:
"what historical structures materially contributed to this state?"

## 10. Falsifiable prediction

SALMON should add value when:
- many memories compete,
- transformations are multi-step,
- outputs depend on long histories,
- origin must be distinguished from mere recency.

If standard tracing or provenance graphs recover origins equally well, SALMON adds no justified complexity.
