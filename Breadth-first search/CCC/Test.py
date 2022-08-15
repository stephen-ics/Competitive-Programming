n = int(input())
paths = []
visited = {}
for i in range(n):
    path = [int(i) for i in input().split(" ")]
    paths.append(path)
    visited[int(i+1)] = 1

visited[1] = 0    

if -1 not in visited.values():
    print('Y')
else:
    print('N')

        





