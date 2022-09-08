# Requirements
    # Visited List
    # Unvisited List
    # Start
    # Distances of all other vertices from each vertex they are connected to

# GREEDY VERSION (FIND SHORTEST DISTANCE OF ALL VERTICES FROM START)

# Let distance of start vertex from start vertex = 0
# Let distance of all other vertices from start = infinity

# While vertices remain unvisited
    # Visit the unvisited vertex with the smallest known distnce from the start vertex
    # For the current vertex, calculate distance of each neighbour from start vertex
    # If the calculated distance is less than the known distance, update the shortest distance
    # Add the current vertex to the list of visited vertices
#Until only one unvisited vertice with no neighbour, then add that vertice to visited array

# NON-GREEDY VERSION (FIND SHORTEST PATH FROM START TO END)

# Let distance of start vertex from start vertex = 0
# Let distance of all other vertices from start = infinity

# While vertices remain unvisited
    # Visit unvisited vertex with smallest known distance from start vertex (call this 'current vertex')
    # For each unvisited neighbour of the current vertex
        # Calculate the distance from start vertex
        # If the calculated distance from start vertex is less that known distance
            # Update shortest distance
            # Update the previous vertex with the current vertex
        # Move on to next unvisited neighbour
        # Add the current vertex of the list of vertices
