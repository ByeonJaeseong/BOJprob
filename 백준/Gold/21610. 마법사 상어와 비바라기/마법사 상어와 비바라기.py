'''
N번 행 다음은 1번 행
N번 열 다음은 1번 열
행렬의 값 - > 저장할 수 있는 물의 양
1. 모든 구름이 di 방향으로 si칸 이동한다.
2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
3. 구름이 모두 사라진다.
4. 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 물복사버그 마법을 사용하면, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
예를 들어, (N, 2)에서 인접한 대각선 칸은 (N-1, 1), (N-1, 3)이고, (N, N)에서 인접한 대각선 칸은 (N-1, N-1)뿐이다.
바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
문제 이해 + 구상 : 5분 -> 이친구도 빡구현으로 풀기러 함
'''
def check(x,y):
    return 0<=x<N and 0<=y<N
N, M = map(int, input().split())
#N은 매트릭스, M은 명령횟수
matrix = [list(map(int, input().split())) for _ in range(N)]
#물의 양
order = [list(map(int, input().split())) for _ in range(M)]
# di -> 팔방탐색, si -> 이동 칸 수
order = [[order[i][0]-1, order[i][1]] for i in range(M)]
# 인덱스 맞춰주기
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
cloud = [(N-2, 0), (N-1,0),(N-2,1),(N-1,1)]
#초기 구름 위치
for i in range(M):
    temp_cloud = []
    while cloud:
        x, y = cloud.pop()
        di, si = order[i]
        X = (x + dx[di] * si) % N
        Y = (y + dy[di] * si) % N
        temp_cloud.append((X,Y))
    # 이동한 구름 위치
    for j in range(len(temp_cloud)):
        x, y = temp_cloud[j]
        matrix[x][y]+=1
    # 비내려주기
    # print(*matrix, sep='\n')
    # print()
    for j in range(len(temp_cloud)):
        x,y = temp_cloud[j]
        temp = 0
        for k in [1,3,5,7]:
            X, Y = x+dx[k], y+dy[k]
            if check(X,Y) and matrix[X][Y]!=0:
                temp+=1
        matrix[x][y]+=temp
    temp_cloud = set(temp_cloud)
    # print(*matrix, sep='\n')
    # print()
    ## 대각선의 갯수중 0이 아닌데 세주기
    for j in range(N):
        for k in range(N):
            if (j, k) not in temp_cloud and matrix[j][k]>=2:
                cloud.append((j,k))
                matrix[j][k]-=2
    # print(*matrix, sep='\n')
    # print()
print(sum([sum(matrix[i]) for i in range(N)]))

