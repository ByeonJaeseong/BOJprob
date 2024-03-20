'''
37분부터 문제읽기 시작
문제가 길고 복잡함 +  오늘도 백준의 문제는 매우 모호하다
문제 구현 시작 46분
각 온풍기마다 visit 배열을 써서 관리를 하기러 함

10시 19분 잠깐 쉼 -> 그냥 힘들어서 쉰거임
'''

from collections import deque

def check(x,y) : return 0<=x<M and 0<=y<N

def heat(d, x, y):
    ## 1번로직 구현
    global temperature
    visit = [[False]*N for _ in range(M)]
    if d in [2, 3]:
        # 위 아래로 움직이는 경우
        # 히터와 공간사이에 벽이 없다면
        dq = deque()
        if check(x+dx[d], y+dy[d]) and (x, y, x+dx[d], y+dy[d]):
            dq.append((x+dx[d], y+dy[d], 5))
            temperature[x+dx[d]][y+dy[d]] +=5
            visit[x+dx[d]][y+dy[d]] = True

        while dq:
            vx, vy, t = dq.popleft()
            if t == 0: break
            # 조금 비효율적이지만 메모리가 넉넉하니
            for i in range(-1, 2):

                X, Y = vx+dx[d], vy+i
                # 체크를 해줄건데
                if check(X,Y) and (vx,vy,vx,Y) not in wall_set and (vx,Y, X,Y) not in wall_set and not visit[X][Y] and t>1:
                    # 1번 안에 있는지, 2번 벽이 아닌지, 이번에 방문 안했는지, 넘겨줄 온도가 남았는지
                    dq.append((X,Y,t-1))
                    temperature[X][Y]+=(t-1)
                    visit[X][Y]=True
    else:
        # 양 옆으로 움직이는 경우
        # 히터와 공간사이에 벽이 없다면
        dq = deque()
        # print(dx, d)
        if (x, y, x+dx[d], y+dy[d]):
            dq.append((x+dx[d], y+dy[d], 5))
            temperature[x+dx[d]][y+dy[d]] +=5
            visit[x+dx[d]][y+dy[d]] = True

        while dq:
            vx, vy, t = dq.popleft()
            if t == 0: break
            # 조금 비효율적이지만 메모리가 넉넉하니
            for i in range(-1, 2):
                X, Y = vx+i, vy+dy[d]
                # 체크를 해줄건데
                if check(X,Y) and (vx,vy,X,vy) not in wall_set and (X,vy,X,Y) not in wall_set and not visit[X][Y] and t>1:
                    # 1번 안에 있는지, 2번 벽이 아닌지, 이번에 방문 안했는지, 넘겨줄 온도가 남았는지
                    dq.append((X,Y,t-1))
                    temperature[X][Y]+=(t-1)
                    visit[X][Y]=True
######################### 1번 로직 구현 끝 ##########################################################


def regulize():
    global temperature
    lst = []
    for i in range(M):
        for j in range(N):
            for k in range(4):
                X = i + dx[k]
                Y = j + dy[k]
                if check(X,Y) and (i,j,X,Y) not in wall_set and temperature[X][Y]<temperature[i][j]:
                    # 벽에 안가로 막혀 있고 나보다 작은 애만 나눠줌
                    v = (temperature[i][j]-temperature[X][Y])//4
                    lst.append((i,j,-v))
                    lst.append((X,Y,v))
    # print(lst)
    while lst:
        x, y, v = lst.pop()
        temperature[x][y]+=v


M, N, K = map(int, input().split())
#방 사이즈, 온도
room = [list(map(int, input().split())) for _ in range(M)]
W = int(input())
# 벽 갯수
wall = [list(map(int, input().split())) for _ in range(W)]
temperature = [[0]*N for _ in range(M)]
wall = [(w[0]-1, w[1]-1, w[2]) for w in wall]
# 0인 경우 x,y와 x-1,y 사이의 벽 1인 경우 x,y 와 x,y+1 사이의 벽
wall_set = set({})
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)
for w in wall:
    x,y,d = w
    if d ==0:
        wall_set.add((x, y, x - 1, y))
        wall_set.add((x - 1, y, x, y))
    if d ==1:
        wall_set.add((x, y, x, y + 1))
        wall_set.add((x,  y+ 1, x, y))
# 벽이 있는지는 셋을 통해서 확인하면서 갑시다
# 메모리가 넉넉하니 온풍기 전부 배열로 잡아놓고 시작
heater = []
t_search = []
for i in range(M):
    for j in range(N):
        if room[i][j] in [1,2,3,4]:
            heater.append((room[i][j]-1, i, j))
            # 히터의 위치 찾아주기
        if room[i][j] == 5:
            t_search.append((i, j))
            # 히터의 위치 찾아주기
count = 0
for _ in range(101):
    # 정확히 100번 실행하기
    ######## 1번 로직 구현 시작 #############
    for h in heater:
        hd, hx, hy = h
        heat(hd, hx, hy)
    ################# 1번 끝 #################
    # print(*temperature, sep='\n')
    # print()
    regulize()
    ############# 2번 끝 ##################
    for j in range(N):
        if temperature[0][j] >0:
            temperature[0][j]-=1
        if temperature[M-1][j] >0:
            temperature[M-1][j]-=1
    for i in range(1,M-1):
        for j in [0, N-1]:
            if temperature[i][j] > 0:
                temperature[i][j] -= 1
    ############### 3번 끝#####################
    count+=1
    ############### 4번 끝 ##################
    # print(*temperature, sep='\n')
    # print()
    marker = True
    for ts in t_search:
        tx, ty = ts
        if temperature[tx][ty]<K:
            marker = False
            break
    if marker:
        break


if count>100:
    print(count)
else:
    print(count)
