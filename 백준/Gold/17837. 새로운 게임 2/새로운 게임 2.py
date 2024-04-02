'''
언젠간 털고가야할 문제
시작 9시 56분
말이 4개 이상이면 끝
흰색인 경우 그 칸으로 이동->번호 그대로
빨간색인 경우  -> 쌓여있는 번호 반대로
파란색인 경우 방향 반대로 이동 -> 파란색인경우 움직이지 않음
벗어나는경우 == 파란색
'''

def check(x,y) : return 0<=x<N and 0<=y<N

N, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
order = [list(map(int, input().split())) for _ in range(K)]
order = [[o[0]-1, o[1]-1, o[2]-1] for o in order]
# 우 좌 상 하
# 행, 열, 이동방향
dir = {0:1, 1:0, 2:3, 3:2}
board = [[[] for _ in range(N)] for _ in range(N)]
loc = dict()
for i in range(K):
    x, y, d = order[i]
    # print(x,y,d)
    loc[i] = (x, y, d)
    # 현재 위치 넣어주고
    board[x][y].append(i)
    # 보드에 순서대로 쌓아주기
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)
time = 0
for i in range(1, 1002):
    time = i
    marker = False
    for k in range(K):
        x, y, d = loc[k]
        # 현재위치 받아오기
        X, Y = x+dx[d], y+dy[d]
        if check(X,Y) and matrix[X][Y] == 0:
            # 옮기려는 칸이 흰색이면
            move = []
            for i in range(len(board[x][y])):
                if board[x][y][i] == k:
                    move = board[x][y][i:]
                    board[x][y] = board[x][y][:i]
                    break
            # print(move)
            for n in move:
                loc[n] = (X,Y, loc[n][2])
                # 방향 유지한 채로 움직여 주기
            board[X][Y].extend(move)
            if len(board[X][Y])>=4:
                marker=True
                break
        elif check(X,Y) and matrix[X][Y] == 1:
            # 옮기려는 칸이 빨강이면
            move = []
            for i in range(len(board[x][y])):
                if board[x][y][i] == k:
                    move = board[x][y][i:]
                    board[x][y] = board[x][y][:i]
                    break
            for n in move:
                loc[n] = (X,Y, loc[n][2])
                # 방향 유지한 채로 움직여 주기
            move.reverse()
            # 역방향으로 넣어주기
            board[X][Y].extend(move)
            if len(board[X][Y])>=4:
                marker=True
                break
        else:
            d = dir[d]
            # 방향 바꿔주기
            X, Y = x+dx[d], y+dy[d]
            if not check(X,Y) or matrix[X][Y] == 2:
                loc[k] = (x,y,d)
                # 방향만 바꿔주고 가만히
                continue
            loc[k] = (x,y,d)
            if check(X, Y) and matrix[X][Y] == 0:
                # 옮기려는 칸이 흰색이면
                move = []
                for i in range(len(board[x][y])):
                    if board[x][y][i] == k:
                        move = board[x][y][i:]
                        board[x][y] = board[x][y][:i]
                        break
                for n in move:
                    loc[n] = (X, Y, loc[n][2])
                    # 방향 유지한 채로 움직여 주기
                board[X][Y].extend(move)
                if len(board[X][Y]) >= 4:
                    marker = True
                    break
            elif check(X, Y) and matrix[X][Y] == 1:
                # 옮기려는 칸이 빨강이면
                move = []
                for i in range(len(board[x][y])):
                    if board[x][y][i] == k:
                        move = board[x][y][i:]
                        board[x][y] = board[x][y][:i]
                        break
                for n in move:
                    loc[n] = (X, Y, loc[n][2])
                    # 방향 유지한 채로 움직여 주기
                move.reverse()
                # 역방향으로 넣어주기
                board[X][Y].extend(move)
                if len(board[X][Y]) >= 4:
                    marker = True
                    break
    if marker:break
    # print(*board, sep='\n')
    # print()
if time>1000:
    print(-1)
else:
    print(time)