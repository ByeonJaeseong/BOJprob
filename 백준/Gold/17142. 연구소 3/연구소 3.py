'''
worst 케이스 조합 252
탐색시간 50*50*252 =630_000
시간 자체는 충분함 -> 구상 완료 5분
'''
from collections import deque

def check(x,y):
    return 0<=x<N and 0<=y<N

def combi(n, lst=[]):
    global mn
    if len(lst) ==M:
        dq =deque()
        dq.extend(lst)
        mx = 0
        visit = [[False]*N for _ in range(N)]
        length = [[0]*N for _ in range(N)]
        for i in range(M):
            x, y = lst[i]
            visit[x][y] = True
        # 바이러스 마킹
        while dq:
            x, y = dq.popleft()
            for i in range(4):
                X = x+dx[i]
                Y = y+dy[i]
                if check(X,Y) and not visit[X][Y] and matrix[X][Y] in [0, 2]:
                    visit[X][Y] = True
                    length[X][Y] = length[x][y]+1
                    dq.append((X,Y))
        for i in range(N):
            for j in range(N):
                if matrix[i][j] == 0 and not visit[i][j]:
                    # 빈칸과 바이러스가 있는데 방문을 안한경우
                    mx = -1
                    return
                if matrix[i][j] == 0 and visit[i][j]:
                    mx = max(mx, length[i][j])
        if mx !=-1:
            mn = min(mn,mx)
        return
    # 활성 바이러스 갯수 정해지면
    if n == len(virus):
        return
    # 바이러스 갯수 다 썼으면
    combi(n+1, lst+[(virus[n])])
    # 바이러스를 활성시키는 경우
    combi(n + 1, lst)
    # 바이러스를 활성시키지 않는 경우
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
virus = []
INF = 1_000_000_000
mn = INF
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 2:
            virus.append((i,j))
combi(0, [])
if mn == INF:
    print(-1)
else:
    print(mn)