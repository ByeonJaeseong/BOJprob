'''
Idea
A가 갈 수 있는 모든경로와 B가 갈 수 있는 모든 경로중에서
서로 안겹치면 통과
그리고 그게 최솟값 일때가 정답
'''
from collections import deque
def check(x,y):
    global M,N, matrix
    return 0<=x<M and 0<=y<N and matrix[x][y]!='X'
#탐색할 수 있는 공간만 탐색

def bfs():
    global M, N
    global matrix, visit
    global A_y_start, A_x_start, B_y_start, B_x_start
    dq = deque()
    dq.append([A_x_start, A_y_start, B_x_start, B_y_start, 1])
    visit[A_x_start][A_y_start][B_x_start][B_y_start] =True
    #경로 탐색 시작
    while dq:
        value = dq.popleft()
        Ax, Ay, Bx, By, length = value[0], value[1], value[2], value[3], value[4]
        for i in range(9):
            # A이동 시작
            AX = Ax+dx[i]
            AY = Ay+dy[i]
            if check(AX, AY):
                for j in range(9):
                    BX = Bx + dx[j]
                    BY = By + dy[j]
                    if check(BX, BY):
                        #탐색 가능한 케이스 중에서만
                        if AX==Bx and AY==By and BX==Ax and BY == Ay:
                            continue
                            #교차하는 경우는 패스
                        if AX==BX and AY==BY:
                            continue
                            #같은 자리에 있는 경우에도 패스
                        if AX==B_x_start and AY == B_y_start and BX == A_x_start and BY == A_y_start:
                            return length
                        if not visit[AX][AY][BX][BY]:
                            visit[AX][AY][BX][BY] = True
                            dq.append([AX,AY,BX, BY,length+1])
    return -1




M, N = map(int,input().split())
matrix = [list(input()) for _ in range(M)]
visit= [[[[False] *N for _ in range(M)]for _ in range(N)]for _ in range(M)]
## A, B 경로 체크
A_x_start, A_y_start = 0, 0
B_x_start, B_y_start = 0, 0
dx = [1, 1, 1, -1, -1, -1, 0, 0, 0]
dy = [1, 0, -1, 1, 0, -1, 1, 0, -1]
for i in range(M):
    for j in range(N):
        if matrix[i][j]=='A':
            A_x_start, A_y_start = i, j
        if matrix[i][j] == 'B':
            B_x_start, B_y_start = i, j
result = bfs()
print(result)