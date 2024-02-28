class Graph(object):

    def __init__(self, vertices, is_directed) -> None:
        self.vertices = vertices
        self.adj_list = {}
        self.is_directed = is_directed
        for vertex in self.vertices:
            self.adj_list[vertex] = []

    def printGraph(self):
        for vertex in self.vertices:
            print(vertex, "->", self.adj_list[vertex])

    def add_edge(self, v1, v2):
        self.adj_list[v1].append(v2)
        if not self.is_directed:
            self.adj_list[v2].append(v1)

    def find_outdegree(self, vertex):
        return len(self.adj_list[vertex])

    def find_indegree(self, vertex):
        deg = 0
        for edge in self.adj_list:
            if vertex in self.adj_list[edge]:
                deg += 1
        return deg
    

def depth_first_search(graph, source):
    stack = [source]
    seen = [source]
    while stack:
        vertex = stack.pop()
        print(vertex)
        for conn_node in graph[vertex]:
            if conn_node not in seen:
                stack.append(conn_node)
                seen.append(conn_node)

def depth_first_search_recur(graph, source, seen):
    if source in seen:
        return 
    print(source)
    seen.append(source)
    for node in graph[source]:
        depth_first_search_recur(graph, node, seen)

def breadth_first_search(graph, source):
    queue = [source]
    seen = [source]
    while queue:
        vertex = queue.pop(0)
        print(vertex)
        for conn_node in graph[vertex]:
            if conn_node not in seen:
                queue.append(conn_node)
                seen.append(conn_node)


vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
edge_list = [('a', 'b'), ('b', 'c'), ('c', 'a'), ('d', 'e'), ('e', 'f'), ('f', 'g'), ('g', 'd'), ('h', 'i'), ('i', 'j'), ('j', 'h')]
is_directed = False
graph = Graph(vertices=vertices, is_directed=is_directed)
for edge in edge_list:
    v1, v2 = edge
    graph.add_edge(v1, v2)

graph.printGraph()
# depth_first_search(graph=graph.adj_list, source=input("Enter the source to do dfs: "))
# breadth_first_search(graph=graph.adj_list, source=input("Enter the source to do bfs: "))
# depth_first_search_recur(graph=graph.adj_list, source=input("Enter the source to do dfs: "), seen=[])

def number_of_connected_components(graph):
    visited = set()
    count = 0
    for vertex in graph:
        if explore(graph, vertex, visited):
            count += 1
    
    return count

def explore(graph, vertex, visited):
    if vertex in visited:
        return False
    visited.add(vertex)
    for node in graph[vertex]:
        explore(graph, node, visited)

    return True


print(number_of_connected_components(graph.adj_list))

def longestComponent(graph):
    visited = set()
    maxSize = 0
    for node in graph:
        currSize = findSize(graph, node, visited)
        maxSize = max(maxSize, currSize)

    return maxSize

def findSize(graph, node, visited):
    if node in visited:
        return 0
    size = 1
    visited.add(node)
    for neighbour in graph[node]:
        size += findSize(graph, neighbour, visited)
    return size

print(longestComponent(graph.adj_list))