from collections import deque

def check(x,y):
    return 0<=x<M and 0<=y<N

M, N = map(int, input().split())
sx, sy, ex, ey = map(int, input().split())
sx, sy, ex, ey = sx-1, sy-1, ex-1 ,ey-1
matrix = [list(input()) for _ in range(M)]
ghost = [[[] for _ in range(N)] for _ in range(M)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# print(*matrix, sep='\n')
for i in range(M):
    for j in range(N):
        if matrix[i][j] in ['0', '1', '2', '3']:
            # print("실행")
            for k in range(4):
                X,Y, d = i,j, int(matrix[i][j])
                while True:
                    X = X+dx[(d+k)%4]
                    Y = Y+dy[(d+k)%4]
                    if check(X,Y) and matrix[X][Y] == '.':
                        ghost[X][Y].append(k)
                    elif not check(X,Y) or matrix[X][Y] in ['#','0','1','2','3']:
                        break
# print(*ghost,sep='\n')
# 지나갈 수 없는 시간 다 마킹해놓음
dq = deque()
dq.append([sx, sy, 0])
INF = 2_000_000_000
mn = INF
visit = [[[False]*N for _ in range(M)] for _ in range(4)]
# 방문한 시간에 연관된 방문 배열
visit[0][sx][sy] = True
while dq:
    # 지나가는 로직 짜야함
    value = dq.popleft()
    if value[0] == ex and value[1] == ey:
        mn = min(mn, value[2])

    for i in range(4):
        X = value[0]+dx[i]
        Y = value[1]+dy[i]
        time = (value[2]+1)%4
        # 다음칸 방문 안했고, 귀신과 안마주치면
        # print(X,Y,time)
        if check(X,Y) and not visit[time][X][Y] and time not in ghost[X][Y] and matrix[X][Y] == '.':
            dq.append([X,Y,value[2]+1])
            visit[time][X][Y] = True
        # 현재칸 현재시간에 방문 안했고 현재자리에 머무룰 수 있으면서 다음자리 못갈때
        if check(X,Y) and not visit[time][value[0]][value[1]] \
            and time not in ghost[value[0]][value[1]] and time in ghost[X][Y]:
            dq.append([value[0],value[1],value[2]+1])
            visit[time][value[0]][value[1]]=True

if mn == INF:
    print('GG')
else:
    print(mn)
