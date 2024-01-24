from collections import deque

def check(x, y) :
    global M
    global N
    if 0<=x<M and 0<=y<N:
        return True
    else:
        return False
# 범위 체크
def search(x, y) :
    global matrix
    global dist
    global visit
    dx = [-1, 1, 0 , 0]
    dy = [0, 0, 1, -1]
    lst = deque()
    lst.append([x,y])

    visit[x][y]=True
    while len(lst)>0:
        lst2 = lst.pop()
        for i in range(4):
            X = lst2[0]+dx[i]
            Y = lst2[1]+dy[i]
            if check(X,Y):
                if matrix[X][Y]==1:
                    if dist[X][Y] == -1 and not visit[X][Y]: # 업데이트 해줘야 할 애들
                        visit[lst2[0]][lst2[1]]=True
                        dist[X][Y] = dist[lst2[0]][lst2[1]]+1
                        lst.appendleft([X,Y])
                    # elif dist[X][Y]>dist[lst2[0]][lst2[1]]+1:
                    #     dist[X][Y] = dist[lst2[0]][lst2[1]]+1
                    #     lst.append([X,Y])
                    #     print("실행되었습니다")
                    else:
                        continue
                else:
                    continue
            else:
                continue
        # print(len(lst))

M, N = map(int, input().split())
matrix =[list(map(int, input().split())) for _ in range(M)]
dist = [[-1]*N for _ in range(M)]
visit = [[False]*N for _ in range(M)]
for i in range(M):
    for j in range(N):
        if matrix[i][j]== 0 :
            dist[i][j]=0

for i in range(M):
    for j in range(N):
        if matrix[i][j]==2:
            dist[i][j]=0
            search(i, j)
            break

for i in range(M):
    for j in range(N):
        print(dist[i][j], end=" ")
    print()