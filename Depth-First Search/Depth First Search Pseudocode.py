# Uses 
    # Finding connect components
    # Compute a graph's minimum spanning tree
    # Detect and find cycles in a graph
    # Check if a graph is bipartite
    # Find strongly connected components
    # Topologically sort the nodes of a graph
    # Find bridges and articulation points
    # Find augmenting paths in a flow network
    # Generate mazes

# n = number of nodes in the graph
# g = adjacency list representing graph
# count = 0
# components = [empty int array] # size n
# visited = [false, ..., false] # size n

# function findComponents():
    # for i in range(i = 0; i < n; i++):
        # if !visited[i]:
            # count++ 
            # dfs(i)
        # return (count, components)   

# function dfs(at):
    # if visited[at]: return
    # visited[at] = true
    # components[at] = count
    # for (next:)

    # neighbours = graph[at]
    # for next in g[at]:
        # if !visited[i]
            # dfs(next)

# start_node = 0
# dfs(start_node)

# Start a DFS at every node (except if it has already neem visited) 
# Mark all reachable nodes as being part of the same component

