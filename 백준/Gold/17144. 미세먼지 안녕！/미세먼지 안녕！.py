'''
1초 동안 아래 적힌 일이 순서대로 일어난다.

1.미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
    (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
    인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
    확산되는 양은 Ar,c/5이고 소수점은 버린다. 즉, ⌊Ar,c/5⌋이다.
    (r, c)에 남은 미세먼지의 양은 Ar,c - ⌊Ar,c/5⌋×(확산된 방향의 개수) 이다.
2공기청정기가 작동한다.
    공기청정기에서는 바람이 나온다.
    위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
    바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
    공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.

구상 하는데는 문제 이해하고 풀이 들어가는데에는 3~4분
구현 구상하는데 보니 골드 3난이도라 생각하고 풀면 될듯?
팬시하게 구상해볼까 하다가 좀 실수할 수 있을 것 같아서 그냥 빡구현 모드 결정

구현하는데 걸린시간 40분 총 구상시간 5분
중간에 추가적으로 구상한 시간 5분정도 추가
개인적으로 문제를 풀면서 방만하게 약간 구상을 했다라는 생각을 많이 한 문제였습니다.
구상한 방식이 시간적으로 맞나 라는 생각은 들었지만 이렇게 구상을 안하면 중간에 틀릴 수 있을 것이라는 생각이들어
일단 선 구현 후 디버깅을 할 것을 목적으로 빡구현을 했고 시간이 아슬아슬하게 통과된 느낌입니다
체감 난이도는 골드 3정도라 생각했는데 실제난이도는 골드 4인 것을 보니 컨디션 관리에 좀 신경을 써야되는 시기구나 라는 생각이 들었습니다.
그리고 일단 옆에 앉아 계신 유경프로님이 2등으로 같이 제출한 것에 대해 매우 흡족함을 느끼고 있는 시간입니다.
'''
def check(x,y):
    return 0<=x<M and 0<=y<N

def check_upper(x,y):
    return 0<=x<=upper and 0<=y<N

def check_lower(x,y):
    return lower<=x<M and 0<=y<N


def dusk(x,y):
    count = 0
    value = matrix[x][y]//5
    for i in range(4):
        X = x+dx[i]
        Y = y+dy[i]
        if check(X,Y) and matrix[X][Y]!=-1:
            #공간이 있고 공청기 없으면 퍼뜨리기
            exten.append([X,Y,value])
            count+=1
    # 탐색했고
    # 남은량 계산
    matrix[x][y]=matrix[x][y]-count*value

def cleaner():
    #위쪽으로 가는거 시작
    locx, locy =upper_cleaner
    locx-=1
    matrix[locx][locy]=0
    d = 0
    while True:
        X,Y = locx+dx[d], locy+dy[d]
        if not check_upper(X,Y):
            d = d+1
            # 끝에가면 방향만 바꿔줌
            continue
        if matrix[X][Y]==-1:break
        matrix[locx][locy] = matrix[X][Y]
        matrix[X][Y] = 0
        locx, locy = X,Y
        #한칸씩 당겨줌

    #아래쪽으로 가는거
    locx, locy =lower_cleaner
    locx+=1
    matrix[locx][locy]=0
    d = 2
    while True:
        X,Y = locx+dx[d], locy+dy[d]
        if not check_lower(X,Y):
            d = d-1
            # 끝에가면 방향만 바꿔줌
            continue
        if matrix[X][Y]==-1: break
        matrix[locx][locy] = matrix[X][Y]
        matrix[X][Y] = 0
        locx, locy =  X,Y
        #한칸씩 당겨줌


M, N, T = map(int, input().split())
# 행, 렬, 시간
matrix = [list(map(int, input().split())) for _ in range(M)]
# print(*matrix,sep='\n')
# print()
exten = []
upper, lower = 0, 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(M):
    if matrix[i][0] == -1:
        upper = i
        lower = i+1
        break
upper_cleaner = (upper, 0)
lower_cleaner = (lower, 0)
# print(upper_cleaner)
# print(lower_cleaner)
for _ in range(T):
    for i in range(M):
        for j in range(N):
            if matrix[i][j]>0:
                dusk(i,j)
    while exten:
        x, y, v =exten.pop()
        matrix[x][y]+=v
    cleaner()
# print(*matrix,sep='\n')
print(sum([sum(matrix[i]) for i in range(M)])+2)