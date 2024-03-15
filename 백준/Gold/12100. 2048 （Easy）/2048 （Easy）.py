'''
최대 5번 이동이란 건 그냥 5번 다 해도 된다는 뜻
5번이란 방향이 4^5 = 2^10
위로 오리면  윗방향에서부터 바로 밑에것과 같으면 위에 합해주고 이동
반대로 아래로 내리면 아랫방향에서 부터 욋 방향과 같으면 아래에 합해주고 이동
400 -> 합하는 연산
400 -> 움직이는 연산
토탈케이스 1024
800*1024*(10->계산여유) 1-> 1000만언더 고
'''
import copy


def move(n, lst=[]):
    global move_lst
    if n ==5:
        move_lst.append(lst)
        return

    for i in range(4):
        move(n+1,lst+[i])


def move_block(d):
    if d == 0:
        for j in range(N):
            start = 0
            marker = False
            for i in range(N):
                if not marker and temp_matrix[i][j] == 0:
                    start = i
                    marker = True
                if marker and temp_matrix[i][j] != 0:
                    temp_matrix[start][j] = temp_matrix[i][j]
                    temp_matrix[i][j] = 0
                    start += 1
    elif d == 1:
        for i in range(N):
            start = 0
            marker = False
            for j in range(N):
                if not marker and temp_matrix[i][-1 - j] == 0:
                    start = -1 - j
                    marker = True
                if marker and temp_matrix[i][-1 - j] != 0:
                    temp_matrix[i][start] = temp_matrix[i][-1 - j]
                    temp_matrix[i][-1 - j] = 0
                    start -= 1
    elif d == 2:
        # 여기부터는 옮기는 과정
        for j in range(N):
            start = 0
            marker = False
            for i in range(N):
                if not marker and temp_matrix[-1 - i][j] == 0:
                    start = -1 - i
                    marker = True
                # 초기값 셋팅
                if marker and temp_matrix[-1 - i][j] != 0:
                    temp_matrix[start][j] = temp_matrix[-1 - i][j]
                    temp_matrix[-1 - i][j] = 0
                    start -= 1
        # 옮기기 끝
    elif d == 3:
        for i in range(N):
            start = 0
            marker = False
            for j in range(N):
                if not marker and temp_matrix[i][j] == 0:
                    start = j
                    marker = True
                # 초기값 셋팅
                if marker and temp_matrix[i][j] != 0:
                    temp_matrix[i][start] = temp_matrix[i][j]
                    temp_matrix[i][j] = 0
                    start += 1
        # 옮기기 끝


def play(order):
    global temp_matrix
    for o in range(5):
        d = order[o]
        # 한번밖에 안쓰니 안헷갈리게
        #URDL 더하는 과정
        if d == 0:
            #여기부터는 옮기는 과정
            move_block(d)
            for j in range(N):
                for i in range(N-1):
                    if temp_matrix[i][j] == temp_matrix[i+1][j]:
                        temp_matrix[i][j] *=2
                        temp_matrix[i+1][j]=0
            move_block(d)
            # 옮기기 끝
        elif d == 1:
            move_block(d)
            for i in range(N):
                for j in range(1,N):
                    if temp_matrix[i][-j] == temp_matrix[i][-j-1]:
                        temp_matrix[i][-j] *=2
                        temp_matrix[i][-j-1]=0
            move_block(d)
        elif d == 2:
            move_block(d)
            for j in range(N):
                for i in range(1, N):
                    if temp_matrix[-i][j] == temp_matrix[-i - 1][j]:
                        temp_matrix[-i][j] *= 2
                        temp_matrix[-i -1][j] = 0
            move_block(d)
        elif d == 3:
            move_block(d)
            for i in range(N):
                for j in range(N-1):
                    if temp_matrix[i][j] == temp_matrix[i][j+1]:
                        temp_matrix[i][j] *=2
                        temp_matrix[i][j+1]=0
            move_block(d)

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
move_lst=[]
move(0,[])
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
mx = 0

for ord in move_lst:
    temp_matrix = [x[:] for x in matrix]
    play(ord)
    mx = max(mx,max([max(x) for x in temp_matrix]))
print(mx)