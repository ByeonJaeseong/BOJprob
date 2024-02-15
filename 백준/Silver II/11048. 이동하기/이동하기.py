'''
자기자리 끝자리 포함
'''
M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
candy = [[0]*N for _ in range(M)]
for i in range(M):
    for j in range(N):
        candy[i][j]+=matrix[i][j]
        if j-1>=0:
            candy[i][j]=max(candy[i][j-1]+matrix[i][j], candy[i][j])
        if i-1>=0:
            candy[i][j]=max(candy[i-1][j]+matrix[i][j], candy[i][j])
print(candy[M-1][N-1])