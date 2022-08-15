n = int(input())
paths = []
visited = {}
for i in range(n):
    path = [int(i) for i in input().split(" ")]
    paths.append(path)
    visited[int(i+1)] = -1

visited[1] = 0
queue = [1]
solutions = []

possible = False

while queue:
    x = queue.pop(0)
    for i in paths[x-1]:
        if i == 0:
            solutions.append(visited[x])
            possible = True

        elif visited[i] == -1:
            visited[i] = visited[x] + 1
            queue.append(i)
            

if possible and -1 not in visited.values():
    print('Y')
    solutions.sort()
    print(solutions[0] + 1)
else:
    print('N')
    print(solutions[0] + 1)

        





