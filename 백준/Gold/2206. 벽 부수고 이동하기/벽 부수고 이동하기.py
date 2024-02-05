from collections import deque

def check(x,y) :
    return 0<=x<M and 0<=y<N
# visit 배열을 안 쓸거구 뒤에 벽 부시고 온 것이면
def dfs(x, y):
    global matrix
    global M
    global dx
    global dy
    global length
    dq = deque()
    dq.append([x,y])
    if matrix[x][y]==0:
        while dq:
            # for i in range(M):
            #     print(length[0][i])
            # # print("실행되었습니다")
            value = dq.popleft()
            for i in range(4):
                X = value[0]+dx[i]
                Y = value[1]+dy[i]
                if check(X,Y) and matrix[X][Y]==0 and length[0][value[0]][value[1]]+1<length[0][X][Y]:
                    # print("시일행")
                    length[0][X][Y] = length[0][value[0]][value[1]]+1
                    dq.append([X,Y])
    else:
        while dq:
            value = dq.popleft()
            for i in range(4):
                X = value[0]+dx[i]
                Y = value[1]+dy[i]
                if check(X,Y) and matrix[X][Y]==0 and length[1][value[0]][value[1]]+1<length[0][X][Y] and length[1][value[0]][value[1]]+1<length[1][X][Y]:
                    length[1][X][Y] = length[1][value[0]][value[1]]+1
                    dq.append([X,Y])

M, N = map(int, input().split())
matrix = [list(map(int, input()[0:N])) for _ in range(M)]
length = [[[M*N] * N for _ in range(M)]for _ in range(2)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
length[0][0][0]=0
dfs(0,0)
for i in range(M):
    for j in range(N):
        if matrix[i][j]==1:
            temp = M * N
            for k in range(4):
                X = i+dx[k]
                Y = j+dy[k]
                if check(X,Y):
                    temp = min(temp,length[0][X][Y])
            if temp!=M*N:
                length[1][i][j] = temp+1
                dfs(i,j)

# for i in range(M):
#     print(matrix[i])
#
# for i in range(M):
#     print(length[i])
#
# print()
#
# for i in range(M):
#     print(length1[i])

mn = min(length[0][M-1][N-1], length[1][M-1][N-1])
if mn==M*N:
    print(-1)
else:
    print(mn+1)