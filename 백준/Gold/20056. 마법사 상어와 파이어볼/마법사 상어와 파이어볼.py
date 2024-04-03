''''
ouput : total weight of fireball
N : # size of matrix
M : # of fireball
K : # of order
loc x, loc y, measure, direction, speed
dir : clock wise
time complexity :
searching time 2500  * 1000
rule:
1.모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
1-1이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
2.이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
    2-1 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
    2-2 파이어볼은 4개의 파이어볼로 나누어진다.
    2-3 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
        2-3-1질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
        2-3-2속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
        2-3-3합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고,
            홀수랑 짝수가 섞여 있는 경우 1, 3, 5, 7이 된다.
        2-3-4질량이 0인 파이어볼은 소멸되어 없어진다.
'''

N, M, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(M)]
lst = [ [lst[i][0]-1, lst[i][1]-1] + lst[i][2:] for i in range(M)]
# print(lst)
matrix = [[[] for _ in range(N)] for _ in range(N)]
# 1 ~N까지임을 조심
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
for _ in range(K):
    # print(lst)

    #1.모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
    #1-1이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
    while lst:
        rx, ry, m, s, d = lst.pop()
        rx = (rx+s*dx[d])%N
        ry = (ry+s*dy[d])%N
        # print(rx, ry, m, d, s)
        #이동한 후 로케이션
        matrix[rx][ry].append([rx,ry,m,s,d])
    # 이동완료
    # 여기까지는 시간 2500
    # 파이어볼 합하기
    '''
    2.이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
    2-1 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
    2-2 파이어볼은 4개의 파이어볼로 나누어진다.
    2-3 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
        2-3-1질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
        2-3-2속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
        2-3-3합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고,
            홀수랑 짝수가 섞여 있는 경우 1, 3, 5, 7이 된다.
        2-3-4질량이 0인 파이어볼은 소멸되어 없어진다.
    '''
    for i in range(N):
        for j in range(N):
            if len(matrix[i][j])==0: continue
            if len(matrix[i][j])==1:
                temp_lst =matrix[i][j].pop()
                lst.append(temp_lst)
                # 한개인 경우
            else:
                measure = 0
                speed = 0
                numbers = len(matrix[i][j])
                odd, even = 1, 1

                for _ in range(numbers):
                    temp_lst = matrix[i][j].pop()
                    measure += temp_lst[2]
                    speed += temp_lst[3]
                    odd *= temp_lst[4]
                    even *= (temp_lst[4]+1)
                # odd, even 중 하나라도 홀수라면
                measure = measure//5
                speed = speed//numbers
                if measure == 0: continue
                if (odd%2)==1 or (even%2)==1:
                    lst.append([i,j,measure,speed,0])
                    lst.append([i, j, measure, speed,2])
                    lst.append([i, j, measure, speed,4])
                    lst.append([i, j, measure, speed,6])
                else:
                    lst.append([i, j, measure, speed,1])
                    lst.append([i, j, measure, speed,3])
                    lst.append([i, j, measure, speed,5])
                    lst.append([i, j, measure, speed,7])

sm = 0
for i in range(len(lst)):
    sm += lst[i][2]
print(sm)