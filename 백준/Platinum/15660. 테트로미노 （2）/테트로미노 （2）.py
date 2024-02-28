'''ㅋㅋㅋㅋㅋㅋㅋ 82%에서 틀렸네'''

def check(x,y):
    return 0<=x<M and 0<=y<N

def tet(n, sum, total=None):
    # print(total)
    if total is None:
        total = []
    global mx, visit, temp, mx_loc, double_mx
    if n==4:
        if mx < sum:
            if len(set(mx_loc).intersection(total))==0:
                double_mx = mx + sum
            mx = max(mx,sum)
            mx_loc = total
        #
        if double_mx<mx+sum:
            temp.append([sum,total])
        return sum
    for t in range(len(total)):
        for i in range(4):
            X = total[t][0] + dx[i]
            Y = total[t][1] + dy[i]
            if check(X,Y) and not visit[X][Y]:
                visit[X][Y] = True
                tet(n+1,sum+matrix[X][Y], total+[(X,Y)])
                visit[X][Y] = False



M, N = map(int, input().split())
matrix =  [list(map(int, input().split())) for _ in range(M)]
visit = [[False]*N for _ in range(M)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
mx = 0
double_mx = sum(matrix[0][0:4])+sum(matrix[1][0:4])
mx_loc = []
temp = []

# print(checker)
for i in range(M):
    for j in range(N):
        visit[i][j]=True
        tet(1, matrix[i][j], [(i,j)])
# print(temp)
temp.sort()
start = 0
for i in range(len(temp)):
    if temp[-1][0]+temp[i][0]>=mx:
        start = i
        break
for i in range(max(0,len(temp)-1000), len(temp)):
    for j in range(i+1, len(temp)):
        if len(set(temp[i][1]).intersection(temp[j][1]))==0:
            mx= max(temp[i][0]+temp[j][0], mx)
print(mx)