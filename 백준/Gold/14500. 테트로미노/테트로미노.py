
def check(x,y) : return 0<=x<M and 0<=y<N

def tetris(x,y, value, lst = []):
    global mx
    if len(lst) == 4:
        mx = max(mx, value)
        return

    if (4-len(lst))*mx_value+value<=mx:
        return

    for p, q in lst:
        for i in range(4):
            X = p + dx[i]
            Y = q + dy[i]
            if check(X,Y) and (X,Y) not in lst:
                tetris(X,Y, value+matirx[X][Y], lst+[(X,Y)])


M, N = map(int, input().split())
matirx = [list(map(int, input().split())) for _ in  range(M)]
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)
mx = 0
mx_value = max([max(m) for m in matirx])
for i in range(M):
    for j in range(N):
        tetris(i, j, matirx[i][j], [(i,j)])
print(mx)
