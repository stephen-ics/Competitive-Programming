

def magnify(coords, base, size):
    if base[coords[1]][coords[0]] == True:
        return 'crystal'
    elif count == size:
        return 'empty'
    else:
        pass


def findBase(n):
    unit = 5**n
    centerRight = 0.6 # under or equal 0.6
    centerLeft = 0.4 # over 0.4
    left = 0.2 # over 0.2
    right = 0.8 #under or equal 0.8
    row1 = 0.6 #over or equal to 0.6
    row2 = 0.8 #over or equal to 0.8


    for i in range(unit):
        if row1 < (i+1)/unit <= 0.8:
            for j in range(unit):
                if centerLeft < (j+1)/unit <= centerRight:
                    base[i][j] = True
        elif row2 < (i+1)/unit:
            for j in range(unit):
                if left < (j+1)/unit <= right:
                    base[i][j] = True
    return base


n = int(input())
output = []

for i in range(n):
    count = 0
    txy = input().split(" ")
    size = txy[0]
    base = findBase(size)
    coord = (txy[1],txy[2])
    output.append(magnify(coord, base))
    

    

# Find Base
# Add Extra (exception if count = 1)