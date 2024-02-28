from collections import deque

def check(x,y) :
    global M,N
    return 0<=x<M and 0<=y<N

M, N = map(int, input().split())
matrix = [list(input()) for _ in range(M)]
dq = deque()
jx, jy = 0 ,0
flst = []
for i in range(M):
    for j in range(N):
        if matrix[i][j] == 'J':
            jx, jy= i, j
        if matrix[i][j] == 'F':
            flst.append(['F',i,j])
dq.append(["J", jx, jy])
dq.extend(flst)
# print(dq)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
length = [[0]*N for _ in range(M)]
visit = [[False]*N for _ in range(M)]
visit[jx][jy] = True
marker = False
result = 0
while dq and not marker :
    # print(dq)
    c, x, y = dq.popleft()
    if c=='J' and matrix[x][y]!='F':
        matrix[x][y]='.'
    elif c=='J' and matrix[x][y]=='F':
        continue
    for i in range(4):
        X = x+dx[i]
        Y = y+dy[i]
        if not check(X,Y) and c=='J':
            marker=True
            result = length[x][y]+1
            # print(x,y)
            break
        #지도밖으로 나가면 탈출 표시
        if check(X,Y) and c=='J' and matrix[X][Y]=='.' and not visit[X][Y]:
            matrix[X][Y]='J'
            length[X][Y]=length[x][y]+1
            visit[X][Y]=True
            dq.append(['J',X,Y])
        if check(X, Y) and c == 'F' and (matrix[X][Y] == '.' or matrix[X][Y] == 'J'):
            matrix[X][Y] = 'F'
            dq.append(['F',X,Y])
        #불은 벽을 제외하고 전부 옮기기

# for i in range(M):
#     print(length[i])
if marker:
    print(result)
else:
    print("IMPOSSIBLE")