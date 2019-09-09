from bellmanFord import *

my_graph = Graph()

my_graph.add_undirected_edge('s', 't', 6)
my_graph.add_undirected_edge('s', 'y', 7)
my_graph.add_undirected_edge('t', 'y', 8)
my_graph.add_undirected_edge('z', 's', 2)
my_graph.add_undirected_edge('t', 'x', 5)
my_graph.add_undirected_edge('x', 't', -2)
my_graph.add_undirected_edge('y', 'z', 9)
my_graph.add_undirected_edge('z', 'x', 7)
my_graph.add_undirected_edge('t', 'z', -4)
my_graph.add_undirected_edge('y', 'x', -3)

print(bellman_ford(my_graph, 's'))

# example 2, undirected graph
my_graph2 = Graph()
my_graph2.add_undirected_edge('s', 't', 10)
my_graph2.add_undirected_edge('s', 'y', 5)
my_graph2.add_undirected_edge('t', 'x', 1)
my_graph2.add_undirected_edge('y', 'z', 2)
my_graph2.add_undirected_edge('t', 'y', 2)
my_graph2.add_undirected_edge('y', 't', 3)
my_graph2.add_undirected_edge('x', 'z', 4)
my_graph2.add_undirected_edge('z', 'x', 6)
my_graph2.add_undirected_edge('y', 'x', 9)
my_graph2.add_undirected_edge('z', 's', 7)

print(bellman_ford(my_graph2, 's'))

# example 3, negative cycle

my_graph3 = Graph()
my_graph3.add_undirected_edge('s', 't', 6)
my_graph3.add_undirected_edge('s', 'y', 7)
my_graph3.add_undirected_edge('t', 'y', 8)
my_graph3.add_undirected_edge('z', 's', 2)
my_graph3.add_undirected_edge('t', 'x', 5)
my_graph3.add_undirected_edge('x', 't', -22)
my_graph3.add_undirected_edge('y', 'z', 9)
my_graph3.add_undirected_edge('z', 'x', 7)
my_graph3.add_undirected_edge('t', 'z', -4)
my_graph3.add_undirected_edge('y', 'x', -3)

print(bellman_ford(my_graph3, 's'))

bell