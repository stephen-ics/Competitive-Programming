nm = input.split(" ")
n = int(nm[0])
m = int(nm[1])
mstEdges = [None]*m
visited = [False]*n


def addEdges(nodeIndex):
    visited[nodeIndex]