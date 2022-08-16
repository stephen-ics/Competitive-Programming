m = int(input())
n = int(input())

start = [0, 0]
end = [m-1, n-1]

queue = [[start[0], start[1]]]
levels = {}
visited = []

for i in range(m):
    levels[i] = [int(i) for i in input().split(" ")]

shortest = 0

def findMultiples(x):
    multiple = []
    for i in range(1, int(x/2)+1):
        if x % i == 0:
            multiple.append([i-1, int(x/i)-1])
            multiple.append([int(x/i)-1, i-1])
    
    return multiple

run = True
notPossible = True
while queue and run:
    x = queue.pop(0)
    visited.append(x)
    value = levels[x[0]][x[1]]
    multiples = findMultiples(value)

    for i in multiples:
        if 0 <= i[0] < m and 0 <= i[1] < n and i not in visited:
            queue.append(i)
            if i == end:
                run = False
                notPossible = False
                print('yes')
                break

if notPossible:
    print('no')
        
        

    

        

   

