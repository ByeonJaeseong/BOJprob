from collections import deque
def check(x,y):
    return 0<=x<M and 0<=y<N

TC = int(input())
for _ in range(TC):
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(M)]
    sx, sy = 0, 0

    dq = deque()
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == '*':
                dq.append([i, j,'*'])
            if matrix[i][j] == '@':
                sx, sy = i, j
    dq.append([sx, sy, '@'])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    marker = False
    length = [[0]*N for _ in range(M)]
    result = 0
    while dq and not marker:
        value = dq.popleft()
        # 사람이면 움직임
        if value[2] == '@':
            for i in range(4):
                X = value[0]+dx[i]
                Y = value[1]+dy[i]
                if not check(X,Y) :
                    result = length[value[0]][value[1]]+1
                    marker =True
                    break
                if check(X,Y) and matrix[X][Y] == '.':
                    matrix[X][Y]='@'
                    length[X][Y] = length[value[0]][value[1]]+1
                    dq.append([X,Y, '@'])
        else:
            for i in range(4):
                X = value[0]+dx[i]
                Y = value[1]+dy[i]
                if check(X,Y) and matrix[X][Y] in ['.', '@']:
                    matrix[X][Y]='*'
                    dq.append([X,Y, '*'])
    if marker:
        print(result)
    else:
        print("IMPOSSIBLE")
