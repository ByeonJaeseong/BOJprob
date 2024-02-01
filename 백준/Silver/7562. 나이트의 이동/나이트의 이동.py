'''
3 TC
8 판 크기
0 0 시작점
7 0 움직이는 목표
'''

from collections import  deque

def check(x,y):
    global N
    return 0<=x<N and 0<=y<N

def bfs(xStart, yStart):
    global visit
    global length
    global xEnd
    global yEnd
    dq = deque()
    dq.append([xStart, yStart])
    visit[xStart][yStart] = True

    dx = [[1,2], [2,1], [-1,2],[2,-1], [1,-2],[-2,1],[-1,-2],[-2,-1]]
    while dq:
        value = dq.popleft()
        # print(len(dq))
        for i in range(8):
            X = value[0]+dx[i][0]
            Y = value[1]+dx[i][1]
            if check(X,Y) and not visit[X][Y] :
                visit[X][Y] = True
                dq.append([X,Y])
                length[X][Y] = length[value[0]][value[1]]+1
            if X== xEnd and Y ==yEnd:
                dq.clear()
                break
TC = int(input())
for X in range(TC):
    N = int(input()) # 체스판 사이즈
    visit = [[False]*N for _ in range(N)]
    length = [[0]*N for _ in range(N)]
    xStart, yStart = map(int, input().split())
    xEnd, yEnd = map(int, input().split())
    bfs(xStart,yStart)
    # for i in range(N):
    #     print(length[i])
    print(length[xEnd][yEnd])