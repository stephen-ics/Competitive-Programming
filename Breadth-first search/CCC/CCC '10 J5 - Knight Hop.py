
start = [int(i)-1 for i in input().split(" ")]
end = [int(i)-1 for i in input().split(" ")]

queue = [[start[0], start[1]]]
levels = {}

for i in range(8):
    levels[i] = [-1]*8

levels[start[0]][start[1]] += 1
shortest = 0

while queue:
    x = queue.pop(0)
    
    if 0 <= x[0]+2 < 8 and 0 <= x[1]+1 < 8:
        if levels[x[0]+2][x[1]+1] == -1:
            levels[x[0]+2][x[1]+1] = levels[x[0]][x[1]] + 1
            queue.append([x[0]+2,x[1]+1])
            if x[0]+2 == end[0] and x[1]+1 == end[1]:
                shortest = levels[x[0]+2][x[1]+1]
                break
    
    if 0 <= x[0]+1 < 8 and 0 <= x[1]+2 < 8:
        if levels[x[0]+1][x[1]+2] == -1:
            levels[x[0]+1][x[1]+2] = levels[x[0]][x[1]] + 1
            queue.append([x[0]+1,x[1]+2])
            if x[0]+1 == end[0] and x[1]+2 == end[1]:
                shortest = levels[x[0]+1][x[1]+2]
                break

    if 0 <= x[0]-1 < 8 and 0 <= x[1]+2 < 8:
        if levels[x[0]-1][x[1]+2] == -1:
            levels[x[0]-1][x[1]+2] = levels[x[0]][x[1]] + 1
            queue.append([x[0]-1,x[1]+2])
            if x[0]-1 == end[0] and x[1]+2 == end[1]:
                shortest = levels[x[0]-1][x[1]+2]
                break
            
    if 0 <= x[0]-2 < 8 and 0 <= x[1]+1 < 8:
        if levels[x[0]-2][x[1]+1] == -1:
            levels[x[0]-2][x[1]+1] = levels[x[0]][x[1]] + 1
            queue.append([x[0]-2,x[1]+1])
            if x[0]-2 == end[0] and x[1]+1 == end[1]:
                shortest = levels[x[0]-2][x[1]+1]
                break
    
    if 0 <= x[0]-2 < 8 and 0 <= x[1]-1 < 8:
        if levels[x[0]-2][x[1]-1] == -1:
            levels[x[0]-2][x[1]-1] = levels[x[0]][x[1]] + 1
            queue.append([x[0]-2,x[1]-1])
            if x[0]-2 == end[0] and x[1]-1 == end[1]:
                shortest = levels[x[0]-2][x[1]-1]
                break
    
    if 0 <= x[0]-1 < 8 and 0 <= x[1]-2 < 8:
        if levels[x[0]-1][x[1]-2] == -1:
            levels[x[0]-1][x[1]-2] = levels[x[0]][x[1]] + 1
            queue.append([x[0]-1,x[1]-2])
            if x[0]-1 == end[0] and x[1]-2 == end[1]:
                shortest = levels[x[0]-1][x[1]-2]
                break
    
    if 0 <= x[0]+1 < 8 and 0 <= x[1]-2 < 8:
        if levels[x[0]+1][x[1]-2] == -1:
            levels[x[0]+1][x[1]-2] = levels[x[0]][x[1]] + 1
            queue.append([x[0]+1,x[1]-2])
            if x[0]+1 == end[0] and x[1]-2 == end[1]:
                shortest = levels[x[0]+1][x[1]-2]
                break
    
    if 0 <= x[0]-2 < 8 and 0 <= x[1]-1 < 8:
        if levels[x[0]-2][x[1]-1] == -1:
            levels[x[0]-2][x[1]-1] = levels[x[0]][x[1]] + 1
            queue.append([x[0]-2,x[1]-1])
            if x[0]-2 == end[0] and x[1]-1 == end[1]:
                shortest = levels[x[0]-2][x[1]-1]
                break

print(shortest)


