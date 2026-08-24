from benchmark import build

if __name__ == "__main__":
    tracer = build()
    full = tracer.trace("out")
    print("full:", full)

    # Ablation: ignore contribution weights by equalizing every edge.
    for e in tracer.edges:
        e.weight = 0.5
    tracer.parents.clear()
    from collections import defaultdict
    tracer.parents = defaultdict(list)
    for e in tracer.edges:
        tracer.parents[e.target].append(e)
    print("equal-weight ablation:", tracer.trace("out"))
