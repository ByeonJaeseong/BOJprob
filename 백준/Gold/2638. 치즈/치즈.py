'''아이디어를 생각하면
일단 우선은 밖에 공기가 되는 부분을 먼저 체크하면 될 것 같아.
그 다음에 밖에 있는 치즈를 녹이고
그 다음에 다시 탐색
그리고 나서 다시 치즈 녹이기를 반복하면 될듯?
그렇게 되면 일단 한 번 탐색을 하는데 10000번 연산이 필요하니까
그 다음은 연산 시간에 대하여 크게 부담감을 갖을 필요는 없을 것 같은 느낌
'''

from collections import deque

def search(x, y):
    global visit
    global matrix
    global dx
    global dy

    dq = deque()
    dq.appendleft([x,y])
    while dq :
        loc = dq.pop()
        visit[loc[0]][loc[1]]=True
        for i in range(4):
            X = loc[0]+dx[i]
            Y = loc[1]+dy[i]
            if not visit[X][Y] and matrix[X][Y] == 0:
                visit[X][Y] = True
                dq.appendleft([X,Y])
    ## 방문하면 안될 것들 체크해서 값을 집어 넣고
    ## 여기서 생각해봐야 할 것은 매번 새로 visit 배열을 만들어서 해도 될것인가?
    ## 그리고 문제점이 반드시 공기가 이어져 있지도 않다고 생각했는데 맨 가장자리에는 놓여 있지 않으니까
    ## 그런걱정은 상대적으로 덜해도 될듯
    ## 바깥 공기를 체크한 다음에 그 다음에 지속적으로 업데이트?
    ## 아이디어 자체는 사라지는 공간에 대해서 계속 search 를 해주면 될듯?
    ## 못없애는 경우는 없음

M, N = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visit = [[False]*N for _ in range(M)]
matrix = [list(map(int, input().split())) for _ in range(M)]
count =0
search(0,0) # 초기값 셋팅하자
cheeze = []
# print(matrix)

while sum([sum(x) for x in matrix])!=0:
    # print(matrix.count(0))
    temp = 0
    for i in range(M):
        for j in range(N):
            if matrix[i][j]==1:
                for k in range(4):
                    if visit[i+dx[k]][j+dy[k]]: #주변에 공기와 접하는부분
                        temp+=1
                    if temp >=2:
                        cheeze.append([i,j])
                        break
                    ## 녹는 치즈 탐색
                temp=0 # 다음 치즈 탐색
    # print(cheeze)
    for i in cheeze:
        # print(i[0], i[1])
        matrix[i[0]][i[1]] = 0
    # 치즈녹이기
    for i in cheeze:
        search(i[0], i[1])
    count +=1
    cheeze=[]
print(count)
