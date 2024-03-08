'''
100*100
겉은 전부 0으로 둘러 싸기
'''
from collections import deque
def check(x,y):
    return 0<=x<M and 0<=y<N

def search(pivot):
    global visit
    for i in range(M):
        for j in range(N):
            if matrix[i][j]>=pivot:
                visit[i][j]=True
## 벽세우기
def water(n,m,pivot):
    global visit, count
    dq =deque()
    dq.append([n,m])
    visit[n][m]=True
    temp = 1
    marker = False
    while dq:
        value = dq.popleft()
        for i in range(4):
            X=value[0]+dx[i]
            Y=value[1]+dy[i]
            if not check(X,Y) :
                marker=True
            if check(X,Y) and not visit[X][Y]:
                temp+=1
                visit[X][Y]=True
                dq.append([X,Y])
    if marker:
        return 0
    else:
        return temp



## 고일 수 있는 물 채우기

M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
# 0으로 둘러 쌈
# print(*matrix,sep='\n')
mx = max([max(matrix[i]) for i in range(M)])
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
count = 0
for k in range(1,mx+1):
    visit = [[False]*(N) for _ in range(M)]
    search(k)
    # print(*visit,sep='\n')
    # print()
    for i in range(M):
        for j in range(N):
            if visit[i][j]: continue
            # 벽이면 넘어가기
            # print(i,j,k)
            count+=water(i,j,k)
            # print(*visit, sep='\n')
            # print()

print(count)