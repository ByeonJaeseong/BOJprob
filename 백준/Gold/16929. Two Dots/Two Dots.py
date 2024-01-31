import sys
sys.setrecursionlimit(100_000)
'''아이디어
11
11 이런식으로 같은게 사각형을 이루고 있으면 무조건 참을 리턴을 해야한다.
만약에 이런게 하나도 없다 싶으면
회전 되는 것이 있나 확인을 해 보고 이게 영역을 2개로 나누면 패스
3개 이상으로 나누면 오케이를 하면 될 것 같다.
디민 이때 시간 복잡도가 문제가 될 수 있는데 그러한 문제를 방지하기 위하여
같은 색깔로 연결 되어 있으면 방문 리스트를 체크 하는 것이지
'''
def check(x,y):
    global M
    global N
    return 0<=x<M and 0<=y<N

def square(x, y, color):
    global matrix
    for i in range(2):
        for j in range(2):
            if matrix[x+i][y+j] != color: return False
    return True

def search(x,y, color):
    global visit
    global visited
    global matrix
    global M
    global N
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    if not visit[x][y]:
        visit[x][y]=True
        visited[x][y]=True
        for i in range(4):
            X = x+dx[i]
            Y = y+dy[i]
            if check(X,Y) and matrix[X][Y]== color and not visit[X][Y]:
                search(X,Y, color)
'''False가 몇개 구역인지를 파악'''

def search2(x,y):
    global visit
    global M
    global N
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    if not visit[x][y]:
        visit[x][y]=True
        for i in range(4):
            X = x+dx[i]
            Y = y+dy[i]
            if check(X,Y) and not visit[X][Y]:
                search2(X,Y)

def search3():
    global visit
    global M
    global N
    count = 0
    for i in range(M):
        for j in range(N):
            if not visit[i][j]:
                search2(i,j)
                count+=1
    return count

M, N = map(int,input().split()) #인풋 받기
matrix = ['-'*(N+2)]+["-"+input()+"-" for _ in range(M)]+['-'*(N+2)] #탐색 배열 받기
# print(matrix)
M, N = M+2, N+2
visited = [[False]*N for _ in range(M)] #이미 탐색 된 것들
marker = False
for i in range(1, M-1):
    for j in range(1, N-1):
        visit = [[False]*N for _ in range(M)] # 몇개로 나누어지는 지 체크용
        if i<M-1 and j < N-1 and square(i, j, matrix[i][j]): #사각형이면 참이다 하고 끊기
            # print(i, j, "실행되었습나디")
            marker=True
            break
        if not visited[i][j]: #한번도 탐색 안한거면
            search(i, j, matrix[i][j]) # 방문 안한 것만 방문하고 체크하기
        #
        # for k in range(M):
        #     print(visit[k])
        count = search3()
        '''여기서부터 이어서 하기 구역 구하고 나서 count 세서 판단하기'''
        # print(count)
        if count >1:
            marker = True
            break
    if marker:
        break

if marker:
    print("Yes")
else:
    print("No")