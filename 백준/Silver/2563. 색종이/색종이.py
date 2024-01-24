def color(x, y) :
    global matrix
    for i in range(x, x+10):
        for j in range(y, y+10):
            result[i][j]=1

N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
result = [[0]*100 for _ in range(100)]
for i in range(N):
    color(matrix[i][0], matrix[i][1])
count = 0
for i in range(100):
    for j in range(100):
        if result[i][j]==1:
            count+=1
print(count)