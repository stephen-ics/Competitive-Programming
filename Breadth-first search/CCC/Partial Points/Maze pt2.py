n = int(input())

for i in range(n):
    n = int(input())
    m = int(input())
    
    paths = []
    queue = []

    for i in range(n):
        path = list(input())
        paths.append(path)
    
    start = [0, 0]
    end = [len(n)-1, len(m)-1]

    queue.append(start)

    for i in ['L', 'R', 'U', 'D']:     
        if i == 'L':
            pass
        if i == 'R':
            pass
        if i == 'U':
            pass
        if i == 'D':
            pass
    
