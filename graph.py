class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.size = 0

    def get_vertices(self):
        output = []
        for vertex in self.adjacency_list:
            output.append(vertex)
        return output


    def get_neighbours(self, v):
        """
        :param v: vertex
        :return: list of neighbours with their weight. e.g.: ['v', 1]
        """
        list = []
        for neighbour in self.adjacency_list[v]:
            list.append(neighbour)
        return list

    def get_weight(self, u, v):
        for vertex in self.get_neighbours(u):
            if v == vertex[0]:
                return vertex[1]

    def print_vertices(self):
        print ("Vertices:")
        for vertex in self.adjacency_list:
            print(vertex)
        print('\n')

    def print_neighbours(self, v):
        print ("Neighbours of " + v)
        for neighbour in self.adjacency_list[v]:
            print (neighbour[0] + ", weight of edge: " + str(neighbour[1]))

    # v is not in the graph
    def add_vertex(self, v):
        self.adjacency_list[v] = []
        self.size += 1

    def add_undirected_edge(self, u, v, w):
        if u not in self.adjacency_list:
            self.add_vertex(u)
        if v not in self.adjacency_list:
            self.add_vertex(v)
        self.adjacency_list[u].append([v, w])

    def add_directed_edge(self, u, v, w):
        self.add_undirected_edge(u, v, w)
        self.add_undirected_edge(v, u, w)

    def get_edges(self):
        output = []
        for s in self.adjacency_list:
            for t in self.adjacency_list[s]:
                output.append([s, t[0], t[1]])
        return output
