import queue

n = int(input())

def printMaze(maze, path=''):
  x = 0
  y = 0
  pos = set()
  for move in path:
    if move == 'L':
      x -= 1

    elif move == 'R':
      x += 1

    elif move == 'U':
      y -= 1

    elif move == 'D':
      y += 1
    pos.add((x, y))

  for j, row in enumerate(maze):
    for i, col in enumerate(row):
      if (j , i) in pos:
        print('+', end='')
      else:
        print(col + ' ', end='')
    print()
        
    
  

def valid(maze, moves):
  x = 0
  y = 0

  for move in moves:
    if move == 'L':
      if not (maze[y][x] == '+' and maze[y][x] == '-'):
        return False
      x -= 1
    elif move == 'R':
      if not (maze[y][x] == '+' and maze[y][x] == '-'):
        return False
      x += 1
    elif move == 'U':
      if not (maze[y][x] == '+' and maze[y][x] == '|'):
        return False
      y -= 1
    elif move == 'D':
      if not (maze[y][x] == '+' and maze[y][x] == '|'):
        return False
      y += 1

    if not (0 <= x < len(maze[0]) and 0 <= j < len(maze)):
      return False
    elif (maze[y][x] == '*'):
      return False
      
  return True
      
def findEnd(maze, moves):
  x = 0
  y = 0

  for move in moves:
    if move == 'L':
      x -= 1
    elif move == 'R':
      x += 1
    elif move == 'U':
      y -= 1
    elif move == 'D':
      y += 1
    if (x == len(maze[0])-1 and y == len(maze)-1):
      print('Found: ' + moves)
      return True
  return False

for i in range(n):
  height = int(input())
  width = int(input())

  maze = []
  for i in range(height):
    mazeLine = input()
    maze.append(mazeLine)

  nums = queue.Queue()
  nums.put('')
  add = ''

  while not findEnd(maze, add):
    add = nums.get()
    for j in ['L', 'R', 'U', 'D']:
      put = add + j
      if valid(maze, put):
        nums.put(put)