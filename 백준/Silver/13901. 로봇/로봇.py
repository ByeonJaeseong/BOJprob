'''
규칙은 밑에 주어짐
3 3 # 판의 크기
1 # 장애물의 개수
1 0 # 장애물의 위칠
1 1 # 시작 위치
1 2 3 4 # 규칙 1 위 2 아래 3 왼쪽 4 오른쪽
방문한 지역,
장애물을 만날 경우 로봇은 사용자가 지정한
다음 방향으로 움직인다.
'''
def check(x,y):
    return 0<=x<M and 0<=y<N and not visit[x][y]
M, N = map(int, input().split())
D=0
visit = [[False]*N for _ in range(M)]
Block = int(input())
block = [list(map(int, input().split())) for _ in range(Block)]
# block 위치
for i in range(Block):
    visit[block[i][0]][block[i][1]] = True
# 장애물 못가는 데 처리
sx, sy = map(int, input().split())
visit[sx][sy] = True
dir = {1 : [-1, 0], 2: [1, 0], 3:[0, -1], 4:[0, 1]}
rule = list(map(int, input().split()))
# print(rule)
D=0
while True:
    marker = True
    X, Y= sx + dir[rule[D]][0], sy + dir[rule[D]][1]
    if check(X,Y):
        #앞으로 갈 수 있으면
        visit[X][Y]=True
        sx, sy = X, Y
        # 계속 앞으로 간다
        continue
    for _ in range(1, 4):
        D = (D+1)%4
        X, Y = sx + dir[rule[D]][0], sy + dir[rule[D]][1]
        if check(X, Y):
            # 앞으로 갈 수 있으면
            visit[X][Y] = True
            sx, sy = X, Y
            marker = False
            break
    if marker: break
# for i in range(M):
#     print(visit[i])
print(sx, sy)