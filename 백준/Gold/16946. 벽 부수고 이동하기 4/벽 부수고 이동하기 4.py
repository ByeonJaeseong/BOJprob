import sys
from collections import deque
# input = sys.stdin.readline
def check(x,y):
    return 0<=x<M and 0<=y<N

def bfs(x,y):
    global visit
    count = 1

    dq =deque()
    dq.append((x,y))
    visit[x][y] =True
    walls = set([])
    while dq:
        p, q = dq.popleft()
        for i in range(4):
            X = p+dx[i]
            Y = q+dy[i]
            if check(X,Y) and not visit[X][Y] and matrix[X][Y] ==0:
                visit[X][Y]=True
                count+=1
                dq.append((X,Y))
            if check(X, Y) and matrix[X][Y] == 1:
                walls.add((X,Y))
    count = count%10
    while walls:
        x, y = walls.pop()
        result[x][y] +=count

M, N =map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
length = [[[] for _ in range(N)] for _ in range(M)]
visit = [[False] * N for _ in range(M)]
matrix = [list(map(int,input())) for _ in range(M)]
result = [[0]*N for _ in range(M)]
for i in range(M):
    for j in range(N):
        if matrix[i][j]==0 and not visit[i][j]:
            bfs(i,j)
            # print("실행")
# print(*visit,sep='\n')
for i in range(M):
    for j in range(N):
        # st = set([])
        if matrix[i][j]==1:
            # for k in range(4):
            #     X = i+dx[k]
            #     Y = j+dy[k]
            #     if check(X,Y) and length[X][Y] and length[X][Y][1] not in st:
            #         st.add(length[X][Y][1])
            #         result[i][j]+=length[X][Y][0]
            result[i][j]=(result[i][j]+1)%10
for i in range(M):
    print(*result[i],sep='')
# 어디서 시작한 애인지도 적어줘야함