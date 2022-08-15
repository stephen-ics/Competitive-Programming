
nm = input().split(" ")
n = int(nm[0])
m = int(nm[1])

mazes = []
for i in range(n):
    maze = list(input())
    mazes.append(maze)

def findDots(mazes):
    dots = [] 
    for i in range(len(mazes)):
        for j in mazes[i]:
            if j == '.':
                dots.append([i, j])
    return dots

def searchStart(mazes):
    output = ''
    for i in range(len(mazes)):
        for j in mazes[i]:
            if j == 'S':
                output = [i, j]
    return output            

dotLocations = findDots(mazes)
length = len(dotLocations)
start = searchStart(mazes)

for i in range(length):
    dot = dotLocations[i]
    queue = []
    queue.append(start)
    visited = {}

    for i in range(n):
        visited[i] = [-1]*n
         
    queue.append(start)

    while queue:
        for i in ['L', 'R', 'U', 'D']:
            v

        

        

