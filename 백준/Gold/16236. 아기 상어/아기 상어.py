'''
시작 3시 48분
아기상어 크기 2 아기상어 1초 상하좌우 이동
'''

from collections import deque

def check(x,y) : return 0<=x<N and 0<=y<N

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
sx, sy = -1, -1
for i in range(N):
    marker = False
    for j in range(N):
        if matrix[i][j] == 9:
            sx, sy = i, j
            break
    if marker : break
matrix[sx][sy] = 0
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
time, size, eat = 0, 2, 0
INF = 2_100_000_000
while True:
    dq = deque()
    dq.append((sx,sy, 0))
    visit = [[False]*N for _ in range(N)]
    visit[sx][sy]= True
    dist = INF
    locx, locy = -1, -1
    while dq:
        x, y, t = dq.popleft()
        if t>=dist:continue
        for i in range(4):
            X, Y = x+dx[i], y+dy[i]
            if check(X,Y) and not visit[X][Y] and matrix[X][Y]<=size:
                if matrix[X][Y] in [0, size]:
                    visit[X][Y] = True
                    dq.append((X,Y,t+1))
                    continue
                visit[X][Y] = True
                # 사이즈가 작으면 가장 최단 거리 찾고, 조건에 맞는 위치
                if t+1 < dist:
                    dist = t+1
                    locx, locy = X, Y
                    continue
                if t+1 == dist:
                    if locx> X:
                        locx, locy = X, Y
                    elif locx == X:
                        if locy>Y:
                            locx, locy = X, Y

    if (locx, locy) == (-1, -1): break
    time += dist
    sx, sy = locx, locy
    matrix[locx][locy]=0
    eat += 1
    if eat == size:
        size +=1
        eat = 0
print(time)

