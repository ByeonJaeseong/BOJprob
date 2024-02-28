'''
아이디어 4개 붙어 있으면 합 최대 갱신 끝

## 1번째 틀림
1. 아이디어 구상이 잘못됨 -> 중간에서 끊고 들어가는 파트들이 없음 예를 들어 ㅏ, ㅓ 이런 모양이 구현이 안되었음
2. 이거 칠공주에서 했던 잘못을 똑같이 재현한 문제

## 2번째 틀림
1. 말이 안되는 오류가 나왔는데 값이 정답보다 크게 나왔다.
2. 이건 아마도 로직에서 값을 어디를 잘못 추가했을 확률이 높아보이는데 디버깅이 쉽지 않다

##
말도안되는 실수를 했다는 것을 깨닳앗다.
시간을 너무 많이 쓰이길래 뭔가 했더니, 초기에 값을 셋팅을 안하고 넘겨준 문제가 있었다
전형적으로 마음 급하게 짰을때 내는 에러라고 생각이 되는데 아..... 문제 조건을 자꾸 잘 못 세팅하는 문제가 생긴다.
'''
def check(x,y):
    return 0<=x<M and 0<=y<N

def tet(n, sum, loc=[]):
    global mx, visit
    if n==4:
        mx = max(mx, sum)
        # if sum == 3942:
        #     print(loc)
        return
    for i in range(4):
        X = loc[0] + dx[i]
        Y = loc[1] + dy[i]
        if check(X,Y) and not visit[X][Y]:
            visit[X][Y] = True
            tet(n+1,sum+matrix[X][Y],[X,Y])
            visit[X][Y] = False
    x = loc[0]
    y = loc[1]
    if n <= 2:
        if check(x+1, y) and check(x, y+1) and not visit[x+1][y] and not visit[x][y+1]:
            visit[x+1][y] = True
            visit[x][y+1] = True
            tet(n+2, sum+matrix[x+1][y]+matrix[x][y+1], [x+1, y])
            tet(n + 2, sum + matrix[x + 1][y] + matrix[x][y + 1], [x , y+1])
            visit[x + 1][y] = False
            visit[x][y + 1] = False

        if check(x+1, y) and check(x, y-1) and not visit[x+1][y] and not visit[x][y-1]:
            visit[x+1][y] = True
            visit[x][y-1] = True
            tet(n+2, sum+matrix[x+1][y]+matrix[x][y-1], [x+1, y])
            tet(n + 2, sum + matrix[x + 1][y] + matrix[x][y - 1], [x , y-1])
            visit[x + 1][y] = False
            visit[x][y - 1] = False

        if check(x, y+1) and check(x, y-1) and not visit[x][y+1] and not visit[x][y-1]:
            visit[x][y+1] = True
            visit[x][y-1] = True
            tet(n+2, sum+matrix[x][y+1]+matrix[x][y-1], [x, y+1])
            tet(n + 2, sum + matrix[x][y+1] + matrix[x][y - 1], [x , y-1])
            visit[x][y+1] = False
            visit[x][y - 1] = False

M, N = map(int, input().split())
matrix =  [list(map(int, input().split())) for _ in range(M)]
visit = [[False]*N for _ in range(M)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
mx = 0
# print(*matrix, sep='\n')
for i in range(M):
    for j in range(N):
        visit[i][j]=True
        tet(1,matrix[i][j],[i,j])
print(mx)
