'''
차분히 풀면 쉽게 풀수 있는 문제
M -> 행
N -> 열
열끼리는는 이어져 있음
T번 회전
xi, di ki ->번호가 xi인 원판을 (di->0시계방향, -1 반시계 방향 )방향으로 ki칸
번호란 행의 순서를 이야기함
-> 원판에 수가 남아 있으면 인접하면서 수가 같은것 모두 찾음
    -> 있는 경우 인접한 수들 다 지움
    -> 없는 경우 원ㅍ나에 적힌 수의 평균을 구하고 평균보다 큰 수에서 1빼고 작은 수 1 더함
구상 7분 -> 시키는대로만 잘하면 되는 문제

디버깅 하는데 시간을 많이쓴게 아쉬움 ㅠ -> 반시계방향 구상을 잘못함
'''

def rotation(x,d,k):
    for i in range(1,M+1):
        if i % x == 0:
            # print(i,x)
            # print(matrix[i-1])
            if d == 0:
                # print("0실행")
                matrix[i - 1] = matrix[i - 1][-k:] + matrix[i - 1][:-k]
            else:
                # print("1실행")
                matrix[i - 1] =  matrix[i - 1][k:] + matrix[i - 1][:k]
            # print(matrix[i-1])

def delete():
    global matrix
    st = set([])
    # print()
    # print(*matrix, sep='\n')
    # print()
    for i in range(M):
        for j in range(N):
            if matrix[i][j]==0:continue
            for k in range(2):
                X = i+dx[k]
                Y = (j+dy[k])%N
                if X<M and matrix[i][j]==matrix[X][Y]:
                    st.add((i,j))
                    st.add((X,Y))
    # print(len(st))
    if len(st)>0:
        while st:
            x, y =st.pop()
            matrix[x][y]=0
    # 같은경우가 있을때
    else:
        total = 0
        total_length = 0
        for i in range(M):
            for j in range(N):
                if matrix[i][j] !=0:
                    total += matrix[i][j]
                    total_length +=1
        if total_length>0:
            average = total/total_length
            for i in range(M):
                for j in range(N):
                    if matrix[i][j] == 0 : continue
                    if matrix[i][j] >average:
                        matrix[i][j]-=1
                    elif matrix[i][j] < average:
                        matrix[i][j]+=1





M, N, T = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
rot = [list(map(int, input().split())) for _ in range(T)]
dx = (0, 1)
dy = (1, 0)
for i in range(T):
    x, d, k = rot[i]
    rotation(x, d, k)
    # print(*matrix, sep='\n')
    delete()
print(sum([sum(matrix[i]) for i in range(M)]))