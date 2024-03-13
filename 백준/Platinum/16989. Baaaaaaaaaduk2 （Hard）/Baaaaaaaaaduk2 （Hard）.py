'''
IDEA 전체를 1로 둘러싼 다음에
2가 0과 마주치지 않는 군락의 갯수 세기
'''
from collections import deque


#돌 갯수 새기

def bfs():
    global M,N,matrix,dx,dy,z2,z1
    visit = [[False] * (N + 2) for _ in range(M + 2)]
    count = 0
    for i in range(1, M+1):
        for j in range(1, N+1):
            ## 전체를 돌면서 2찾기
            temp = 0
            if not visit[i][j] and matrix[i][j]==2:
                dq = deque()
                dq.append((i,j))
                visit[i][j] = True
                temp+=1
                zeros = set([])
                marker = False
                while dq:
                    value = dq.popleft()
                    for k in range(4):
                        X = value[0]+dx[k]
                        Y = value[1]+dy[k]
                        if not visit[X][Y] and matrix[X][Y]==2:
                            temp+=1
                            visit[X][Y]=True
                            dq.append((X,Y))
                        elif matrix[X][Y]==0:
                            zeros.add((X,Y))
                            # print((i,j),(X,Y))
                        ## 2의 갯수를 세고 0과 접촉한다면 제거시켜버리기
                        ## 단 중복적으로 카운트 안하도록 2의 개수는 전부 세기
                if len(zeros)==2:
                    zeros = list(zeros)
                    zeros.sort()
                    zeros = tuple(zeros)
                    if zeros in z2:
                        z2[zeros] = z2[zeros]+temp
                    else:
                        z2[zeros] = temp
                elif len(zeros)==1:
                    zeros = tuple(zeros)
                    if zeros in z1:
                        z1[zeros] = z1[zeros]+temp
                    else:
                        z1[zeros] = temp
                elif len(zeros) == 0:
                    z0.append(temp)


                count+=temp
    return count




M, N = map(int, input().split())
matrix =[[1]*(N+2)]+ [[1]+list(map(int, input().split()))+[1] for _ in range(M)]+[[1]*(N+2)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
mx = 0
mark = [[False]*(N+2) for _ in range(M+2)]
# data 받기
z0 = []
z1 = dict()
z2 = dict()
bfs()
# print(z2)
# print(z1)
# print(z0)
z2_kye = [k for k in z2.keys()]
# print(z2_kye[0][0])
z1_kye = [k for k in z1.keys()]
# print(z1_kye[0][0])
z1_value = [v for v in z1.values()]
# print(z1_value)
for i in range(len(z2)):
    for j in range(len(z1_value)):
        if z1_kye[j][0] == z2_kye[i][0] or z1_kye[j][0] == z2_kye[i][1]:
            z2[z2_kye[i]]=z2[z2_kye[i]]+z1[z1_kye[j]]
if z2:
    mx = max([ v for v in z2.values()])
else:
    mx=0
if z1:
    mx = max(mx,*z1_value)

for i in range(len(z1_value)):
    for j in range(i+1, len(z1_value)):
        mx = max(mx, z1_value[i]+z1_value[j])

print(mx+sum(z0))

