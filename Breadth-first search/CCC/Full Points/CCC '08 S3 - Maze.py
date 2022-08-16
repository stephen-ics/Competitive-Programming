n = int(input())
output = []

for i in range(n):
    n = int(input())
    m = int(input())
    
    paths = []
    queue = []
    visited = {}

    for i in range(n):
        visited[i] = [-1]*m

    for i in range(n):
        path = list(input())
        paths.append(path)
    
    start = [0, 0]
    end = [n-1, m-1]

    queue.append(start)
    visited[start[0]][start[1]] = 0
    
    run = True
    notPossible = True

    if len(paths) == 1 and len(paths[0]) == 1:
        if not paths[0][0] == "*":
            output.append(1)
            run = False
            notPossible = False

    while queue and run:
        x = queue.pop(0)

        for i in ['L', 'R', 'U', 'D']:     
            if i == 'L' and 0 < x[1]:
                if visited[x[0]][x[1]-1] == -1:
                    if paths[x[0]][x[1]] == '+' or paths[x[0]][x[1]] == '-':
                        if paths[x[0]][x[1]-1] != '*':
                            visited[x[0]][x[1]-1] = visited[x[0]][x[1]] + 1
                            queue.append([x[0],x[1]-1])
                if [x[0],x[1]] == end:
                    run = False
                    notPossible = False
                    output.append(visited[x[0]][x[1]]+1)
                    break

            if i == 'R' and x[1] < m-1:
                if visited[x[0]][x[1]+1] == -1:
                    if paths[x[0]][x[1]] == '+' or paths[x[0]][x[1]] == '-':
                        if paths[x[0]][x[1]+1] != '*':
                            visited[x[0]][x[1]+1] = visited[x[0]][x[1]] + 1
                            queue.append([x[0],x[1]+1])
                if [x[0],x[1]] == end:
                    run = False
                    notPossible = False
                    output.append(visited[x[0]][x[1]]+1)
                    break
                
            if i == 'U' and 0 < x[0]:
                if visited[x[0]-1][x[1]] == -1:
                    if paths[x[0]][x[1]] == '+' or paths[x[0]][x[1]] == '|':
                        if paths[x[0]-1][x[1]] != '*':
                            visited[x[0]-1][x[1]] = visited[x[0]][x[1]] + 1
                            queue.append([x[0]-1,x[1]])
                if [x[0],x[1]] == end:
                    run = False
                    notPossible = False
                    output.append(visited[x[0]][x[1]]+1)
                    break

            if i == 'D' and x[0] < n-1:
                if visited[x[0]+1][x[1]] == -1:
                    if paths[x[0]][x[1]] == '+' or paths[x[0]][x[1]] == '|':
                        if paths[x[0]+1][x[1]] != '*':
                            visited[x[0]+1][x[1]] = visited[x[0]][x[1]] + 1
                            queue.append([x[0]+1,x[1]])
                if [x[0],x[1]] == end:
                    run = False
                    notPossible = False
                    output.append(visited[x[0]][x[1]]+1)
                    break
    if notPossible:
        output.append(-1)
for i in output:
    print(i)
    
