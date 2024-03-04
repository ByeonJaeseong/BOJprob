from collections import deque

def check(x,y):
    return 0<=x<M and 0<=y<N and matrix[x][y]==0

K = int(input())
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
visit = [[[False]*N for _ in range(M)] for _ in range(K+1)]
dx = [1,0,-1,0,2,1,-1,-2,-2,-1,1,2]
dy = [0,1,0,-1,1,2,2,1,-1,-2,-2,-1]
dq = deque()
dq.append([0,0,0,0])
#x,y,말횟수, 이동횟수
visit[0][0][0]=True
INF =2_100_000_000
mn = INF
while dq:
    value = dq.popleft()
    # print(value)
    if value[0]==M-1 and value[1]==N-1:
        mn = min(mn, value[3])
        continue
    if value[2]<K:
        for i in range(12):
            X = value[0] + dx[i]
            Y = value[1] + dy[i]
            if i<4:
                if check(X,Y) and not visit[value[2]][X][Y]:
                    visit[value[2]][X][Y]=True
                    dq.append([X,Y,value[2],value[3]+1])
            else:
                if check(X,Y) and not visit[value[2]+1][X][Y]:
                    visit[value[2]+1][X][Y] = True
                    dq.append([X, Y, value[2]+1, value[3] + 1])
    else:
        for i in range(4):
            X = value[0] + dx[i]
            Y = value[1] + dy[i]
            if check(X,Y) and not visit[value[2]][X][Y]:
                visit[value[2]][X][Y]=True
                dq.append([X,Y,value[2],value[3]+1])
if mn == INF:
    print(-1)
else:
    print(mn)