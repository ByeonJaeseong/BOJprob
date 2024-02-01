from collections import deque

def check(x, y):
    global M
    global N
    return 0<=x<N and 0<=y<M

def dfs():
    global matrix
    global length
    global start
    dq = deque()
    for i in start:
        dq.append([i[0], i[1], 0])
        length[i[0]][i[1]]=0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while dq:
        value = dq.popleft()
        for i in range(4):
            X = value[0]+dx[i]
            Y = value[1]+dy[i]
            if check(X,Y) and matrix[X][Y]==0:
                if length[X][Y]>value[2]+1:
                    length[X][Y] = value[2]+1
                    dq.append([X,Y,length[X][Y]])

M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
length = [[1000*1000]*M for _ in range(N)]
start = []
# 토마토 집어넣기
for i in range(N):
    for j in range(M):
        if matrix[i][j]==1:
            start.append([i,j])
dfs()
marker = False
max_value=0
# 0인 것이 하나라도 있나 확인
for i in range(N):
    # print(length[i])
    for j in range(M):
        if matrix[i][j]==0 and length[i][j]==1_000_000:
            marker = True
            break
        elif matrix[i][j]!=-1 and length[i][j]!=1_000_000:
            max_value=max(max_value, length[i][j])
    if marker :
        break

if not marker:
    print(max_value)
else:
    print(-1)