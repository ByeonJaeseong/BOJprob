
def check(x,y) : return 0<=x<8 and 0<=y<21

def game(lst):
    global mx
    score = 0
    loc = {0:(0,0), 1:(0,0), 2:(0,0), 3:(0,0)}
    for i in range(10):
        # print(i)
        x, y = loc[lst[i]]
        if not check(x, y): return
        if (x,y) != (0,0) and score_board[x][y] == 0: return
        if (x,y) == (-1, -1) : return
        # print(i,x,y,lst[i],dice[i],score)
        # 밖에 나간 애를 다시 쓰려 하면
        matrix[x][y].pop()
        if score_board[x][y] == 40:
            loc[lst[i]] = (-1, -1)
            # 말 아웃 시키기
            continue
        if y>0 and y % 5 == 0:
            X, Y = x+dice[i], y
            loc[lst[i]] = (X,Y)
            if not check(X,Y): continue
            if len(matrix[X][Y])>0 : return
            # 차있으면 못쓰는 것
            # print(i,X,Y)
            score += score_board[X][Y]
            matrix[X][Y].append(lst[i])
        else:
            X, Y = x, y + dice[i]
            loc[lst[i]] = (X, Y)
            # print("실행")
            if not check(X, Y): continue
            if len(matrix[X][Y])>0: return
            # 차있으면 못쓰는 것
            score += score_board[X][Y]
            matrix[X][Y].append(lst[i])

    mx = max(mx, score)
def combination(n, lst=[]):
    if n ==10:
        for i in range(8):
            for j in range(21):
                matrix[i][j].clear()
        matrix[0][0].extend((0,1,2,3))
        game(lst)
        return

    combination(n + 1, lst + [0])
    combination(n + 1, lst + [1])
    combination(n + 1, lst + [2])
    combination(n + 1, lst + [3])

dice = list(map(int, input().split()))
# print(dice)
# 이건 주사위
matrix = [[[] for _ in range(21)] for _ in range(8)]
score_board = [[0 for _ in range(21)] for _ in range(8)]
score_board[0] =  [2*i for i in range(21)]
score_board[1][5], score_board[2][5], score_board[3][5], score_board[4][5], score_board[5][5], score_board[6][5], score_board[7][5] = 13, 16, 19, 25, 30, 35, 40
score_board[1][10], score_board[2][10], score_board[3][10], score_board[4][10], score_board[5][10], score_board[6][10] = 22, 24, 25, 30, 35, 40
score_board[1][15], score_board[2][15], score_board[3][15], score_board[4][15], score_board[5][15], score_board[6][15], score_board[7][15] = 28, 27, 26, 25, 30, 35, 40
matrix[4][5] = matrix[3][10] = matrix[4][15]
# 같은 주솟값으로 업데이트 해주기
matrix[0][20] = matrix[7][5] = matrix[6][10] = matrix[7][15]
matrix[5][5] = matrix[4][10] = matrix[5][15]
matrix[6][5] = matrix[5][10] = matrix[6][15]
# matrix[4][5].append(1)
# print(*matrix, sep='\n')
mx = 0
combination(1,[0])
print(mx)