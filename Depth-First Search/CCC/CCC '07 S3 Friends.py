def dfs(index, end):
    if visited[index] or possible: return
    visited[index] = True

    connected = connections[index]
    for i in connected:
        if i == end:
            possible = True
            return
        dfs(i)

n = int(input())

connections = {}

for i in range(n):
    xy = input().split(" ")
    x = xy[0]
    y = xy[1]

    if x in connections:
        connections[x].append(y)
    else:
        connections[x] = [y]


visited = {}
for i in range(10000):
    visited[str(i+1)] = False

cord = input().split(" ")
possible = False

dfs(cord[0], cord[1])


if possible:
    print("Yes")

else:
    print("No")






