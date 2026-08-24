from salmon import Node, Edge, SalmonTracer

nodes = {
    "sensor": Node("sensor",1,0.99,0.98,"observation"),
    "memory": Node("memory",2,0.80,0.85,"memory"),
    "state": Node("state",3),
    "decision": Node("decision",4)
}

edges = [
    Edge("sensor","state",0.75),
    Edge("memory","state",0.15),
    Edge("state","decision",0.9)
]

tracer = SalmonTracer(nodes, edges)
print(tracer.trace("decision"))
