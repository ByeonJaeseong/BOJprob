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

    if count == 5 and (x==0 or matrix[x-1][y]!=matrix[x][y]):
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
    if count == 5  and (y==0 or matrix[x][y-1]!=matrix[x][y]):
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
    if count == 5 and (x==0 or y==0 or matrix[x][y]!=matrix[x-1][y-1]):
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
    if count == 5 and (y==18 or x==0 or matrix[x][y]!=matrix[x-1][y+1]):
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

        if matrix[i][j]!=0 and (search(i, j) or search1(i, j) or search2(i, j) or search3(i, j)):
            marker = True
            x = i
            y = j
            winner = matrix[i][j]
            break
    if marker:
        break
if winner != 0 and not search3(x, y):
    print(winner)
    print(x+1, y+1)
elif winner !=0 and search3(x,y):
    print(winner)
    print(x+5, y-3)
else:
    print(0)