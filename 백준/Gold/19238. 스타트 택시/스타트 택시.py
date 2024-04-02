'''
자주본 유형
이해끝 -> 4분
승객을 고르는 순서 -> BFS상 최단 거리 -> 같으면 행 적은 순 -> 크면 열 적은 순
?? 캐슬디펜스다?
400 탐색 시간 400
별로 안걸리네요
같은 위치에 있으면 최단 경로 0
태우고**** 이동한 연료양의 *2만큼 충전
'''
from collections import deque
def check(x,y):
    return 0<=x<N and 0<=y<N

# 태울 승객 찾기
def passenger(sx, sy):
    dq = deque()
    lst = []
    if (sx,sy) in location_set:
        # 택시가 고객과 같이 있으면
        lst.append((0,sx,sy))
        # 이미 최단거리 찾음
        return (0,sx,sy)
    visit = [[False]*N for _ in range(N)]
    dq.append((sx,sy, 0))
    mn = INF
    visit[sx][sy] = True
    # print(location_set)
    while dq:
        vx, vy, d = dq.popleft()
        for i in range(4):

            X = vx+dx[i]
            Y = vy+dy[i]
            if check(X,Y) and not visit[X][Y] and matrix[X][Y]==0 and mn>=d+1:
                if (X,Y) in location_set:
                    lst.append((d+1,X,Y))
                    visit[X][Y]=True
                else:
                    visit[X][Y]=True
                    dq.append((X,Y,d+1))
    # print(lst)
    if lst:
        lst.sort()
        return (lst[0][0], lst[0][1], lst[0][2])
    else: return (INF, INF, INF)

# 태울 승객 찾기
def arrival(sx, sy):
    dq = deque()
    lst = []
    if (sx,sy) in destination and destination[(sx,sy)] == (sx,sy):
        return (0, sx, sy)
    visit = [[False]*N for _ in range(N)]
    dq.append((sx,sy, 0))
    mn = INF
    visit[sx][sy] = True
    desx, desy =  destination[(sx,sy)]
    while dq:
        vx, vy, d = dq.popleft()
        for i in range(4):
            X = vx+dx[i]
            Y = vy+dy[i]
            if check(X,Y) and not visit[X][Y] and matrix[X][Y]==0:
                if (desx, desy) == (X,Y):
                    return (d+1, desx, desy)
                else:
                    visit[X][Y]=True
                    dq.append((X,Y,d+1))
    return (INF, INF, INF)
# 손님 목적지가 엉뚱할때

N, M, fuel = map(int, input().split())
# 배열사이즈, 승객수, 연료양
INF = 2_000_000_000
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
matrix =[list(map(int, input().split())) for _ in range(N)]
sx, sy = map(int, input().split())
sx, sy = sx-1, sy-1
location = [list(map(int, input().split())) for _ in range(M)]
# 승객 위치 받기
destination = dict()
location_set = set([])
# 배열 받기 완료
for i in range(M):
    x, y, ddx, ddy = location[i]
    location_set.add((x-1, y-1))
    destination[(x-1,y-1)] = (ddx-1, ddy-1)
# print(location_set)
# print(destination)

marker = True
for _ in range(M):
    f, sx, sy = passenger(sx, sy)
    if f == INF:
        marker = False
        break
        # 손님을 태울 수 없는 경우
    fuel -= f
    if fuel<0:
        marker = False
        # 기름 바닥나면 끝내기
        break
    # 손님을 태우는데 까지 든 연료
    ssx, ssy= sx, sy
    # 태울 손님 리스트에서 지우기
    f, sx, sy = arrival(sx, sy)
    location_set.remove((ssx, ssy))
    destination.pop((ssx,ssy))
    # 손님 태우고 도착지로 가기
    if f == INF:
        marker = False
        break
    # 손님이 갈 수 없는데로 가달라 하는 경우
    fuel -=f
    if fuel < 0:
        marker = False
        # 기름 바닥나면 끝내기
        break
    fuel += f*2
    # 잘 도착했으면 기름 업데이트
if marker:
    print(fuel)
else:
    print(-1)

