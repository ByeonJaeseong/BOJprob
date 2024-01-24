def check(x,y):
    global visit
    global matrix
    global M
    global N
    if 0<=x<M and 0<=y<N:
        if not visit[x][y] :
            return True
        else:
            return False
    else:
        return False

def cloud(x, y):
    global result
    X = x
    Y = y+1
    while check(X,Y):
        result[X][Y] = (result[X][Y-1]+1)
        Y+=1


M, N = map(int, input().split())
matrix = [list(input()) for _ in range(M)]
result = [[-1]*N for _ in range(M)]
visit = [[False]*N for _ in range(M)]
for i in range(M):
    for j in range(N):
        if matrix[i][j] == 'c':
            visit[i][j] = True
            result[i][j] = 0

for i in range(M):
    for j in range(N):
        if matrix[i][j] == 'c':
            cloud(i , j)

for i in range(M):
    join_str = (' ').join(map(str, result[i]))
    print(join_str)

