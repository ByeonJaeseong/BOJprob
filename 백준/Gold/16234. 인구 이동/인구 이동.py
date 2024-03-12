'''
얘부터 풀기로 결정
구상 3분 -> BFS로 구현하기로 함
'''
from collections import deque

def check(x,y):
    return 0<=x<N and 0<=y<N

def bfs(x,y):
    global visit
    dq =deque()
    dq.append((x,y))
    result = []
    sm = 0
    while dq:
        # print(*visit,sep='\n')
        # print()
        p, q = dq.popleft()
        sm += matrix[p][q]
        result.append((p,q))
        for i in range(4):
            X = p+dx[i]
            Y = q+dy[i]
            if check(X,Y) and not visit[X][Y] and MN<=abs(matrix[X][Y]-matrix[p][q])<=MX:
                visit[X][Y] = True
                dq.append((X,Y))
    return [sm, result]


N, MN, MX = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 0
while True:
    # print(count)
    marker = False
    visit = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                visit[i][j]=True
                sm, result = bfs(i, j)
                if len(result) == 1: continue
                marker = True
                value = sm//len(result)
                for x, y in result:
                    matrix[x][y]=value
    # print(*matrix, sep='\n')
    if marker: count+=1
    else: break
print(count)