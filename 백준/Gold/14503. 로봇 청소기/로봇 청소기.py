'''
구현 시작 1분
'''

M, N = map(int, input().split())
sx, sy, d = map(int, input().split())
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
matirx= [list(map(int, input().split())) for _ in range(M)]
while True:
    if matirx[sx][sy] == 0:
        matirx[sx][sy] = 2
    marker = False
    for _ in range(4):
        d = (d-1)%4
        X, Y = sx+dx[d], sy+dy[d]
        if matirx[X][Y] == 0:
            marker = True
            sx, sy = X, Y
            break
    if marker: continue
    if matirx[sx+dx[(d+2)%4]][sy+dy[(d+2)%4]] == 2:
        sx, sy = sx+dx[(d+2)%4], sy+dy[(d+2)%4]
    else:
        break
count = 0
for i in range(M):
    for j in range(N):
        if matirx[i][j] == 2:
            count+=1
print(count)