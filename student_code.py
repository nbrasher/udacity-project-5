from math import sqrt, inf

def get_distance(x: list, y: list):
    ''' Find Euclidean distance between two
        points '''

    return sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)


def shortest_path(M, start, goal):
    # Implement Djikstra's algorithm for graph search
    distance_dict = {node: inf for node in M.intersections.keys()}
    shortest_path_to_node = dict()

    # Initialize tracking dictionaries
    distance_dict[start] = 0
    shortest_path_to_node[start] = [start]
    
    while distance_dict:
        # Pop the shortest path 
        current, distance = sorted(distance_dict.items(), key=lambda x: x[1])[0]
        distance_dict.pop(current)

        for edge in M.roads[current]:
            if edge in distance_dict:
                # Get distance and path to each edge
                new_node_distance = distance + get_distance(M.intersections[current],
                                                M.intersections[edge])
                new_node_path = shortest_path_to_node[current] + [edge]

                # If new path to the edge is shorter, update trackers
                if distance_dict[edge] > new_node_distance:
                    distance_dict[edge] = new_node_distance
                    shortest_path_to_node[edge] = new_node_path
    
    return shortest_path_to_node[goal]