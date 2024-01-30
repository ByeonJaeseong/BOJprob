import sys
sys.setrecursionlimit(100_000)

def check(x, y):
    global N
    global M
    return 0<=x<M and 0<=y<N

def dfs(x, y):
    global dx
    global dy
    global matrix
    global visit
    global count
    if not visit[x][y]:
        visit[x][y]=True
        # count+=1
        for i in range(4):
            X = x+dx[i]
            Y = y+dy[i]
            if check(X,Y) and matrix[X][Y]!=0 and not visit[X][Y]:
                dfs(X,Y)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

M, N = map(int, input().split())
# M 세로길이 #N 가로길이
count = 0
number = -1
matrix=[list(map(int, input().split())) for _ in range(M)]
# for i in range(M):
#     print(matrix[i])
# 전체가 0 이 되거나 또는 갯수가 2개 이상일 때 끊음
while sum([sum(matrix[i]) for i in range(M)]) :
    # print(sum([sum(matrix[i]) for i in range(M)]))
    number+=1 #
    count =0 # 몇개인지 셀 준비
    melting = [[0]*N for _ in range(M)]
    visit = [[False]*N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            if matrix[i][j]!=0 and not visit[i][j]:
                dfs(i,j) # 빙산 갯수 체크
                count+=1
                # print(count)
                # print("실행되었습니다")
                # for k in range(M):
                #     print(visit[k])
                # print()
    # print(count)

    if count>1:
        # print("빠져나왔습니다")
        break # 갯수가 2이상이면 나오기

    for i in range(1, M-1):
        for j in range(1, N-1): #가생이 제외
            for k in range(4):
                if matrix[i+dx[k]][j+dy[k]]==0:
                    melting[i][j]+=1 # 몇개 녹일 것인지 체크
    # for i in range(M):
    #     print(melting[i])
    for i in range(1, M - 1):
        for j in range(1, N - 1):  # 가생이 제외
            if matrix[i][j] != 0:
                if matrix[i][j]>=melting[i][j]:
                    matrix[i][j]-=melting[i][j]
                else:
                    matrix[i][j]=0
    #얼음 뽀개기
    # for i in range(M):
    #     print(matrix[i])

if not sum([sum(matrix[i]) for i in range(M)]):
    print(0)
else:
    print(number)