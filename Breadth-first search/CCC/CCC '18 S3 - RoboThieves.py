
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
        for j in range(len(mazes[i])):
            if mazes[i][j] == '.':
                dots.append([i, j])
    return dots

def searchStart(mazes):
    output = ''
    for i in range(len(mazes)):
        for j in range(len(mazes[0])):
            if mazes[i][j] == 'S':
                output = [i, j]
    return output     

def findCameras(mazes):
    cameras = []
    for i in range(len(mazes)):
        for j in range(len(mazes[0])):
            if mazes[i][j] == 'C':
                cameras.append([i, j])  
    return cameras

def checkConveyors(position, mazes):
    if mazes[position[0]][position[1]] == 'L' and 0 <= position[1] - 1 < m:
        if not mazes[position[0]][position[1]-1] == 'W':
            position[1] -= 1
            return position
    if mazes[position[0]][position[1]] == 'R' and 0 <= position[1] + 1 < m:
        if not mazes[position[0]][position[1]+1] == 'W':
            position[1] += 1
            return position
    if mazes[position[0]][position[1]] == 'U' and 0 <= position[0] - 1 < m:
        if not mazes[position[0]-1][position[1]] == 'W':
            position[0] -= 1
            return position
    if mazes[position[0]][position[1]] == 'D' and 0 <= position[0] + 1 < m:
        if not mazes[position[0+1]][position[1]] == 'W':
            position[0] += 1
            return position
    return position

def convertToWalls(maze, cameras):
    for i in cameras:
        left = i[1]
        right = i[1]
        top = i[0]
        bottom = i[0]

        while 0 <= left-1 < m:
            left -= 1
            if maze[i[0]][left] == 'W':
                break
            if maze[i[0]][left] not in ['L', 'R', 'U', 'D']:
                maze[i[0]][left] = 'W'
        
        while 0 <= right+1 < m:
            right += 1
            if maze[i[0]][right] == 'W':
                break
            if maze[i[0]][right] not in ['L', 'R', 'U', 'D']:
                maze[i[0]][right] = 'W'
        
        while 0 <= top-1 < n:
            top -= 1
            if maze[i[0]][top] == 'W':
                break
            if maze[top][i[1]] not in ['L', 'R', 'U', 'D']:
                maze[top][i[1]] = 'W'
        
        while 0 <= bottom+1 < n:
            bottom += 1
            if maze[i[0]][bottom] == 'W':
                break
            if maze[bottom][i[1]] not in ['L', 'R', 'U', 'D']:
                maze[bottom][i[1]] = 'W'
    return maze

dotLocations = findDots(mazes)
length = len(dotLocations)
cameraLocations = findCameras(mazes)
start = searchStart(mazes)
output = []
finalMaze = convertToWalls(mazes, cameraLocations)
excuseList = []
count = 0
for i in dotLocations:
    if finalMaze[i[0]][i[1]] == 'W':
        excuseList.append(count)
    count += 1

for i in range(length):
    run = True
    notPossible = True
    excuse = False

    if i in excuseList:
        run = False
        excuse = True
    dot = dotLocations[i]
    queue = []
    queue.append(start)
    visited = {}

    for j in range(n):
        visited[j] = [-1]*m
    
    visited[start[0]][start[1]] = 0

    while queue and run and not excuse:
        x = queue.pop(0)

        for k in ['L', 'R', 'U', 'D']:
            if k == 'L':
                if 0 <= x[1] - 1 < m:
                    if visited[x[0]][x[1]-1] == -1:
                        visited[x[0]][x[1]-1] = visited[x[0]][x[1]] + 1
                        checkConveyor = checkConveyors([x[0], x[1]-1], finalMaze)
                        if finalMaze[checkConveyor[0]][checkConveyor[1]] != finalMaze[x[0]][x[1]-1]:
                            visited[checkConveyor[0]][checkConveyor[1]] = visited[x[0]][x[1]] + 1
                        if finalMaze[checkConveyor[0]][checkConveyor[1]] != 'W':
                            queue.append(checkConveyor)
                        if checkConveyor == dot:
                            run = False
                            notPossible = False
                            output.append(visited[x[0]][x[1]-1])
                            break

            elif k == 'R':
                if 0 <= x[1] + 1 < m:
                    if visited[x[0]][x[1]+1] == -1:
                        visited[x[0]][x[1]+1] = visited[x[0]][x[1]] + 1
                        checkConveyor = checkConveyors([x[0], x[1]+1], finalMaze)
                        if finalMaze[checkConveyor[0]][checkConveyor[1]] != finalMaze[x[0]][x[1]+1]:
                            visited[checkConveyor[0]][checkConveyor[1]] = visited[x[0]][x[1]] + 1
                        if finalMaze[checkConveyor[0]][checkConveyor[1]] != 'W':    
                            queue.append(checkConveyor)
                        if checkConveyor == dot:
                            run = False
                            notPossible = False
                            output.append(visited[x[0]][x[1]+1])
                            break
            
            elif k == 'U':
                if 0 <= x[0] - 1 < n:
                    if visited[x[0]-1][x[1]] == -1:
                        visited[x[0]-1][x[1]] = visited[x[0]][x[1]] + 1
                        checkConveyor = checkConveyors([x[0]-1, x[1]], finalMaze)
                        if finalMaze[checkConveyor[0]][checkConveyor[1]] != finalMaze[x[0]-1][x[1]]:
                            visited[checkConveyor[0]][checkConveyor[1]] = visited[x[0]][x[1]] + 1
                        if finalMaze[checkConveyor[0]][checkConveyor[1]] != 'W':    
                            queue.append(checkConveyor)
                        if checkConveyor == dot:
                            run = False
                            notPossible = False
                            output.append(visited[x[0]-1][x[1]])
                            break
            
            elif k == 'D':
                if 0 <= x[0] + 1 < n:
                    if visited[x[0]+1][x[1]] == -1:
                        visited[x[0]+1][x[1]] = visited[x[0]][x[1]] + 1
                        checkConveyor = checkConveyors([x[0]+1, x[1]], finalMaze)
                        if finalMaze[checkConveyor[0]][checkConveyor[1]] != finalMaze[x[0]+1][x[1]]:
                            visited[checkConveyor[0]][checkConveyor[1]] = visited[x[0]][x[1]] + 1
                        if finalMaze[checkConveyor[0]][checkConveyor[1]] != 'W':    
                            queue.append(checkConveyor)
                        if checkConveyor == dot:
                            run = False
                            notPossible = False
                            output.append(visited[x[0]+1][x[1]])
                            break

    if notPossible:
        output.append(-1)

for i in output:
    print(i)

        

        

