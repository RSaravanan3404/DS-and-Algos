from graphClass import Graph


vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
n = len(vertices)
edge_list = [('a', 'b'), ('b', 'c'), ('c', 'a'), ('d', 'e'), ('e', 'f'), ('f', 'g'), ('g', 'd'), ('h', 'i'), ('i', 'j'), ('j', 'h')]
is_directed = True
graph = Graph(vertices=vertices, is_directed=is_directed)
for edge in edge_list:
    v1, v2 = edge
    graph.add_edge(v1, v2)


def bellmanford(graph: Graph, src, dst, n: int) -> int:

    costs = [ float('inf') ] * n
    q = [ src ]
    while q:
        