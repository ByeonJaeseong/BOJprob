'''
시키는대로 구현을 해야함 -> 조심해서
구상 5분
'''
def check(x,y):
    return 0<=x<N and 0<=y<N
# 밖으로 나가는 것을 체크하기 위한 용도

def tonado():
    sx, sy = N//2, N//2
    ## 2n^2 일때는 밖으로 나감
    count = 1
    lst = []
    upper, lower = N//2, N//2
    out, d = 1, 0
    for i in range(1,N**2+1):
        if i == out**2:
            upper+=1
            lower-=1
            out +=2

        lst.append((sx,sy,d))
        if not (lower <= sx+dx[d] <= upper and lower <= sy+dy[d] <= upper):
            d = (d+1)%4
        sx +=dx[d]
        sy +=dy[d]

    return lst
# 토네이도 구현완료 14분





N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
tonado_lst = tonado()
dust0 = [(-1,0,0.07),(-1,-1,0.1),(-1,1,0.01),(-2,0,0.02),(0,-2,0.05),(1,0,0.07),(1,-1,0.1),(1,1,0.01),(2,0,0.02)]
dust1 = [(-i[1], i[0], i[2]) for i in dust0]
dust2 = [(-i[1], i[0], i[2]) for i in dust1]
dust3 = [(-i[1], i[0], i[2]) for i in dust2]
rule = []
rule.append(dust0+[(0,-1)])
rule.append(dust1+[(1,0)])
rule.append(dust2+[(0,1)])
rule.append(dust3+[(-1,0)])
#날려버릴 룰 만들기
count = 0
for i in range(1,N**2):
    x, y, d = tonado_lst[i]
    value = matrix[x][y]
    for j in range(9):
        X, Y =  x+rule[d][j][0], y+rule[d][j][1]
        blow = int(value*rule[d][j][2])
        matrix[x][y]-=blow
        # 날린 모래 빼주기
        if not check(X,Y):
            count+=blow
            continue
        #밖으로 나가면 밖으로 나간 모래 세주기
        matrix[X][Y]+=blow
        # 안에 남으면 더해주기
    p, q = rule[d][9]
    X, Y = x+p, y+q
    if not check(X,Y):
        # 밖으로 나가면
        count += matrix[x][y]
        matrix[x][y]=0
    else:
        matrix[X][Y]+=matrix[x][y]
        matrix[x][y]=0

    # print(*matrix, sep='\n')
    # print()
#구현 완료는 39분
#디버깅 시작, 값이 약간씩 크게나옴
#디버깅 완료 -> 인덱스 실수
print(count)
