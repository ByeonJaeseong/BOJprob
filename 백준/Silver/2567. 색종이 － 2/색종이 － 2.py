def color(x, y) :
    global matrix
    for i in range(x, x+10):
        for j in range(y, y+10):
            result[i+1][j+1]=1


N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
result = [[0]*101 for _ in range(101)]
for i in range(N):
    color(matrix[i][0], matrix[i][1])
count = 0
for i in range(1, 101):
    for j in range(101):
        if (result[i][j-1]==0 and result[i][j]==1) or (result[i][j-1]==1 and result[i][j]==0):
            count+=1

        if (result[j-1][i] == 0 and result[j][i] == 1) or (result[j-1][i] == 1 and result[j][i] == 0):
            count += 1

print(count)