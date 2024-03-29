'''
+1분 합시다
벽이 작으니 노상관
'''

from collections import deque

def check(x,y) : return 0<=x<M and 0<=y<N

def combination(n, lst=[]):
    global combi
    if len(lst) == 3:
        combi.append(lst)
        return

    if n == len(wall):
        return

    combination(n+1, lst+[(wall[n])])
    combination(n + 1, lst)

def spread(matrix= []):
    visit = [[False]*N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 2 and not visit[i][j]:
                dq = deque()
                dq.append((i,j))
                visit[i][j] = True
                while dq:
                    p, q = dq.popleft()
                    for k in range(4):
                        X, Y = p+dx[k], q+dy[k]
                        if check(X,Y) and not visit[X][Y] and matrix[X][Y] == 0:
                            matrix[X][Y] = 2
                            visit[X][Y] = True
                            dq.append((X,Y))
    count = 0
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                count+=1

    return count
M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
wall = []
combi = []
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)
for i in range(M):
    for j in range(N):
        if matrix[i][j] == 0 :
            wall.append((i,j))
combination(0,[])
mx = 0
for w in combi:
    temp = [m[:] for m in matrix]
    # print(w)
    for wal in w:
        x, y = wal
        temp[x][y] = 1
    mx = max(mx,spread(temp))
    # print(*temp, sep='\n')
    # print()

print(mx)