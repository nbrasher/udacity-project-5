import networkx as nx
import pickle
import math
import os

class Map:
	def __init__(self, G):
		self._graph = G
		self.intersections = nx.get_node_attributes(G, "pos")
		self.roads = [list(G[node]) for node in G.nodes()]

	def save(self, filename):
		with open(filename, 'wb') as f:
			pickle.dump(self._graph, f)


def load_map(name):
	with open(name, 'rb') as f:
		G = pickle.load(f)
	return Map(G)


def dist(x: list, y: list):
    # Find Euclidean distance between two points
    return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)


def reconstruct_path(came_from: dict, current: int):
    # Reconstruct shortest path derived by A*
    path = [current]
    while current in came_from.keys():
        current = came_from[current]
        path = [current] + path
    
    return path


def shortest_path(M, start, goal):
    ''' A* graph search

        Parameters
        ______
        M (Map): Current graph
        start (int): Node for start of search
        goal (int): Node for search goal

        Returns
        ______
        List(int): List of nodes in shortest path from start to goal
    '''

    # G- and F-score for path from start to each node
    g = {node: math.inf for node in M.intersections.keys()}
    f = {node: math.inf for node in M.intersections.keys()}
    g[start] = 0
    f[start] = dist(M.intersections[start], M.intersections[goal])

    # Queue of nodes to be searched, sorted by distance estimate
    search = {start: f[start]}

    # Dict for tracking shortest path to each node from start node
    came_from = {}

    while search.keys():
        # Pop the shortest path 
        current, f_est = sorted(search.items(), key=lambda x: x[1])[0]
        search.pop(current)

        if current == goal:
            return reconstruct_path(came_from, current)
        
        for neighbor in M.roads[current]:
            # Get new distance to neighbor
            g_est = g[current] + dist(M.intersections[current],
                                      M.intersections[neighbor])

            # If new distance is shorter, update paths
            if g_est < g[neighbor]:
                came_from[neighbor] = current
                g[neighbor] = g_est
                f[neighbor] = g_est + dist(M.intersections[neighbor],
                                           M.intersections[goal])
                if neighbor not in search.keys():
                    search[neighbor] = f[neighbor]

    # If no path found and no nodes left to search, return None for search failure
    return