def check(x,y):
    return 0<=x<N and 0<=y<N


N = int(input())
order = list(input())
matrix = [list(input()) for _ in range(N)]
dx = [1, 0, -1, 0 , 1, 1, -1, -1]
dy = [0, -1, 0, 1, 1, -1, 1, -1]

#L -> -1, R->+1
marker = True
x, y, d  = 0, 0, 0
# 학생좀비를 만나는지 만나지 않는지
zombi = set([])
switch = set([])
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'Z':
            zombi.add((i, j, 0))
        if matrix[i][j] == 'S':
            switch.add((i,j))
light = [[False]*N for _ in range(N)]
for i in range(len(order)):

    od = order[i]
    if od == 'F':
        X, Y = x+dx[d], y+dy[d]
        if check(X,Y):
            x, y = X, Y
        # 벽에 부딛치지 않으면 전진
        # 벽에 부딛치면 제자리
    if od =='L':
        d = (d-1)%4
    if od =='R':
        d = (d+1)%4
    if (x,y) in switch:
        light[x][y]=True
        for j in range(8):
            X, Y = x+dx[j], y+dy[j]
            if check(X,Y):
                light[X][Y]=True
    if not light[x][y] and ((x,y,0) in zombi or (x,y,2) in zombi):
        marker = False
        break

    temp_set = set([])
    while zombi:
        zx, zy, zd = zombi.pop()
        Zx, Zy = zx+dx[zd], zy+dy[zd]
        if check(Zx, Zy):
            temp_set.add((Zx,Zy,zd))
        else:
            temp_set.add((zx, zy, (zd+2)%4))
    zombi = temp_set
    # 좀비 옮기기 완료

    # 불이 꺼져있고, 좀비랑 같이 있으면
    # print(x,y,d)
    # print(zombi)
    if not light[x][y] and ((x,y,0) in zombi or (x,y,2) in zombi):
        marker = False
        break


if not marker:
    print("Aaaaaah!")
else :
    print( "Phew...")