'''
오작교 두 개 연속 건너기 불가능
'''
from collections import deque

def check(x,y):
    return 1<=x<N+1 and 1<=y<N+1

def move():
    global mn
    length = [[INF]*(N+2) for _ in range(N+2)]
    dq =deque()
    dq.append([1,1,False])
    length[1][1]=0
    while dq:
        # print(dq)
        x, y, v = dq.popleft()
        if x == N and y ==N:
            mn = min(mn, length[x][y])
            continue
        for i in range(4):
            X = x+dx[i]
            Y = y+dy[i]
            if not check(X,Y):continue
            if length[X][Y]>length[x][y]+1 and matrix[X][Y]==1:
                length[X][Y] = length[x][y] + 1
                dq.append([X,Y,False])
                #이동한 좌표, 현재까지 걸린시간, 직전 오작교 아님
            if matrix[X][Y] <2:continue
            d = length[x][y]//matrix[X][Y]
            if matrix[X][Y]>1 and length[X][Y]>matrix[X][Y]*(d+1) and not v :
                length[X][Y] = matrix[X][Y] * (d + 1)
                dq.append([X,Y,True])
    # print(*length, sep = '\n')
    # print()


N, M = map(int,input().split())
matrix = [[1]*(N+2)]+[[1]+list(map(int,input().split()))+[1] for _ in range(N)]+[[1]*(N+2)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
INF = 200000000
mn = 200000000
for r in range(1,N+1):
    for c in range(1,N+1):
        if matrix[r][c] == 0 and \
                ((matrix[r+dx[0]][c+dx[0]] ==1 and matrix[r+dx[2]][c+dx[2]] ==1)\
                or(matrix[r+dx[1]][c+dx[1]] ==1 and matrix[r+dx[3]][c+dx[3]] ==1)):
            matrix[r][c] = M
            # print(*matrix,sep='\n')
            move()
            # print(mn)
            matrix[r][c] = 0
    # 오작교 하나 놓고 시작하기

print(mn)