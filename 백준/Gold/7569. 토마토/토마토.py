from collections import deque

def check(z, x, y):
    global M
    global N
    return 0<=z<K and 0<=x<N and 0<=y<M

def dfs():
    global matrix
    global length
    global start
    dq = deque()
    for i in start:
        dq.append([i[0], i[1], i[2], 0])
        length[i[0]][i[1]][i[2]]=0
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0,  1, -1]
    while dq:
        value = dq.popleft()
        for i in range(6):
            Z = value[0]+dz[i]
            X = value[1]+dx[i]
            Y = value[2]+dy[i]
            if check(Z,X,Y) and matrix[Z][X][Y]==0:
                if length[Z][X][Y]>value[3]+1:
                    length[Z][X][Y] = value[3]+1
                    dq.append([Z,X,Y,length[Z][X][Y]])

M, N, K = map(int, input().split())
matrix = [[list(map(int, input().split())) for _ in range(N)] for _ in range(K)]
length = [[[100*100*100]*M for _ in range(N)] for _ in range(K)]
# print(matrix)
start = []
# 토마토 집어넣기
for k in range(K):
    for i in range(N):
        for j in range(M):
            if matrix[k][i][j]==1:
                start.append([k,i,j])
dfs()
marker = False
max_value=0
# 0인 것이 하나라도 있나 확인
for k in range(K):
    # print(length[i])
    for i in range(N):
        for j in range(M):
            if matrix[k][i][j]==0 and length[k][i][j]==1_000_000:
                marker = True
                break
            elif matrix[k][i][j]!=-1 and length[k][i][j]!=1_000_000:
                max_value=max(max_value, length[k][i][j])
        if marker :
            break

if not marker:
    print(max_value)
else:
    print(-1)