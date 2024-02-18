
from collections import deque

def check(x,y):
    return 0<=x<N and 0<=y<N


N, K = map(int, input().split())
# N마리 K번까지 바이러스
matrix = [list(map(int, input().split())) for _ in range(N)]
S, Ex, Ey = map(int, input().split())
length = [[0]*N for _ in range(N)]
lst = []
for i in range(N):
    for j in range(N):
        if matrix[i][j]>0:
            lst.append([matrix[i][j], i, j])
lst.sort()
dq = deque()
dq.extend(lst)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while dq:
    v, s, e = dq.popleft()
    # print(s,e)
    if length[s][e]==S: break
    for i in range(4):
        X = s+dx[i]
        Y = e+dy[i]
        if check(X,Y) and matrix[X][Y]==0:
            matrix[X][Y]=v
            length[X][Y] = length[s][e]+1
            dq.append([v,X,Y])
# for i in range(N):
#     print(matrix[i])
print(matrix[Ex-1][Ey-1])