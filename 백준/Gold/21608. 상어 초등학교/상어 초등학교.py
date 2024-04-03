'''
1.비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
2.1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
3.2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
구상 5분 -> 빡구현으로 구현하기러 함
시간 한명 배치할때 드는 최대 시간 20*20*4 -> 1600
총 배치 인원 400
토탈 640_000
'''
def check(x,y):
    return 0<=x<N and 0<=y<N

def locating(n, st = set([])):
    global class_room
    mx_friend = -1
    mx_empty = -1
    locx, locy = -1, -1
    for i in range(N):
        for j in range(N):
            if class_room[i][j]!=0:
                continue
            friend = 0
            empty = 0
            for k in range(4):
                X = i+dx[k]
                Y = j+dy[k]
                # 자기가 좋아하는 친구가 있으면
                if check(X,Y) and class_room[X][Y] in st:
                    friend +=1

                if check(X, Y) and class_room[X][Y] == 0 :
                    empty +=1
            if mx_friend < friend:
                # 자기가 좋아하는 친구가 많으면
                locx, locy = i, j
                mx_friend = friend
                mx_empty = empty
            elif mx_friend == friend:
                # 좋아하는 친구의 수가 같으면
                if mx_empty < empty:
                    locx, locy = i, j
                    mx_empty = empty
    class_room[locx][locy] = n

N = int(input())
matrix = [[] for _ in range(N**2)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
for i in range(N**2):
    temp = list(map(int, input().split()))
    matrix[i].append(temp[0])
    matrix[i].append(set(temp[1:]))
# print(matrix)
class_room = [[0]*N for _ in range(N)]
for i in range(N**2):
    locating(matrix[i][0], matrix[i][1])
# print(*class_room, sep='\n')
dic = {0:0, 1:1, 2:10, 3:100, 4:1000}
matrix.sort()
result = 0
for i in range(N):
    for j in range(N):
        temp = 0
        for k in range(4):
            X = i+dx[k]
            Y = j+dy[k]
            if check(X,Y) and class_room[X][Y] in matrix[class_room[i][j]-1][1]:
                temp+=1
        result+=dic[temp]
print(result)