def gauss_jordan(matrix):
    n = len(matrix)
    # 단위 행렬 생성
    identity_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        identity_matrix[i][i] = 1

    # 기본 행렬과 단위 행렬을 합친 확장 행렬 생성
    augmented_matrix = [row + identity_matrix[i] for i, row in enumerate(matrix)]

    # 가우스 소거법
    for i in range(n):
        # 주 대각선 원소가 0이라면 피봇을 변경하여 0이 아닌 원소를 찾음
        if augmented_matrix[i][i] == 0:
            for j in range(i + 1, n):
                if augmented_matrix[j][i] != 0:
                    augmented_matrix[i], augmented_matrix[j] = augmented_matrix[j], augmented_matrix[i]
                    break
            else:
                raise ValueError("역행렬이 존재하지 않습니다.")

        # i번째 행을 i번째 원소를 1로 만들기 위해 나눔
        pivot_inverse = 1 / augmented_matrix[i][i]
        augmented_matrix[i] = [elem * pivot_inverse for elem in augmented_matrix[i]]

        # i번째 열의 i번째 원소를 제외한 모든 원소를 0으로 만듦
        for j in range(n):
            if i != j:
                factor = augmented_matrix[j][i]
                augmented_matrix[j] = [elem - factor * augmented_matrix[i][idx] for idx, elem in
                                       enumerate(augmented_matrix[j])]

    # 역행렬 부분만 추출
    inverse_matrix = [row[n:] for row in augmented_matrix]

    return inverse_matrix


N = int(input())
matrix = []
lst = []
for _ in range(N):
    temp = list(map(int, input().split()))
    matrix.append(temp[:N])
    lst.append(temp[N])
# print(matrix)
inverse_matrix = gauss_jordan(matrix)
# print(inverse_matrix)
for i in range(N):
    count = 0
    for j in range(N):
        count += inverse_matrix[i][j]*lst[j]
    print(int(round(count, 0)), end=" ")
