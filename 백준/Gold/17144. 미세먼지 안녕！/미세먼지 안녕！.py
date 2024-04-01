'''
구현 시작 4시 12분
'''

def check(x,y): return 0<=x<M and 0<=y<N

M, N, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
sx = -1
for i in range(M):
    if matrix[i][0] == -1:
        sx = i
        break
for _ in range(K):
    new = [[0]*N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            if matrix[i][j] > 0:
                count = 0
                for k in range(4):
                    X, Y = i+dx[k], j+dy[k]
                    if check(X,Y) and matrix[X][Y]>=0:
                        count+=1
                value = matrix[i][j]//5
                new[i][j] += matrix[i][j] - value*count
                for k in range(4):
                    X, Y = i+dx[k], j+dy[k]
                    if check(X,Y) and matrix[X][Y]>=0:
                        new[X][Y] += value
    new[sx][0], new[sx+1][0] = -1, -1
    matrix = new
    # print(*matrix, sep='\n')
    # print()
    ## 미세먼지 확산 완료
    # 위쪽은 반시계 아래쪽은 시계방향 구현
    # 위쪽 sx, 아래쪽 sx+1
    if matrix[sx-1][0] > 0 :
        matrix[sx-1][0] =0
    locx, locy, d = sx-1, 0, 0
    while True:
        X, Y = locx + dx[d], locy+ dy[d]
        if not(0<=X<=sx and 0<=Y<N):
            d = (d+1)%4
            X, Y = locx + dx[d], locy + dy[d]
        # print(*matrix, sep='\n')
        # print()
        if matrix[X][Y] == -1 : break
        matrix[locx][locy] = matrix[X][Y]
        matrix[X][Y] = 0
        locx, locy = X, Y
    # print("실행")
    locx, locy, d = sx+2, 0, 3
    if matrix[sx+2][0] > 0 :
        matrix[sx+2][0] =0
    while True:
        X, Y = locx + dx[d], locy+ dy[d]
        if not(sx+1<=X<M and 0<=Y<N):
            d = (d-1)%4
            X, Y = locx + dx[d], locy + dy[d]
        if matrix[X][Y] == -1 : break
        matrix[locx][locy] = matrix[X][Y]
        matrix[X][Y] = 0
        locx, locy = X, Y
    # print(*matrix, sep='\n')
    # print()

print(sum([sum(x) for x in matrix])+2)
