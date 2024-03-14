def check(x,y):
    return 0<=x<M and 0<=y<N

M, N = map(int, input().split())
# size of room
R, C, D = map(int, input().split())
# start Row, Column, Direction
ruleA = [list(map(int, input())) for _ in range(M)]
# rule for not cleaned room
ruleB = [list(map(int, input())) for _ in range(M)]
# role for cleaned room
room = [[1]*N for _ in range(M)]
visit = [[0]*N for _ in range(M)]

# set not cleaned room
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
#시계방향 회전
result = 0
count = 0
loc1x = 0
loc1y = 0
while True:
    marker = False
    if room[R][C]==1:
        marker = True
        room[R][C]=0
        count=0
        loc1x = R
        loc1y = C
        visit =  [[0]*N for _ in range(M)]
    else:
        if visit[R][C]>-4:
            visit[R][C]-=1
            count +=1
        else:
            break

    if marker:
        #제거한 경우
        D=(D+ruleA[R][C])%4
    else:
        D = (D + ruleB[R][C]) %4


    #이동시키기
    R = R+dx[D]
    C = C+dy[D]
    result+=1
    if not check(R,C):
        break




print(result-count)



