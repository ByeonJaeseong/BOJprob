'''
문제 이해 4분
어제 푼 문제와 비슷
상어가 두마리 있을 수 있지만 실제로 남는건 큰 상어 밖에 없음
R, C, M
r,c,s,d,z -> 위치, 속력, 방향, 크기
크기 다 다름
구상 3분

상어는 입력으로 주어진 속도로 이동하고, 속도의 단위는 칸/초이다.
상어가 이동하려고 하는 칸이 격자판의 경계를 넘는 경우에는 방향을 반대로
 바꿔서 속력을 유지한채로 이동한다.

첫 제출  :시작후 35분 후 틀렸습니다

시키는대로 전부구현이 됐고, 문제의 주어진 조건과 일치하기때문에 로직적인 결함은 아닌걸로 판단

10시 27분 ~10시 29분 리프레쉬 하고옴
11시 2분 2차 제출 틀림
3차 제출 고친 부분에서 오타를 냈음
'''
def switch(d):
    if d == 0 : return 1
    if d == 1 : return 0
    if d == 2 : return 3
    if d == 3 : return 2

def check(x,y):
    return 0<=x<M and 0<=y<N


M, N, K = map(int, input().split())
# R,C, 상어 갯수
matrix = [[0]*N for _ in range(M)]
dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)
shar = [list(map(int, input().split())) for _ in range(K)]
shar = [(i[0]-1, i[1]-1, i[2], i[3]-1, i[4]) for i in shar]
# print(*shar,sep='\n')
# 위치 r,c 속도 방향 크기
shark_loc = dict()
for i in range(K):
    shark_loc[shar[i][4]] = shar[i]
    matrix[shar[i][0]][shar[i][1]] = shar[i][4]
score = 0
for j in range(N):
    # 1번 오른쪽 한칸 이동된 상태에서 시작
    # print(shark_loc)
    for i in range(M):
        if matrix[i][j]!=0:
            score += matrix[i][j]
            # print(i, matrix[i][j], "잡았다")
            shark_loc.pop(matrix[i][j])
            # 상어 먹혔으니 지우기
            matrix[i][j]=0
            break
    # 상어 사라지기
    new = [[0]*N for _ in range(M)]
    keys = list(shark_loc.keys())
    for t in keys:
        x, y, s, d, z = shark_loc[t]
        X = x
        Y = y
        temp = 0
        if d == 0 or d == 1:
            temp = s%(2*(M-1))
        else:
            temp = s%(2*(N-1))

        for _ in range(temp):
            X = X+dx[d]
            Y = Y+dy[d]
            if check(X,Y): continue
            d = switch(d)
            X = X+dx[d]*2
            Y = Y+dy[d]*2
        if new[X][Y]<z:
            if new[X][Y] !=0:
                shark_loc.pop(new[X][Y])
            new[X][Y]=z
            shark_loc[z] = (X,Y,s,d,z)
        else:
            shark_loc.pop(z)
    # print(shark_loc)
    matrix = new
    # print(*matrix, sep='\n')
    # print()
# print(*matrix, sep='\n')
# print()
print(score)

