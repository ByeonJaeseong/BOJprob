from collections import deque

def check(X,Y):
    global M, N
    return 0<=X<M and 0<=Y<N

def bfs(x,y):
    global matrix
    global visit
    global length
    global N
    global M
    dq = deque()
    dq.append([x,y])
    visit[x][y]=True
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    while dq:
        value = dq.popleft()
        if value[0] == M-1 and value[1]==N-1:
            break
        for i in range(4):
            X = value[0]+dx[i]
            Y = value[1]+dy[i]
            if check(X,Y) and not visit[X][Y] and matrix[X][Y]=='1':
                visit[X][Y]=True
                length[X][Y] = length[value[0]][value[1]]+1
                dq.append([X,Y])


M, N = map(int, input().split())
matrix = [list(input()) for _ in range(M)]
visit = [[False]*N for _ in range(M)]
length = [[1]*N for _ in range(M)]
bfs(0,0)
# for i in range(M):
#     print(visit[i])
print(length[M-1][N-1])