from collections import deque

def check(x,y) :
    return 0<=x<M and 0<=y<N


M, N, K = map(int, input().split())
INF = 2_100_000_000
matrix = [list(map(int, input())) for _ in range(M)]
visit = [[[False] * N for _ in range(M)]for _ in range(K+1)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dq = deque()
dq.append([0,0,0,0])
#x,y, 벽부수기 횟수, length
mn = INF
while dq:
    value = dq.popleft()
    # print(value)
    if value[0]==M-1 and value[1]==N-1:
        mn =min(mn,value[3])
        continue
    for i in range(4):
        X = value[0]+dx[i]
        Y = value[1]+dy[i]
        if check(X,Y) and matrix[X][Y] == 0 and not visit[value[2]][X][Y]:
            visit[value[2]][X][Y] = True
            dq.append([X,Y,value[2],value[3]+1])
        elif check(X,Y) and matrix[X][Y] == 1 and value[2]+1<K+1 and not visit[value[2]+1][X][Y]:
            visit[value[2] + 1][X][Y] = True
            dq.append([X,Y,value[2]+1,value[3]+1])


if mn==INF:
    print(-1)
else:
    print(mn+1)