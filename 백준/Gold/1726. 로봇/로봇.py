from collections import deque

def check(x,y):
    return 0<=x<M and 0<=y<N

def switch(n):
    if n in [0,1]:
        return [2,3]
    if n in [2, 3]:
        return [0,1]

M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
sx, sy, sd = map(int, input().split())
sx, sy, sd = sx-1, sy-1, sd-1
ex, ey, ed = map(int, input().split())
ex, ey, ed = ex-1, ey-1, ed-1
visit =[[[False]*N for _ in range(M)] for _ in range(4)]
length =[[[0]*N for _ in range(M)] for _ in range(4)]
dq =deque()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
dq.append([sx,sy,sd])
while dq:
    # print(dq)
    x, y, d = dq.popleft()
    # print(x,y,d)
    if x == ex and y == ey and d==ed:
        break
    for j in range(1,4):
        X = x+dx[d]*j
        Y = y+dy[d]*j
        if check(X,Y) and not visit[d][X][Y] and matrix[X][Y] == 0:
            length[d][X][Y] = length[d][x][y]+1
            visit[d][X][Y] = True
            dq.append([X,Y,d])
        elif check(X, Y) and matrix[X][Y] == 1:
            break
    for i in switch(d):
        if not visit[i][x][y]:
            length[i][x][y] = length[d][x][y] + 1
            visit[i][x][y] = True
            dq.append([x, y, i])

print(length[ed][ex][ey])