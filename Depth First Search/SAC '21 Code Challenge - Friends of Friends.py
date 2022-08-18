from operator import truediv


nq = input().split(" ")
n = int(nq[0])
q = int(nq[1])

connections = {}

for i in range(n):
    connections[i+1] = [False]*n

def dfs(position, visited):
    if visited[position] == False:
        visited[position] = True
        for i in connections[connections]:
            if i == True:
                dfs(i, visited)

for i in range(q):
    command = [int(i) for i in input().split(" ")]
    visited = []
    
    for i in range(n):
        visited[i+1] = False

    if command[0] == 1:
        friend1 = command[1]
        friend2 = command[2]
        connections[friend1][friend2-1] = True
        connections[friend2][friend1-1] = True
    
    else:
        dfs(i, visited)
