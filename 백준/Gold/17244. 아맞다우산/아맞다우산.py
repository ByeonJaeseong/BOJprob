
from collections import deque
def check(x,y):
    return 0<=x<M and 0<=y<N and matrix[x][y]!='#'
def bfs(n, m, count, dist, matrix, lst=deque()):
    global sx, sy, ex, ey, result
    dq = deque()
    dq.append([n,m])
    visit = [[False]*N for _ in range(M)]
    length = [[0]*N for _ in range(M)]
    visit[n][m]=True

    while dq:
        value = dq.popleft()
        for i in range(4):
            X = value[0]+dx[i]
            Y = value[1]+dy[i]
            if check(X,Y) and not visit[X][Y]:
                visit[X][Y]=True
                dq.append([X,Y])
                length[X][Y] = length[value[0]][value[1]]+1
    # for i in range(M):
    #     print(length[i])
    # print()
    if count == 0:
        dist += length[ex][ey]
        result = min(dist, result)
    else:

        for _ in range(count):
            value = lst.popleft()
            matrix[value[0]][value[1]]="."
            dist += length[value[0]][value[1]]
            # print(dist)
            bfs(value[0], value[1], count-1, dist, matrix, lst )
            lst.append(value)
            matrix[value[0]][value[1]] = "X"
            dist -= length[value[0]][value[1]]











N, M = map(int, input().split())
matrix = [list(input()) for _ in range(M)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
count = 0
result = 1000000000
sx, sy = 0, 0
ex, ey = 0, 0
lst = deque()
for i in range(M):
    for j in range(N):
        if matrix[i][j]=='X':
            count +=1
            lst.append([i, j])
        if matrix[i][j]=='S':
            sx = i
            sy = j
        if matrix[i][j]=='E':
            ex = i
            ey = j

bfs(sx, sy, count, 0, matrix, lst)
print(result)