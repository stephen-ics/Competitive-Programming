n = int(input())
paths = []
visited = {}
for i in range(n):
    path = [int(i) for i in input().split(" ")]
    paths.append(path)
    visited[int(i+1)] = -1

visited[1] = 0
queue = [1]

run = True
possible = False

while queue and run:
    x = queue.pop(0)
    for i in paths[x-1]:
        if i == 0:
            run = False
            possible = True
            break

        if visited[i] == -1:
            visited[i] = visited[x] + 1
            queue.append(i)
            

if possible and -1 not in visited.values():
    print('Y')
    print(visited[x] + 1)
else:
    print('N')

        





