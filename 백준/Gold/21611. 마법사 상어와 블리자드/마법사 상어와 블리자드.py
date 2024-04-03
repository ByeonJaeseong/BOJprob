N, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
order = [list(map(int, input().split())) for _ in range(K)]
order = [[x[0]-1, x[1]] for x in order]
sx, sy = N//2, N//2
dx = (0, 1, 0, -1)
dy = (-1, 0, 1, 0)
upper, lower = N//2+1, N//2-1
bead_loc = dict()
odd, d = 3, 0
for i in range(N**2-1):
    if i == odd**2-2:
        odd+=2
        upper, lower = upper+1, lower-1
    if lower<=sx+dx[d]<=upper and lower<=sy+dy[d]<=upper:
        sx, sy = sx+dx[d], sy+dy[d]
        bead_loc[i] = (sx, sy)
    else:
        d = (d+1)%4
        sx, sy = sx + dx[d], sy+dy[d]
        bead_loc[i] = (sx, sy)
loc_dict = { v : k for k, v in bead_loc.items()}
bead_lst = []
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
# print(bead_loc)
for i in range(N**2-1):
    x, y = bead_loc[i]
    if matrix[x][y]==0:continue
    bead_lst.append(matrix[x][y])
# 초기 구술 넣기
score = 0
for o in order:
    dir, dist = o
    romove_set = set({})
    for i in range(1,dist+1):
        rx, ry = N // 2 + i * dx[dir], N // 2 + i * dy[dir]
        romove_set.add(loc_dict[(rx,ry)])
    new_lst = []
    ############# 블리자드 시작

    for i in range(len(bead_lst)):
        if i in romove_set:continue
        new_lst.append(bead_lst[i])
    ############# 블리자드 끝
    while True:
        # print(new_lst)
        if not new_lst: break
        nl = len(new_lst)
        new_lst.append(4)
        new_lst2 = []
        count = 0
        new_lst.reverse()
        for i in range(len(new_lst)):
            # print(new_lst2)
            v = new_lst.pop()
            if len(new_lst2) == 0:
                count = 1
            else:
                if v == new_lst2[-1]:
                    count+=1
                else:
                    # 값이 다른 케이스는
                    if count>=4 :
                        score += new_lst2[-1]*count
                        # 점수 더해주고
                        for _ in range(count):
                            new_lst2.pop()
                        # 개수 빼주고
                        count = 1
                    else:
                        count =1
            if v<4:
                new_lst2.append(v)
                # 조건에 맞을 때 만 갯수 더해주기
        new_lst = new_lst2
        if nl == len(new_lst2):break
    bead_lst.clear()
    new_lst.append(4)
    count = 0
    now = -1
    for i in range(len(new_lst)):
        if count == 0:
            now = new_lst[i]
            count = 1
            continue

        if now == new_lst[i]:
            # 값이 서로 같으면
            count+=1
        else:
            bead_lst.append(count)
            bead_lst.append(now)
            count=1
            now = new_lst[i]
        if len(bead_lst) == N**2-1 : break
    bead_lst = bead_lst[:N**2-1]
    # print(bead_lst)
print(score)
