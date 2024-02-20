'''
M, N , P -> 좌표 개수, 플레이어 수
토탈 시간 1000*1000*26=26_000_000
도착하고 빨리 도착한 순으로 뚜까패기
최소시간을 시작시간으로 잡고 뚜까기인데
다 도착하는데 걸리는 시간이 워스트 1999이므로 그냥 탐색도
문제없음
'''

from collections import deque

def check(x,y):
    return 0<=x<M and 0<=y<N

def bfs(x,y):
    global matrix, M, N, mx, my
    visit = [[False]*N for _ in range(M)]
    length = [[0]*N for _ in range(M)]
    dq = deque()
    dq.append([x,y])
    visit[x][y]=True
    while dq:
        value = dq.popleft()
        marker = False
        for i in range(4):
            X = value[0] + dx[i]
            Y = value[1] + dy[i]
            if check(X,Y) and matrix[X][Y]!='X' and not visit[X][Y]:
                length[X][Y] = length[value[0]][value[1]]+1
                dq.append([X,Y])
                visit[X][Y] = True
                if X == mx and Y==my:
                    marker = True
                    # print("실행되었습니다")
                    break
        if marker:
            break
    # for i in range(M):
    #     print(length[i])
    # print()
    return length[mx][my]


M, N, P = map(int, input().split())
matrix = [list(input()) for _ in range(M)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
loc = [[] for _ in range(P)]
# 사람들의 위치를 정할 location
dic = {k:v for v,k in enumerate('abcdefghijklmnopqrstuvwxyz')}
dic2 = {v:k for v,k in enumerate('abcdefghijklmnopqrstuvwxyz')}
power = [list(input().split()) for _ in range(P)]
dic3 = {k:int(v) for k,v in power}
hp = int(input())
# print(dic3)
# print(dic)
# print(dic2)
mx, my = 0, 0
for i in range(M):
    for j in range(N):
        if matrix[i][j] =='.':
            continue
        elif matrix[i][j]=='B':
            mx, my = i, j
        elif matrix[i][j]=='X':
            continue
        else:
            loc[dic[matrix[i][j]]].extend([i,j])
# print(loc)
# print(mx,my)
monster_length = []
for i in range(P):
    length = bfs(loc[i][0], loc[i][1])
    if length == 0:
        continue
    monster_length.append([length, matrix[loc[i][0]][loc[i][1]]])
monster_length.sort()
monster_length.append([1000000000, monster_length[-1][1]])
# print(monster_length)
start =monster_length[0][0]
sum = 0
result = 0
# print(monster_length)
for i in range(len(monster_length)):
    if start == monster_length[i][0]:
        sum += dic3[monster_length[i][1]]
    else:
        hp -= sum*(monster_length[i][0]-start)
        if hp<=0:
            break
        start = monster_length[i][0]
        sum += dic3[monster_length[i][1]]
    # print(start, hp, sum)
    result = i+1
print(result)