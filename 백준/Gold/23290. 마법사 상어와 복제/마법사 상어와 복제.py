'''
풀기시작한 시간 14시 13븐
'''

def check(x,y) : return 0<=x<4 and 0<=y<4

N, K = map(int, input().split())
input_fish = [list(map(int, input().split())) for _ in range(N)]
matrix = [[[] for _ in range(4)] for _ in range(4)]
smell = [[0]*4 for _ in range(4)]
sx, sy = map(int, input().split())
sx, sy = sx-1 , sy-1
for x, y, d in input_fish:
    matrix[x-1][y-1].append(d-1)
dx = (0 ,-1, -1, -1, 0, 1, 1, 1)
dy = (-1, -1, 0, 1, 1, 1, 0, -1)

sdx = (-1, 0, 1, 0)
sdy = (0, -1, 0, 1)
priority = []
for i in range(4):
    for j in range(4):
        for k in range(4):
            priority.append((i,j,k))

for de in range(K):
    # 1번 구현
    # 사실 할 건 없음

    # 2번 구현
    new = [[[] for _ in range(4)] for _ in range(4)]

    for i in range(4):
        for j in range(4):
            if not matrix[i][j]: continue
            # 물고기 없으면 넘어가기
            for dir in matrix[i][j]:
                d = dir
                marker = False
                for _ in range(8):
                     X, Y = i+dx[d], j+dy[d]
                     if check(X,Y) and smell[X][Y] == 0 and (X,Y) != (sx, sy):
                         new[X][Y].append(d)
                         # 갈 수 있으면 회전 시키기
                         marker = True
                         break
                     d = (d-1)%8
                if not marker:
                    new[i][j].append(dir)

    # print("이동함")
    # print(*new,sep='\n')
    # 2번 구현 완료

    mx = -1
    move_dir = ()
    visit =  [[False]*4 for _ in range(4)]
    for p in priority:
        ssx, ssy = sx, sy
        count = 0
        for direc in p:
            ssx, ssy = ssx+sdx[direc], ssy + sdy[direc]
            if not check(ssx, ssy):

                count = -1
                #밖으로 나가는건 불가능한 경로
                break
            if visit[ssx][ssy]: continue
            visit[ssx][ssy] = True
            count += len(new[ssx][ssy])

        ssx, ssy = sx, sy

        for direc in p:
            ssx, ssy = ssx+sdx[direc], ssy + sdy[direc]
            if not check(ssx, ssy): continue
            visit[ssx][ssy] = False
        if count == -1 : continue
        if mx<count:
            mx = count
            move_dir = p

    for d in move_dir:
        sx, sy = sx+sdx[d], sy+sdy[d]

        if not new[sx][sy]: continue
        # 없으면 안하기
        smell[sx][sy] = 3
        new[sx][sy].clear()
    # 3번 구현 완료
    for i in range(4):
        for j in range(4):
            if smell[i][j]>0: smell[i][j] -= 1
            matrix[i][j].extend(new[i][j])
    # 4번 구현 완료
    # print(de+1)
    # print(sx, sy)
    # print(*new,sep='\n')
    # print("smell")
    # print(*smell, sep='\n')
    # print()
    # print(*matrix,sep='\n')
    # print()
    #

result = 0
for i in range(4):
    for j in range(4):
        result += len(matrix[i][j])
print(result)