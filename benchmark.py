from salmon import Node, Edge, SalmonTracer

def build():
    nodes = {
        "o1": Node("o1",1,0.95,0.95,"observation"),
        "o2": Node("o2",2,0.90,0.90,"observation"),
        "m1": Node("m1",3,0.85,0.90,"memory"),
        "s1": Node("s1",4),
        "s2": Node("s2",5),
        "out": Node("out",6)
    }
    edges = [
        Edge("o1","s1",0.7),
        Edge("m1","s1",0.2),
        Edge("o2","s2",0.6),
        Edge("s1","s2",0.3),
        Edge("s2","out",0.8),
        Edge("s1","out",0.1)
    ]
    return SalmonTracer(nodes, edges)

if __name__ == "__main__":
    tracer = build()
    print(tracer.trace("out"))
