'''
union-find and simulation
-> 단순 union - find드 보단 크루스칼에 가까움

아 아니다 다익스트라다
아니 그냥 크루스칼이 맞을듯
'''

from collections import deque
import heapq

def find(n):
    global group
    if group[n]!=n:
        group[n] = find(group[n])
    return group[n]

def union(a, b):
    global group
    group[find(b)] = find(a)


def check(x,y):
    return 0<=x<M and 0<=y<N

M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
visit = [[False]*N for _ in range(M)]
INF = 2_100_000_000
numbers = [[0]*N for _ in range(M)]
name  = 1
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
for i in range(M):
    for j in range(N):
        if matrix[i][j] == 1 and not visit[i][j]:
            dq = deque()
            dq.append((i,j))
            visit[i][j]=True
            numbers[i][j] = name
            while dq:
                x, y = dq.popleft()
                for k in range(4):
                    X = x+dx[k]
                    Y = y+dy[k]
                    if check(X,Y) and not visit[X][Y] and matrix[X][Y] ==1:
                        visit[X][Y]=True
                        dq.append((X,Y))
                        numbers[X][Y] = name
            name+=1
# print(name-1)
adj = [[INF]*(name) for _ in range(name)]
# 패딩해놓은 상태
for i in range(M):
    sx = i
    sy = -1
    for j in range(N):
        # print(sx, sy)
        if sy==-1 and numbers[i][j] != 0:
            sy = j
            continue
        # 시작값 셋팅
        if numbers[i][j] == numbers[sx][sy]:
            sy = j
            continue

        if numbers[i][j] != 0 and numbers[sx][sy] != numbers[i][j]:
            dist = j - sy -1
            # print(dist)
            if dist>1:
                adj[numbers[sx][sy]][numbers[i][j]] = min(adj[numbers[sx][sy]][numbers[i][j]], dist)
                adj[numbers[i][j]][numbers[sx][sy]] = min(adj[numbers[i][j]][numbers[sx][sy]], dist)
            sy = j


for j in range(N):
    sx = -1
    sy = j
    for i in range(M):
        # print(sx, sy)
        if sx==-1 and numbers[i][j] != 0:
            sx = i
            continue
        # 시작값 셋팅
        if numbers[i][j] == numbers[sx][sy]:
            sx = i
            continue

        if numbers[i][j] != 0 and numbers[sx][sy] != numbers[i][j]:
            dist = i - sx -1
            # print(dist)
            if dist>1:
                adj[numbers[sx][sy]][numbers[i][j]] = min(adj[numbers[sx][sy]][numbers[i][j]], dist)
                adj[numbers[i][j]][numbers[sx][sy]] = min(adj[numbers[i][j]][numbers[sx][sy]], dist)
            sx = i
# 이제 셋팅은 다 됐고 모든 경로를 통해서 건너면 됨
# print(*numbers, sep='\n')
# print()
# print(*adj, sep='\n')
distance = []
heapq.heapify(distance)
for i in range(1,name):
    for j in range(1,name):
        if adj[i][j]!=INF:
            heapq.heappush(distance, (adj[i][j],i,j))
group = [i for i in range(name)]
count = 0
for i in range(len(distance)):
    d, x, y = heapq.heappop(distance)

    if find(x) != find(y):
        union(x, y)
        count += d
marker = 0
for i in range(1,name):
    if group[i] == i:
        marker +=1
# print(group)
if marker > 1:
    print(-1)
else:
    print(count)


