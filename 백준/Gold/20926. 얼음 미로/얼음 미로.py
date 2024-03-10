from collections import deque

def check(x,y):
    return 0<=x<M and 0<=y<N

N, M = map(int, input().split())
matrix = [list(input()) for _ in range(M)]
tx, ty = 0, 0
for i in range(M):
    for j in range(N):
        if matrix[i][j]=='T':
            tx, ty = i, j
            matrix[i][j] ='0'
            break
INF = 2_100_000_000
visit = [[[INF]*N for _ in range(M)] for _ in range(4)]
dq = deque()
## 포인트는 왔던 길 다시 안가기
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dq.append([tx, ty, 0, 0])
dq.append([tx, ty, 0, 1])
dq.append([tx, ty, 0, 2])
dq.append([tx, ty, 0, 3])
for i in range(4):
    visit[i][tx][ty] = 0
mn = 2_100_000_000
while dq:
    x, y, l, d = dq.popleft()
    while True:
        X, Y = x+dx[d], y+dy[d]
        if not check(X,Y): break
        #안에 있는 케이스만
        if visit[d][X][Y]<l: break
        visit[d][X][Y] = l
        if matrix[X][Y] == 'H' : break
        # 홀이면 빠트리기
        if matrix[X][Y] == 'E' :
            mn = min(mn, l)
            break
        if matrix[X][Y] == 'R':
            # if visit[d][X][Y] > l: visit[d][X][Y]=l
            if visit[(d+1)%4][x][y]>l :
                dq.append([x, y, l, (d + 1) % 4])
                visit[(d + 1) % 4][x][y] = l
            if visit[(d+2)%4][x][y]>l:
                dq.append([x, y, l, (d + 2) % 4])
                visit[(d + 2) % 4][x][y] = l
            if visit[(d+3)%4][x][y]>l:
                dq.append([x, y, l, (d + 3) % 4])
                visit[(d + 3) % 4][x][y] = l
            break
        # print(*visit,sep='\n')
        l += int(matrix[X][Y])
        x += dx[d]
        y += dy[d]
if mn == INF:
    print(-1)
else:
    print(mn)