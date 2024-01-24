N = int(input())
input_value = [list(map(int, input().split())) for _ in range(N)]
matrix = [[0]*1001 for _ in range(1001)]
result = [0]*(N+1)
for i in range(N):
    x = input_value[i][0]
    dx = input_value[i][2]
    y = input_value[i][1]
    dy = input_value[i][3]
    for j in range(x, x+dx):
        for k in range(y, y+dy):
            matrix[j][k]=i+1

for i in range(1001):
    for j in range(1001):
        result[matrix[i][j]]+=1

for i in range(1, N+1):
    print(result[i])