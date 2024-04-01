'''
문제 시작 3시 16분
시작 21분 틀렸습니다.
'''

def check(x,y) : return 0<=x<N and 0<=y<N

N, M, K = map(int, input().split())
nourisous = [list(map(int, input().split())) for _ in range(N)]
input_tree = [list(map(int, input().split())) for _ in range(M)]
board = [[5]*N for _ in range(N)]
tree = [[[] for _ in range(N)] for _ in range(N)]
for x, y, a in input_tree:
    tree[x-1][y-1].append(a)
dx = (-1, -1, -1, 0, 0, 1, 1, 1)
dy = (0 ,1, -1, 1, -1, 0, 1, -1)
for _ in range(K):
    # 봄 구현
    # print(*tree,sep='\n')
    # print()
    fall = []
    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                tree[i][j].sort()
                for k in range(len(tree[i][j])):
                    if tree[i][j][k]<=board[i][j]:
                        board[i][j] -= tree[i][j][k]
                        tree[i][j][k] +=1
                        if tree[i][j][k] % 5 == 0:
                            fall.append((i,j))
                    else:
                        for _ in range(len(tree[i][j])-k):
                            board[i][j] += tree[i][j].pop()//2
                        break
    for i in range(len(fall)):
        x, y = fall[i]
        for j in range(8):
            X, Y = x+dx[j], y+dy[j]
            if check(X,Y):
                tree[X][Y].append(1)
    for i in range(N):
        for j in range(N):
            board[i][j]+=nourisous[i][j]

count = 0
# print(*tree, sep='\n')
for i in range(N):
    for j in range(N):
        count+=len(tree[i][j])
print(count)