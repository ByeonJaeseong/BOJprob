'''
시작 9시 37분
'''
from collections import deque

def check(x,y) : return  0<=x<N and 0<=y<N

def combination(n, lst):
    global combi
    if len(lst)==M:
        combi.append(lst)
        return

    if n>= len(virus): return

    combination(n+1, lst+[virus[n]])
    # 바이러스 넣고 보내기
    combination(n+1, lst)
    # 바이러스 안 넣고 보내기

def spread(lst):
    visit = [[False]*N for _ in range(N)]
    length = [[0] * N for _ in range(N)]
    dq = deque()
    for x, y in lst:
        dq.append((x,y))
        visit[x][y] = True
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            X, Y = x+dx[i], y+dy[i]
            if check(X,Y) and not visit[X][Y] and matrix[X][Y] !=1:
                dq.append((X,Y))
                length[X][Y] = length[x][y] +1
                visit[X][Y] = True
    # print(*visit, sep='\n')
    # print()
    # print(*length, sep='\n')
    # print()
    mx = 0
    for i in range(N):
        for j in range(N):
            if not visit[i][j] and matrix[i][j] == 0:
                # 방문 못한 자리가 있으면 무한대
                return INF
            if visit[i][j] and matrix[i][j] == 0:
                # 바이러스일 때는 제외
                mx = max(mx, length[i][j])
    return mx
N, M = map(int, input().split())
# 바이러스 M개 골라서 활성화 시키기, 바이러스는 2
matrix = [list(map(int, input().split())) for _ in range(N)]
virus = []
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
INF = 2_100_000_000
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 2:
            virus.append((i,j))
combi = []
combination(0,[])
mn = INF
for l in combi:
    # print(spread(l))
    mn = min(mn, spread(l))
if mn == INF:
    print(-1)
else:
    print(mn)
