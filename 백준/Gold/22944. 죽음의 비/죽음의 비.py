
from collections import deque

N, HP, D = map(int, input().split())
matrix = [list(input()) for _ in range(N)]

sx, sy = 0, 0
ex, ey = 0, 0
lst = []
visit = [[False]*N for _ in range(N)] #룩업 1
hp_ub = [[[] for _ in range(N)] for _ in range(N)] #룩업 2
length = [[1_000_001]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'S':
            sx, sy = i, j

        if matrix[i][j] == 'E':
            ex, ey = i, j

        if matrix[i][j] == 'U':
            lst.append([i,j])

# print(lst)
dq = deque()
dq.append([sx,sy])
visit[sx][sy]=True
length[sx][sy] = 0
hp_ub[sx][sy].extend([HP, 0]) # 처음 시작할 때 피통 채우기
while dq:
    sx, sy = dq.popleft()
    #종점으로 갈 수 있는지 체크하고 갈 수 있으면 가기
    if abs(sx-ex)+abs(sy-ey)<=sum(hp_ub[sx][sy]):
        length[ex][ey]=min(length[ex][ey],length[sx][sy]+abs(sx-ex)+abs(sy-ey))
        continue

    #종점으로 갈 수 없으면 우산 찾기
    for i in range(len(lst)):
        ux, uy = lst[i]
        #우산을 가지러 갈 수 있는 경우만
        if abs(sx-ux)+abs(sy-uy)<=sum(hp_ub[sx][sy]):
            if not visit[ux][uy]:
                #방문을 안한케이스는 그냥 방문하면 됨
                if hp_ub[sx][sy][1] >= abs(sx-ux)+abs(sy-uy):
                    hp_ub[ux][uy].extend([hp_ub[sx][sy][0], D-1])
                    dq.append([ux,uy])
                    visit[ux][uy]=True
                    length[ux][uy] = min(length[ux][uy], length[sx][sy]+abs(sx-ux)+abs(sy-uy))
                else:
                    hp_ub[ux][uy].extend([hp_ub[sx][sy][0]-(abs(sx-ux)+abs(sy-uy))+hp_ub[sx][sy][1]+1, D-1])
                    dq.append([ux, uy])
                    visit[ux][uy] = True
                    length[ux][uy] = min(length[ux][uy], length[sx][sy] + abs(sx - ux) + abs(sy - uy))
            else: # 방문을 한 경우는 피가 높은걸로 바꿔줘야함
                if hp_ub[sx][sy][1] >= abs(sx-ux)+abs(sy-uy) and hp_ub[sx][sy][0]>hp_ub[ux][uy][0]:
                    #우산으로 다 버틸수 있는 경우
                    hp_ub[ux][uy] = [hp_ub[sx][sy][0], D-1]
                    # 피는 그대로 유지하고 우산만 바꿈
                    dq.append([ux,uy])
                    length[ux][uy] = min(length[ux][uy], length[sx][sy]+abs(sx-ux)+abs(sy-uy))

                elif hp_ub[sx][sy][1] < abs(sx-ux)+abs(sy-uy) and hp_ub[sx][sy][0]>hp_ub[ux][uy][0]:
                    # 우산으로 다 못버티고 피를 써야하는 경우
                    hp_ub[ux][uy] = [max(hp_ub[sx][sy][0]-(abs(sx-ux)+abs(sy-uy))+hp_ub[sx][sy][1]+1, hp_ub[ux][uy][0]), D-1]
                    dq.append([ux, uy])
                    length[ux][uy] = min(length[ux][uy], length[sx][sy] + abs(sx - ux) + abs(sy - uy))
# for i in range(N):
#     print(hp_ub[i])
# print()
#
# for i in range(N):
#     print(length[i])

if length[ex][ey]==1_000_001:
    print(-1)
else:
    print(length[ex][ey])