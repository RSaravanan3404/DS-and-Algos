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

    def add_weighted_edge(self, v1, v2, weight):
        self.adj_list[v1].append([v2, weight])
        if not self.is_directed:
            self.adj_list[v2].append([v1, weight])


    def find_outdegree(self, vertex):
        return len(self.adj_list[vertex])

    def find_indegree(self, vertex):
        deg = 0
        for edge in self.adj_list:
            if vertex in self.adj_list[edge]:
                deg += 1
        return deg