'''
시작 4시 49분
냄새 남기는 문제
'''

def check(x,y) : return 0<=x<N and 0<=y<N

N, M, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
rule = [[[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]]
dir = list(map(int, input().split()))
dir = [0] + [d-1 for d in dir]
smell = [[(0,0)]*N for _ in range(N)]
location = [(0,0)]*(M+1)
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 0 : continue
        location[matrix[i][j]] = (i,j)
# print(*dir)
# print(*location)
for _ in range(M):
    temp_rule = [list(map(int, input().split())) for _ in range(4)]
    temp_rule = [[t[0]-1, t[1]-1, t[2]-1, t[3]-1] for t in temp_rule]
    rule.append(temp_rule)
# print(*rule, sep='\n')
time = 0
for i in range(1, M + 1):
    x, y = location[i]
    smell[x][y] = (K, i)
# 자기자리에 냄새 뿌리기
for t in range(1, 1002):
    time = t
    for i in range(N):
        for j in range(N):
            matrix[i][j] = 0
    for i in range(1, M+1):
        marker = False
        x, y = location[-i]
        if (x,y) == (-1, -1): continue
        # 역순으로 넣을거임
        for j in range(4):
            d = rule[-i][dir[-i]][j]
            X, Y = x+dx[d], y+dy[d]
            if check(X,Y) and smell[X][Y][0] == 0:
                if matrix[X][Y] == 0:
                    matrix[X][Y] = M - i + 1
                    location[-i] = (X,Y)
                    dir[-i] = d
                else:
                    location[matrix[X][Y]] = (-1,-1)
                    matrix[X][Y] = M-i+1
                    # 쫓아내기
                    location[-i] = (X, Y)
                    dir[-i] =d
                marker = True
                break
        if not marker:
            for j in range(4):
                d = rule[-i][dir[-i]][j]
                X, Y = x + dx[d], y + dy[d]
                if check(X,Y) and smell[X][Y][1] == M-i+1:

                    location[-i] = (X, Y)
                    matrix[x][y] = 0
                    matrix[X][Y] = M-i+1
                    dir[-i] =d
                    break
        # 상어 다 옮김
    for i in range(1,M+1):
        x, y = location[i]
        if (x,y) == (-1, -1) : continue
        smell[x][y] = (K+1,i)
    # 자기자리에 냄새 뿌리기

    for i in range(N):
        for j in range(N):
            if smell[i][j] == (0, 0): continue
            x, y = smell[i][j]
            if x == 1:
                smell[i][j] = (0, 0)
                continue
            smell[i][j] = (x-1, y)
    #
    # print(*matrix, sep='\n')
    # print(*location)
    # print("냄새")
    # print(*smell, sep='\n')
    # print()


    if sum([sum(m) for m in matrix]) == 1: break



if time>1000:
    print(-1)
else:
    print(time)