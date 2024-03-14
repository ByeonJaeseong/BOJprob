'''
구상 시키는대로 잘하자 문제가 참 어렵다
max 100*100행열
시간 0.5초
구상 5분 정도?
'''
def Rsort():
    global matrix
    # print(*matrix,sep="\n")
    # print("실행")
    mx = 0
    temp_matrix = []
    # 맨 위에서 부터 작업을 하고 역순으로 넣자
    for i in range(len(matrix)):
        temp = dict()
        # print(temp)
        for j in range(len(matrix[i])):
            if matrix[i][j]==0:continue
            if matrix[i][j] in temp:
                temp[matrix[i][j]] = temp[matrix[i][j]] + 1
            else:
                temp[matrix[i][j]] = 1
        # 개수 저장하기 완료
        temp_lst = [(v, k) for k, v in temp.items()]
        mx = max(mx, len(temp_lst)*2)
        temp_lst.sort()
        append_lst = []
        for i in temp_lst:
            append_lst.append(i[1])
            append_lst.append(i[0])
        # print(append_lst)
        temp_matrix.append(append_lst)
    matrix.clear()
    # print(*temp_matrix,sep="\n")
    # print("템프 실행")
    for t in temp_matrix:
        if len(t) < min(mx, 100):
            for _ in range(len(t), min(mx, 100)):
                t.append(0)
        matrix.append(t[:100])
def Csort():
    global matrix
    # print(*matrix,sep='\n')
    # print("돌리기전")
    matrix = list(map(list, zip(*matrix)))
    # print(*matrix,sep='\n')
    # print("Csort")
    Rsort()
    matrix = list(map(list, zip(*matrix)))

r, c, K = map(int, input().split())
r, c = r-1, c-1
## 타겟 되는 지점 설정
matrix = [list(map(int, input().split())) for _ in range(3)]
# print(*matrix, sep='\n')
# print(r, c)
count = 0
while True:

    if len(matrix)>r and len(matrix[0])>c and matrix[r][c] == K:
        break
    count+=1
    if count>100:break
    if len(matrix)>=len(matrix[0]):
        Rsort()
    else:
        Csort()
    # print(*matrix,sep='\n')
    # print()

if count>100:
    print(-1)
else:
    print(count)