'''
시작 11시 4분
'''

from collections import deque

def check(x, y) : return 0<=x<M and 0<=y<N

def rolling(d):
    global center, right, below
    if d == 0 : center, right, below = 7-below, right, center
    if d == 1 : center, right, below = right, 7-center, below
    if d == 2 : center, right, below = below, right, 7-center
    if d == 3 : center, right, below = 7-right, center, below

def dir(d):
    if center > matrix[sx][sy] : return (d+1)%4
    elif center < matrix[sx][sy]: return (d - 1) % 4
    else: return d

def scoring(x, y):
    global score
    dq = deque()
    visit = [[False]*N for _ in range(M)]
    visit[x][y] = True
    dq.append((x, y))
    score += matrix[x][y]
    while dq:
        p, q = dq.popleft()
        for i in range(4):
            X, Y = p+dx[i], q+dy[i]
            if check(X,Y) and not visit[X][Y] and matrix[X][Y] == matrix[x][y]:
                visit[X][Y] = True
                score += matrix[X][Y]
                dq.append((X,Y))


M, N, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
center, right, below, d = 6, 3, 5, 1
score = 0
sx, sy = 0, 0
for _ in range(K):
    X, Y = sx+dx[d], sy+dy[d]
    if not check(X,Y) :
        d = (d+2)%4
    sx, sy = sx+dx[d], sy+dy[d]
    rolling(d)
    d = dir(d)
    scoring(sx,sy)
print(score)

