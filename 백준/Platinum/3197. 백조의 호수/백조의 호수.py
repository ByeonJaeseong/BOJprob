'''
마인드 녹는데 얼마걸리는지 한번에 체크
'''

from collections import deque
def check(x,y):
    return 0<=x<M and 0<=y<N


M, N = map(int, input().split())
INF = 30000
matrix = [list(input()) for _ in range(M)]
length = [[30000]*N for _ in range(M)]

swan_check= False
sx, sy = 0, 0
ex, ey = 0 ,0
dq = deque()
for i in range(M):
    for j in range(N):
        if not swan_check and matrix[i][j]=='L':
            sx, sy = i, j
            swan_check=True
        elif swan_check and matrix[i][j]=='L':
            ex, ey = i, j

        if matrix[i][j] != 'X':
            length[i][j] = 0
            dq.append([i,j])
# print(sx,sy,ex,ey)
######## 시작위치 찾기 끝
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
while dq:
    value = dq.popleft()
    for i in range(4):
        X = value[0] + dx[i]
        Y = value[1] + dy[i]
        if check(X,Y) and length[X][Y]==INF and matrix[X][Y]=='X':

            dq.append([X,Y])
            length[X][Y]=length[value[0]][value[1]]+1

mx = max([max(length[i]) for i in range(M)])
result = -1
lst = []

marker = False
visit = [[False]*N for _ in range(M)]
dq.append([sx,sy])
visit[sx][sy]=True
i=0
# count = 0
while dq and not marker:
    # count +=1
    # print(count)
    value = dq.popleft()
    for j in range(4):
        X = value[0] + dx[j]
        Y = value[1] + dy[j]
        if check(X, Y) and not visit[X][Y] and length[X][Y] <=i:
            dq.append([X, Y])
            visit[X][Y] = True
            if X == ex and Y == ey:
                marker=True
                break
        elif check(X, Y) and not visit[X][Y] and length[X][Y] ==i+1:
            visit[X][Y]=True
            lst.append([X, Y])
    if len(dq)==0:
        dq.extend(lst)
        lst.clear()
        i+=1
if marker:
    result = i
print(result)