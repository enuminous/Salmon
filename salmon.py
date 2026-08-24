from dataclasses import dataclass
from typing import Dict, List, Tuple
from collections import defaultdict
import math

@dataclass
class Node:
    id: str
    time: int
    confidence: float = 1.0
    provenance_quality: float = 1.0
    kind: str = "state"

@dataclass
class Edge:
    source: str
    target: str
    weight: float

class SalmonTracer:
    def __init__(self, nodes: Dict[str, Node], edges: List[Edge]):
        self.nodes = nodes
        self.edges = edges
        self.parents = defaultdict(list)
        for e in edges:
            self.parents[e.target].append(e)

    def trace(self, target: str):
        contrib = defaultdict(float)
        unresolved = 0.0
        max_depth = 0

        stack = [(target, 1.0, 0)]
        visited_guard = 0

        while stack:
            node_id, weight, depth = stack.pop()
            visited_guard += 1
            if visited_guard > 100000:
                raise RuntimeError("Possible cyclic or excessively large ancestry graph")
            max_depth = max(max_depth, depth)

            incoming = self.parents.get(node_id, [])
            if not incoming:
                n = self.nodes[node_id]
                contrib[node_id] += weight * n.confidence * n.provenance_quality
                continue

            total = sum(max(0.0, min(1.0, e.weight)) for e in incoming)
            unresolved += weight * max(0.0, 1.0-total)

            for e in incoming:
                ew = max(0.0, min(1.0, e.weight))
                if ew > 0:
                    stack.append((e.source, weight*ew, depth+1))

        total_c = sum(contrib.values())
        probs = []
        if total_c > 0:
            probs = [v/total_c for v in contrib.values() if v > 0]
        entropy = -sum(p*math.log(p) for p in probs) if probs else 0.0

        ranked = sorted(contrib.items(), key=lambda x: x[1], reverse=True)

        return {
            "target": target,
            "origins": ranked,
            "origin_entropy": entropy,
            "unresolved_origin": unresolved,
            "max_depth": max_depth
        }
