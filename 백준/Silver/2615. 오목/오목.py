def check(x, y):
    return 0<=x<19 and 0<=y<19

def search(x, y):
    global matrix
    dx = [1, 2, 3, 4, 5]
    count = 1
    for i in range(5):
        if check(x+dx[i], y) and matrix[x][y] == matrix[x+dx[i]][y]:
            count+=1
        else:
            break
    # if x==9 and y == 6:
    # #     print(x, y, "실행1", count)
    # # # print(count)
    if count == 5:
        return True
    else:
        return False

def search1(x, y):
    global matrix
    dx = [1, 2, 3, 4, 5]
    count = 1
    for i in range(5):
        if check(x, y+dx[i]) and matrix[x][y] == matrix[x][y+dx[i]]:
            count+=1
        else:
            break
    # if y == 18:
    #     print("실행2", x, y, count)
    if count == 5:
        return True
    else:
        return False

def search2(x, y):
    global matrix
    dx = [1, 2, 3, 4, 5]
    count = 1
    for i in range(5):
        if check(x+dx[i], y+dx[i]) and matrix[x][y] == matrix[x+dx[i]][y+dx[i]]:
            count+=1
        else:
            break
    # print(count)
    # if y == 18:
    #     print(x,y,count,"실행3")
    if count == 5:
        return True
    else:
        return False

def search3(x, y):
    global matrix
    dx = [1, 2, 3, 4, 5]
    count = 1
    for i in range(5):
        if check(x+dx[i], y-dx[i]) and matrix[x][y] == matrix[x+dx[i]][y-dx[i]]:
            count+=1
        else:
            break
    # print(count)
    # if y == 18:
    #     print(x,y,count,"실행4")
    if count == 5:
        return True
    else:
        return False

matrix = [list(map(int, input().split())) for _ in range(19)]

winner = 0
x = 0
y = 0
for i in range(19):
    marker = False
    for j in range(19):
        # if i==9 and j==6:
        #     # print("ㅁㅇㄴㄻㄴㅇㄹ")
        #     print(matrix[i][j], search(x, y), (i==0 or matrix[i-1][j]!=matrix[i][j]))

        if matrix[i][j]!=0 and ((search(i, j) and (i==0 or matrix[i-1][j]!=matrix[i][j]))\
                                or (search1(i, j) and (j==0 or matrix[i][j-1]!=matrix[i][j])) \
                                or (search2(i, j) and (i==0 or j==0 or matrix[i][j]!=matrix[i-1][j-1]))\
                                or (search3(i, j) and (j==18 or i==0 or matrix[i][j]!=matrix[i-1][j+1]))):
            # print(i, j, "실행되었습니다")
            # print(matrix[i][j], search(x, y), (i == 0 or matrix[i - 1][j] != matrix[i][j]))
            # print(matrix[i][j], search1(x, y), (i == 0 or matrix[i - 1][j] != matrix[i][j]))
            # print(matrix[i][j], search2(x, y), (i == 0 or matrix[i - 1][j] != matrix[i][j]))
            # print(matrix[i][j], search3(x, y), (i == 0 or matrix[i - 1][j] != matrix[i][j]))

            marker = True
            x = i
            y = j
            winner = matrix[i][j]
            break
    if marker:
        # print(x, y, "끊음")
        break
if winner != 0 and not search3(x, y):
    print(winner)
    print(x+1, y+1)
elif winner !=0 and search3(x,y):
    print(winner)
    print(x+5, y-3)
else:
    print(0)