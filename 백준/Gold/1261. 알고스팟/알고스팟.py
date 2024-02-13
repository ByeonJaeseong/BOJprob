
def check(x,y):
    global M, N, visit
    return 0<=x<M and 0<=y<N and not visit[x][y]

N, M = map(int, input().split())
matrix=[list(map(int,input())) for _ in range(M)]
visit=[[False]*N for _ in range(M)]
lst = []
length=[[2_000_000_000] *N for _ in range(M)]
length[0][0]=0
visit[0][0]=True
current = (0, 0)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
st = set([])
st.add(current)
for _ in range(M):
    for _ in range(N):
        if current==(M-1, N-1): break
        x, y = current
        st.remove(current)
        # print(x,y)
        visit[x][y]=True
        for i in range(4):
            X = x+dx[i]
            Y = y+dy[i]
            if check(X,Y):
                length[X][Y] = min(length[X][Y], length[x][y]+matrix[X][Y])
                st.add((X,Y))
        temp_lst = list(st)
        mini = 2_000_000_000
        p = 0, 0
        for i in range(len(temp_lst)):
            x = temp_lst[i][0]
            y = temp_lst[i][1]
            if not visit[x][y] and length[x][y] < mini:
                mini = length[x][y]
                p, q = x, y
        current = (p, q)

print(length[M-1][N-1])