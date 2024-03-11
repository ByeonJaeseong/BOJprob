'''
브르투포스로 완탐하면 끝날문제
'''
M1, N1 = map(int, input().split())
matrix1 = [list(map(int, input())) for _ in range(M1)]
M2, N2 = map(int, input().split())
matrix2 = [list(map(int, input())) for _ in range(M2)]
mn = max(N1,N2)*(M1+M2)
for _ in range(4):
    matrix = [[0]*100 for _ in range(100)]
    for i in range(M1):
        for j in range(N1):
            matrix[i][j] = matrix1[i][j]
    for i in range(max(M1, M2)+1):
        for j in range(max(N1, N2)+1):
            if (i+M2)*(j+N2)>mn: continue
            # 워스트 케이스보다 나쁘면 탐색할 이유가 없음
            marker = True
            for p in range(len(matrix2)):
                for q in range(len(matrix2[0])):
                    if matrix[i+p][j+q] ==1 and matrix2[p][q] ==1:
                        marker = False
                        break
            if marker:
                mn = min(max(M1, (i+len(matrix2)))*max(N1,(j+len(matrix2[0]))), mn)

    matrix2 = list(map(list, zip(*matrix2[::-1])))
print(mn)