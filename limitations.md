# Limitations and Falsification

SALMON is an experimental attribution framework.

## Limitations

- Contribution weights may be estimated poorly.
- Correlation can masquerade as causation.
- Missing logs create unresolved ancestry.
- Cyclic systems complicate ancestry interpretation.
- Attribution may depend heavily on instrumentation.
- Long paths can dilute weight.

## Falsification criteria

SALMON's central hypothesis is weakened if:

1. Simple provenance graphs perform equivalently.
2. Contribution weighting does not improve origin recovery.
3. Recursive path aggregation adds no value.
4. Origin entropy does not correlate with ambiguity.
5. Results fail on held-out synthetic histories with known ground truth.
6. Attribution is unstable under small perturbations.

## Claim boundary

SALMON estimates origin under an explicit contribution graph. It does not independently prove causation.
