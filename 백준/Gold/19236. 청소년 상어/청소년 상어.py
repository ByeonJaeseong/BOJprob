'''
문제 이해 7분
크게 방만하지 않게 구현만 하면 되는 문제
# 상어는 한번에 여러칸을 이동할 수 있음
-> 이 여러 칸에 대해서 백트래킹을 해야함
첫 테케 돌리기 53분
'''
def check(x,y):
    return 0<=x<4 and 0<=y<4

def shark_move(n, sx, sy, d, count, temp_matrix = []):
    global mx
    temp_matrix = fish_move(temp_matrix)
    # print(*temp_matrix, sep='\n')
    # print(n, sx, sy, d, count)
    for i in range(1,5):
        X = sx+dx[d]*i
        Y = sy+dy[d]*i
        if check(X,Y) and 0<temp_matrix[X][Y][0]<=16:
            v, fd = temp_matrix[X][Y]
            temp_matrix[sx][sy] = (0, d)
            temp_matrix[X][Y] =  (17, fd)
            shark_move(n+1, X, Y, fd, count+v, [x[:] for x in temp_matrix])
            temp_matrix[X][Y] = (v,fd)
            temp_matrix[sx][sy] = (17, d)
        elif check(X,Y) and temp_matrix[X][Y]==0:
            mx = max(mx,count)
        else:
            mx = max(mx,count)

            # 물고기 방향으로 설정



def fish_move(temp_matrix):
    fish = dict()
    for i in range(4):
        for j in range(4):
            fish[temp_matrix[i][j][0]]=(i,j,temp_matrix[i][j][1])

    for i in range(1,17):
        if i in fish:
            x, y, d = fish[i]
            for j in range(8):
                X = x+dx[(d+j)%8]
                Y = y+dy[(d+j)%8]
                if check(X, Y) and temp_matrix[X][Y][0]<=16:
                    # 안에 있고 물고기거나 빈칸이면
                    fish[temp_matrix[x][y][0]] = (X, Y, (d+j)%8)
                    fish[temp_matrix[X][Y][0]] = (x, y, temp_matrix[X][Y][1])
                    temp_matrix[x][y] = (temp_matrix[x][y][0], (d+j)%8)
                    temp_matrix[X][Y], temp_matrix[x][y] = temp_matrix[x][y], temp_matrix[X][Y]
                    # 서로 자리 바꾸기
                    break
    return temp_matrix
            # i번째 물고기 위치

# 상어는 17로 표시 빈칸은 0으로 표시


temp_matrix = [list(map(int, input().split())) for _ in range(4)]
matrix = [[] for _ in range(4)]
dx = (-1, -1, 0, 1, 1, 1, 0, -1)
dy = (0, -1, -1, -1, 0, 1, 1, 1)
# zero padding 방향 맞춰주기
for i in range(4):
    matrix[i].append((temp_matrix[i][0], temp_matrix[i][1]-1))
    matrix[i].append((temp_matrix[i][2], temp_matrix[i][3]-1))
    matrix[i].append((temp_matrix[i][4], temp_matrix[i][5]-1))
    matrix[i].append((temp_matrix[i][6], temp_matrix[i][7]-1))
# print(*matrix, sep='\n')
# print()
mx = matrix[0][0][0]
matrix[0][0] = (17, matrix[0][0][1])

shark_move(1, 0, 0, matrix[0][0][1], mx, [x[:] for x in matrix])
print(mx)
