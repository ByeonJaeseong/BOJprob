from collections import deque

def check(x,y):
    return 0<=x<M and 0<=y<N

def bfs(x, y):
    global matrix, temp_mx, visit
    temp_mx += 1
    dq = deque()
    visit[x][y] = True
    dq.append([x,y])
    while dq:
        value = dq.popleft()
        for i in range(4):
            X = value[0]+dx[i]
            Y = value[1]+dy[i]
            if check(X,Y) and not visit[X][Y] and matrix[X][Y]==1:
                visit[X][Y] = True
                dq.append([X,Y])
                temp_mx += 1


M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
visit = [[False]*N for _ in range(M)]
count = 0
mx = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(M):
    for j in range(N):
        if not visit[i][j] and matrix[i][j]==1:
            temp_mx = 0
            # print(i, j, temp_mx)
            bfs(i,j)
            mx = max(mx, temp_mx)
            count+=1


print(count)
print(mx)


