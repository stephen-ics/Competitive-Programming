nq = input().split(" ")
n = int(nq[0])
q = int(nq[1])

output = []

connections = {}

for i in range(n):
    connections[i+1] = [False]*n

def dfs(position, visited):
    global count

    if visited[position] == False:
        visited[position] = True
        for i in range(len(connections[position])):
            if connections[position][i] == True:
                if visited[i+1] == False:
                    count += 1
                    dfs(i+1, visited)

for i in range(q):
    command = [int(i) for i in input().split(" ")]
    visited = {}
    count = 1
    
    for i in range(n):
        visited[i+1] = False

    if command[0] == 1:
        friend1 = command[1]
        friend2 = command[2]
        connections[friend1][friend2-1] = True
        connections[friend2][friend1-1] = True
    
    else:
        dfs(command[1], visited)
        output.append(count)

for i in output:
    print(i)
