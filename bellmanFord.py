from graph import *

INFINITE = 99999


def relax(graph, parents, distance, u, v, w):
    status = False
    if distance[v] > distance[u] + w:
        distance[v] = distance[u] + w
        parents[v] = u
        status = True
    return status


def initialize(graph, parents, distance, s):
    vertices = graph.get_vertices()
    for i in range(0, graph.size):
        parents[vertices[i]] = None
        distance[vertices[i]] = INFINITE
    parents[s] = s
    distance[s] = 0


def bellman_ford(graph, s):
    """
    computes shortest path from s to all vertex in the graph
    :param graph: the graph
    :param s: source vertex
    :return: list containing boolean if the problem is defined (non negative cycles), and the dictonary of parents and distances if boolean is true
    """
    edges = graph.get_edges()
    parents = {}
    distance = {}
    initialize(graph, parents, distance, s)
    for i in range(1, graph.size - 1):
        for edge in edges:
            relax(graph, parents, distance, edge[0], edge[1], edge[2])
    for edge in edges:
        if relax(graph, parents, distance, edge[0], edge[1], edge[2]):
            return [False, [], []]
    return [True, parents, distance]
