class Graph(object):

    def __init__(self, edges, n) -> None:
        self.adj_list = {}
        for i in range(n):
            self.adj_list[i] = []

        for edge in edges:
            node, neighbour = edge
            self.adj_list[node].append(neighbour)
            self.adj_list[neighbour].append(node)


n = int(input())
e = int(input())
edges = []
for i in range(e):
    edges.append(list(map(int, input().split())))


def dfs(src, graph, visited, res):
    visited.add(src)
    res.append(src)
    for nei in graph[src]:
        if nei not in visited:
            dfs(nei, graph, visited, res)

    return res

g = Graph(edges, n)
for key, value in g.adj_list.items():
    print(key, "->", *value)
print("Depth first search:", dfs(0, g.adj_list, set(), []))