
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

def findCameras(mazes):
    cameras = []
    for i in range(len(mazes)):
        for j in mazes[i]:
            if j == 'C':
                cameras.append([i, j])  
    return cameras

def checkConveyors(position, mazes):
    if position == 'L' and 0 <= position[1] - 1 < m:
        if not mazes[position[0]][position[1]-1] == 'W':
            position[1] - 1
            return position
    if position == 'R' and 0 <= position[1] + 1 < m:
        if not mazes[position[0]][position[1]+1] == 'W':
            position[1] + 1
            return position
    if position == 'U' and 0 <= position[0] - 1 < m:
        if not mazes[position[0]-1][position[1]] == 'W':
            position[0] - 1
            return position
    if position == 'D' and 0 <= position[0] + 1 < m:
        if not mazes[position[0+1]][position[1]] == 'W':
            position[0] + 1
            return position
    return position

def convertToWalls(maze, cameras):
    for i in cameras:
        left = i[1]
        right = i[1]
        top = i[0]
        bottom = i[0]

        while 0 <= left < m:
            if maze[i[0]][left] not in ['L', 'R', 'U', 'D']:
                maze[i[0]][left] = 'W'
                left -= 1
        
        while 0 <= right < m:
            if maze[i[0]][right] not in ['L', 'R', 'U', 'D']:
                maze[i[0]][right] = 'W'
                right += 1
        
        while 0 <= top < n:
            if maze[top][i[1]] not in ['L', 'R', 'U', 'D']:
                maze[top][i[1]] = 'W'
                top -= 1
        
        while 0 <= bottom < n:
            if maze[bottom][i[1]] not in ['L', 'R', 'U', 'D']:
                maze[bottom][i[1]] = 'W'
                bottom += 1
         
dotLocations = findDots(mazes)
cameraLocations = findCameras(mazes)
length = len(dotLocations)
start = searchStart(mazes)
print(cameraLocations)
finalMaze = convertToWalls(mazes, cameraLocations)
output = []

for i in range(length):
    dot = dotLocations[i]
    queue = []
    queue.append(start)
    visited = {}

    for i in range(n):
        visited[i] = [-1]*n
    
    visited[start]
         
    queue.append(start)
    run = True
    notPossible = False
    while queue and run:
        x = queue.pop[0]

        for i in ['L', 'R', 'U', 'D']:
            if i == 'L':
                if 0 <= x[1] - 1 < len(m):
                    visited[x[0]][x[1]-1] = visited[x[0]][x[1]] + 1
                    checkConveyor = checkConveyors(visited[x[0]][x[1]-1], finalMaze)
                    if checkConveyor != 'W':
                        queue.append(checkConveyor)
                    if checkConveyor == dot:
                        run = False
                        notPossible = True
                        break


            elif i == 'R':
                if 0 <= x[1] + 1 < len(m):
                    visited[x[0]][x[1]+1] = visited[x[0]][x[1]] + 1
                    checkConveyor = checkConveyors(visited[x[0]][x[1]+1], finalMaze)
                    if checkConveyor != 'W':
                        queue.append(checkConveyor)
                    if checkConveyor == dot:
                        run = False
                        notPossible = True
                        break
            
            elif i == 'U':
                if 0 <= x[0] - 1 < len(n):
                    visited[x[0]-1][x[1]] = visited[x[0]][x[1]] + 1
                    checkConveyor = checkConveyors(visited[x[0]-1][x[1]], finalMaze)
                    if checkConveyor != 'W':
                        queue.append(checkConveyor)
                    if checkConveyor == dot:
                        run = False
                        notPossible = True
                        break
            
            elif i == 'D':
                if 0 <= x[0] + 1 < len(m):
                    visited[x[0]+1][x[1]] = visited[x[0]][x[1]] + 1
                    checkConveyor = checkConveyors(visited[x[0]+1][x[1]], finalMaze)
                    if checkConveyor != 'W':
                        queue.append(checkConveyor)
                    if checkConveyor == dot:
                        run = False
                        notPossible = True
                        output.append(visited[x[0]+1][x[1]])
                        break

    if notPossible:
        output.append(-1)

for i in output:
    print(i)

        

        

