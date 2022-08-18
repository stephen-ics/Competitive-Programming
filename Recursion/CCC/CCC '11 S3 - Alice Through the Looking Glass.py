

def magnify():
    pass

def findBase(n, base):
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

base = {}

for i in range(25):
    base[i] = [False]*25

newBase = findBase(2, base)
print(newBase)

n = int(input())

for i in range(n):
    txy = input().split(" ")
    t = txy[0]
    coord = (txy[1],txy[2])

    

# Find Base
# Add Extra (exception if count = 1)