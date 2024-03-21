'''
문제 이해 7분
물고기는 8방이동
상어와 물고기, 물고기와 물고기 같은 칸 가능 -> lst 써야겠넹

예제보고 뭐야 메모리 안터져라 생각했지만 메모리 용량보고 끄덕

디버깅 시작은 35분즈음?
'''

def check(x,y):
    return 0<=x<4 and 0<=y<4

fdx = (0, -1, -1, -1, 0 ,1, 1, 1)
fdy = (-1, -1, 0, 1, 1, 1, 0, -1)
sdx = (-1, 0, 1, 0)
sdy = (0, -1, 0, 1)

M, S = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
sx, sy = map(int, input().split())
sx, sy = sx-1, sy-1
fish = [[[] for _ in range(4)] for _ in range(4)]
smell = [[0]*4 for _ in range(4)]
# 물고기는 좌표와 방향을 가지고 있따.
for f in matrix:
    x, y, d= f
    fish[x-1][y-1].append(d-1)
# print(*fish, sep='\n')
# print()
shark_move = []
for i in range(4):
    for j in range(4):
        for k in range(4):
            shark_move.append((i,j,k))
## 조심 격자를 벗어나면 잘못된 방법


for _ in range(S):
    copy_fish = [[f[:] for f in f1 ] for f1 in fish]
    # 3차원 배열 복사
    ######### 1번 구현 완료 5번에서 추가 해줄 예정 ###########
    new_fish = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for f in fish[i][j]:
                d = f
                marker = False
                for _ in range(8):
                    X = i+fdx[d]
                    Y = j+fdy[d]
                    # 물고기가 갈 수 있는지 파악
                    if check(X,Y) and (X,Y) !=(sx,sy) and smell[X][Y]==0:
                        # 격자 안, 상어가 없는 칸, 냄새가 없는 칸
                        new_fish[X][Y].append(d)
                        marker = True
                        break
                    else:
                        d = (d-1)%8
                if not marker:
                    # 이동 못했으면 자기 자리에 넣기
                    new_fish[i][j].append(f)
    ############# 2번 구현 끝 ######################
    # print(*new_fish, sep='\n')
    # print()
    mx = -1
    shark_dir = ()
    for sm in shark_move:
        visit = [[False]*4 for _ in range(4)]
        marker = True
        X, Y = sx, sy
        temp_mx =0
        for smd in sm:
            X += sdx[smd]
            Y += sdy[smd]
            if not check(X,Y):
                marker = False
                break

            if visit[X][Y]:continue
            visit[X][Y] = True
            temp_mx += len(new_fish[X][Y])
        # print(sm, marker, temp_mx,sx,sy,X,Y)
        if not marker :
            X, Y = sx, sy
            for smd in sm:
                X += sdx[smd]
                Y += sdy[smd]
                if check(X,Y) : visit[X][Y] = False
            continue
        # 불가능한 경로면 아래 안봐도 됨
        # 처리 할 것 없음
        if temp_mx>mx:
            mx = temp_mx
            shark_dir = sm
        X, Y = sx, sy
        for smd in sm:
            X += sdx[smd]
            Y += sdy[smd]
            if check(X,Y) : visit[X][Y]=False

    ############## 상어 길찾기 끝 #############
    # 냄새남기기 + 상어 옮기기
    for sm in shark_dir:
        sx += sdx[sm]
        sy += sdy[sm]
        if len(new_fish[sx][sy]) > 0:
            new_fish[sx][sy].clear()
            smell[sx][sy] = 3
            # 한번씩 빼줄거니까 3으로 셋팅
    ############# 3번구현 완료 ###############3
    for i in range(4):
        for j in range(4):
            if smell[i][j]>0:
                smell[i][j]-=1
    ########### 4번 구현 완료 ###############

    for i in range(4):
        for j in range(4):
            # if (i, j) == (sx, sy) : continue
            new_fish[i][j].extend(copy_fish[i][j])

    fish = new_fish
    # print(shark_dir)
    # print(*fish, sep='\n')
    # print(sx, sy)
# print(*fish,sep='\n')
# print(sx, sy)
count = 0
for i in range(4):
    for j in range(4):
        count+=len(fish[i][j])
print(count)



