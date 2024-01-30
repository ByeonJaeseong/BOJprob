# import sys
# sys.setrecursionlimit(100_000)

def check(x, y):
    global N
    return 0<=x<N and 0<=y<M

def dfs(x, y):
    global dx
    global dy
    global matrix
    global visit
    if not visit[x][y]:
        visit[x][y]=True
        for i in range(4):
            X = x+dx[i]
            Y = y+dy[i]
            if check(X,Y) and matrix[X][Y]==1 and not visit[X][Y]:
                dfs(X,Y)

TC = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for X in range(1, TC+1):
    M, N, K = map(int, input().split())
    count = 0 # 지렁이 갯수
    #M 가로길이 #N 세로길이 #배추 위치 갯수
    matrix=[[0] * M for _ in range(N)]
    visit = [[False]*M for _ in range(N)]
    # print(M, N, K)
    for _ in range(K):
        Q, P = map(int, input().split())
        # print(P, Q)
        matrix[P][Q]=1
    # for i in range(N):
    #     print(matrix[i])

    for i in range(M):
        for j in range(N):
            if matrix[j][i]==1 and not visit[j][i]:
                dfs(j,i)
                # for p in range(N):
                #     print(visit[p])
                # print()
                count+=1
    print(count)