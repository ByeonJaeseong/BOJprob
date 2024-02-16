from collections import deque
def check(x,y):
    global M,N
    return 0<=x<M and 0<=y<N
def bfs(m,n):
    global matrix, M, N, dx, dy
    visit = [[False] *N for _ in range(M)]
    length = [[0] *N for _ in range(M)]
    mx = 0
    dq = deque()
    dq.append([m,n])
    visit[m][n] = True
    while dq:
        value = dq.popleft()
        for i in range(4):
            X = value[0]+dx[i]
            Y = value[1]+dy[i]
            if check(X,Y) and not visit[X][Y] and matrix[X][Y] == 'L':
                length[X][Y] = length[value[0]][value[1]]+1
                visit[X][Y] = True
                mx = max(length[X][Y], mx)
                dq.append([X,Y])
    return mx




M, N = map(int, input().split())
matrix = [list(input()) for _ in range(M)]
magma_length = [[0] * N for _ in range(M)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for i in range(M):
    for j in range(N):
        if matrix[i][j]=='L':
            magma_length[i][j] = bfs(i, j)
magma_mx = max([max(magma_length[i]) for i in range(M)])
rx = M-1
ry = N-1
for i in range(M):
    marker = False
    for j in range(N):
        if magma_length[i][j] == magma_mx and (rx+ry)>i+j:
            rx = i
            ry = j
print(magma_length[rx][ry])