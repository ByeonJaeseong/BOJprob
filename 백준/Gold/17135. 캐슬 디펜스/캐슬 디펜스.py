'''
M,N,D -> 격자판 사이즈와 Distance
N+1 칸 궁수 배치가능
'''
from collections import deque
def check(x,y):
    return 0<=x<M and 0<=y<N

def search(x, y):
    dq = deque()
    dq.append([x,y])
    locx, locy = 0 ,0
    visit = [[False]*N for _ in range(M)]
    marker = False
    while dq and not marker:
        value = dq.popleft()
        for i in range(3):
            X = value[0]+dx[i]
            Y = value[1]+dy[i]
            if check(X,Y) and  not visit[X][Y] and temp_matrix[X][Y] == 0 and (abs(x-X)+abs(y-Y))<D:
                visit[X][Y]=True
                dq.append([X,Y])
            elif check(X,Y) and temp_matrix[X][Y]==1 and (abs(x-X)+abs(y-Y))<=D:
                locx, locy = X, Y
                marker=True
                break
    if marker:
        return (locx,locy)
    else:
        return ()


M, N, D= map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
loc = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            loc.append((i, j, k))
dx = [0, -1, 0]
dy = [-1, 0, 1]
count = 0
for x in loc:
    # location (M, x[0]), (M, x[1]), (M, x[2])
    kill = []
    temp_matrix = [x[:] for x in matrix]
    temp_count = 0
    # print(x)
    while sum([sum(temp_matrix[i]) for i in range(M)]):
        # 다 없어 질때까지
        for i in range(3):
            kill.append(search(M, x[i]))
            #죽일 애 찾기
        # print(*temp_matrix,sep="\n")
        # print(kill)
        # print()
        while kill:
            kloc = kill.pop()

            if len(kloc)>0:
                if temp_matrix[kloc[0]][kloc[1]]==1:
                    temp_matrix[kloc[0]][kloc[1]]=0
                    temp_count+=1
                # 죽일애 있으면 죽이기(이미 죽였으면 스킵)
        for i in range(1, M):
            for j in range(N):
                temp_matrix[M-i][j] = temp_matrix[M-1-i][j]
                # 한칸씩 옮기기
        for i in range(N):
            temp_matrix[0][i]=0
        # 첫번째 칸 비워주기
        count = max(count,temp_count)
print(count)
