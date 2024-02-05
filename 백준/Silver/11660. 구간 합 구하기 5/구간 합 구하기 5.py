M, N = map(int, input().split())
matrix = [[0]*(M+1)]+[[0]+list(map(int, input().split())) for _ in range(M)]
# for i in range(M):
#     print(matrix[i])
# print()
sum_matrix = [[0]*(M+1) for _ in range(M+1)]
result_matrix = [list(map(int,input().split())) for _ in range(N)]
for i in range(1,M+1):
    sum_matrix[i][1]=sum_matrix[i-1][1]+matrix[i][1]
    for j in range(2,M+1):
        sum_matrix[i][j] = sum_matrix[i][j-1]+sum_matrix[i-1][j]+matrix[i][j]-sum_matrix[i-1][j-1]
# for i in range(M+1):
#     print(sum_matrix[i])
for i in range(N):
    s,e,S,E = result_matrix[i][0], result_matrix[i][1], result_matrix[i][2], result_matrix[i][3]
    print(sum_matrix[S][E]-sum_matrix[S][e-1]-sum_matrix[s-1][E]+sum_matrix[s-1][e-1])
