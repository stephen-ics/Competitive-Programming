# Prim's Minimum Spanning Tree Algorithm

# Prim's is a greedy MST algorithm that works well on dense graphs
    # However, when finding the minimum spanning forest on a disconnected graph, Prim's will have trouble doing so
    # The lazy version of Prim's has a runtime of O(E*log(E))
    # The eager version has a better runtime of O(E*log(V))

# Lazy Prim's MST Overview
    # Maintain a min Priority Queue (PQ) that sorts edges based on min edge cost
    # This will be used to determine the next node to visit and the edge used to get there
    # Start the algorithm on any node s
    # Mark s as visited and iterate over all edges of s
    # Adding them to the PQ
    # While PQ is not empty
        # MST has not been formed
        # Dequeue the next cheapest edge from the PQ
        # If the dequeue edge is outdated, then skip it and poll again
        # Otherwise, mark the current node as visited and add the selected edge to the MST
    # Iterate over the new current node's edges and add all it's edges to the PQ
    # Do not add edges that point to already visited nodes
    # Although the graph represents an undirected edfge, the internal adjacency is typically two directed edges

# Lazy Prim's Pseudo Code
    # n = Number of nodes in the graph
    # pq = PQ data structure, stores edge objects consisting of {start node, end node, edge cost} tuples. The PQ Sorts edges based on min edge cost
    # g = Graph representing an adjacency list of weighted edges, each adjacency list of weighted edges
        # Note: Edges in g for especially dense graphs prefer using adjacency matrix instead of an adjacency list
    # visited = [false, ..., false] size n

    # def addEdges(nodeIndex):
        # visited[nodeIndex] = true
        # edges = g[nodeIndex]
        # for (edge : edges):
            # if !visited[edge.to]:
                #pq.enqueue(edge)

    # def lazyPrims(s = 0):
        # m = n - 1 # number of edges in MST
        # edgeCount, mstCost = 0, 0 --> Track edge count and mst cost
        # mstEdges = [null, ..., null] # size m
        # addEdges(s)
        
        # while (!pq.isEmpty() and edgeCount != m):
            # edge = pq.dequeue()
            # nodeIndex = edge.to

            # if visited[nodeIndex]:
                # continue
            # mstEdges[edgeCount += 1] = edge
            # mstCost += edge.cost

            # addEdges(nodeIndex)
        
        # if edgeCount != m:
            # return (null, null) # No MST exists!
        # return (mstCost, mstEdges)





