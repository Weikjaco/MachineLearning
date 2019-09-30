import math as m

def get_euclidean_dist(classify_me, neighbor):
    """Get distance of each neighbor compared to the node we are trying to classify"""
    distance_squared = 0
    for i in range(len(classify_me)-1):
        distance_squared += (classify_me[i]-neighbor[i])**2

    distance = m.sqrt(distance_squared)
    return distance

def get_nearest_neighbor(k, nodes):
    """Return the k nearest neighbors given k and list of nodes"""
    nearest_neighbors = []
    # Sort list of nodes, least distance to greatest distance
    sorted_nodes = sorted(nodes, key=lambda distance: distance[2])
    # Get nearest neighbors
    for i in range(k):
        nearest_neighbors.append(sorted_nodes[k])

def classify():
    """Classify based on k classes"""