from collections import deque

def move(d, rx, ry, bx, by, matrix = []):
    rmarker = False
    bmarker = False
    RX, RY = rx, ry
    BX, BY = bx, by
    for _ in range(2):
        while True:
            X, Y = RX+dx[d], RY+dy[d]
            if matrix[X][Y] == '.':
                matrix[X][Y] = 'R'
                matrix[RX][RY] = '.'
                RX, RY = X, Y
            elif matrix[X][Y] == 'O':
                # 구슬에 들어간 경우
                matrix[RX][RY]='.'
                rmarker = True
                break
            else:
                break
        while True:
            X, Y = BX + dx[d], BY + dy[d]
            if matrix[X][Y] == '.':
                matrix[X][Y] = 'B'
                matrix[BX][BY] = '.'
                BX, BY = X, Y
            elif matrix[X][Y] == 'O':
                # 구슬에 들어간 경우
                matrix[BX][BY] = '.'
                bmarker = True
                return False, -1, -1, -1, -1, matrix
            else:
                break
    if rmarker:
        # 빨간것만 들어간 경우 들어갔다라고 해주기
        return True, -1, -1 ,-1 ,-1, matrix
    else:
        return False, RX, RY, BX, BY, matrix




M, N = map(int, input().split())
matrix = [list(input()) for _ in range(M)]
rx, ry, bx, by = -1, -1, -1, -1
visit = [[[[False]*N for _ in range(M)] for _ in range(N)] for _ in range(M)]
# 빨간 구슬의 좌표가 안쪽 파란구슬의 좌표가 바깥쪽

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
for i in range(M):
    for j in range(N):
        if matrix[i][j]=='R':
            rx, ry = i, j
        if matrix[i][j] == 'B':
            bx, by = i, j

visit[rx][ry][bx][by] = True

dq = deque()
dq.append((0,rx,ry,bx,by,matrix))
time = 0
while dq:
    t, x, y, x1, y1, temp_matrix = dq.popleft()
    for i in range(4):
        move_matrix = [t[:] for t in temp_matrix]
        marker, rx, ry, bx, by, temp = move(i, x, y, x1, y1, move_matrix)
        # print(*temp,sep='\n')
        if marker:
            # print(*temp_matrix,sep='\n')
            # print()
            # print(*temp, sep='\n')
            time = t+1
            dq.clear()
            break
        if (rx, ry, bx, by) == (-1, -1, -1, -1) : continue
        if visit[rx][ry][bx][by]: continue
        visit[rx][ry][bx][by] = True
        dq.append((t+1,rx,ry,bx,by,temp))
if time > 10 or time == 0:
    print(-1)
else:
    print(time)
