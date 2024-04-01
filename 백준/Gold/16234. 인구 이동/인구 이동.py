'''
문제 시작 2시 52분
'''

from collections import deque

def check(x, y) : return 0<=x<N and 0<=y<N

N, MN, MX = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
time = 0
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
for t in range(1, 2001):
    marker = False
    new = [[-1]*N for _ in range(N)]
    visit = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if new[i][j] == -1 :
                count = 1
                sm = matrix[i][j]
                dq = deque()
                dq.append((i,j))
                visit[i][j] =True
                new_lst = [(i,j)]
                while dq:
                    p, q = dq.popleft()
                    for k in range(4):
                        X, Y = p+dx[k], q+dy[k]
                        if check(X,Y) and not visit[X][Y] and MN<=abs(matrix[X][Y] - matrix[p][q])<=MX:
                            new_lst.append((X,Y))
                            visit[X][Y] = True
                            count+=1
                            sm +=matrix[X][Y]
                            dq.append((X,Y))
                if count > 1 : marker =True
                # 인구 이동 일어났다고 체크
                while new_lst:
                    x, y = new_lst.pop()
                    new[x][y] = sm // count
    matrix = new
    if not marker: break
    time = t
print(time)
