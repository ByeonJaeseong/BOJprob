'''
구상 5분 단순 빡구현 문제로 접근하기러 함
'''

def row(n):
    count = 0
    visit = [False]*N
    for i in range(N):
        if i==N-1:
            count = 1
            break

        if matrix[n][i]==matrix[n][i+1]:
            continue
        #같으면 그냥 가면 됨
        if abs(matrix[n][i]-matrix[n][i+1])>1:
            break
        # 두칸 이상 차이나면 다리를 놓을 수 없음

        if matrix[n][i]> matrix[n][i+1]:
            #큰데서 밑으로 내려가려먼
            marker = True
            # L칸의 길이가 1이하여야함
            if i+L>=N:
                break
            for j in range(i+1, i+1+L):
                if matrix[n][i]-matrix[n][j] == 1 and not visit[j]:
                    visit[j]=True
                    continue
                else:
                    marker=False
                    break
            if not marker:
                break

        if matrix[n][i] < matrix[n][i + 1]:
            # 올라가려면
            marker = True
            # L칸의 길이가 1이하여야함
            if i-L+1<0:break
            for j in range(L):
                if matrix[n][i-j]-matrix[n][i+1] == -1 and not visit[i-j]:
                    visit[i-j]=True
                    continue
                else:
                    marker=False
                    break
            if not marker:
                break
    return count

def column(n):
    count = 0
    visit = [False] * N
    for i in range(N):
        if i == N - 1:
            count = 1
            break

        if matrix[i][n] == matrix[i+1][n]:
            continue
        # 같으면 그냥 가면 됨
        if abs(matrix[i][n] - matrix[i+1][n]) > 1:
            break
        # 두칸 이상 차이나면 다리를 놓을 수 없음

        if matrix[i][n] > matrix[i+1][n]:
            # 큰데서 밑으로 내려가려먼
            marker = True
            # L칸의 길이가 1이하여야함
            if i+L>=N:break
            for j in range(i + 1, i + 1 + L):
                if matrix[i][n] - matrix[j][n] == 1 and not visit[j]:
                    visit[j] = True
                    continue
                else:
                    marker = False
                    break
            if not marker:
                break

        if matrix[i][n] < matrix[i+1][n]:
            # 올라가려면
            marker = True
            # L칸의 길이가 1이하여야함
            if i-L+1<0:break
            for j in range(L):
                if matrix[i-j][n] - matrix[i+1][n] == -1 and not visit[i - j]:
                    visit[i - j] = True
                    continue
                else:
                    marker = False
                    break
            if not marker:
                break
    return count

N, L = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
result = 0
for i in range(N):
    result = result+row(i)+column(i)
print(result)