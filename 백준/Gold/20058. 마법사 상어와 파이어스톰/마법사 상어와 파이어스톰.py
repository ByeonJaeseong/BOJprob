'''
ROTATION만 잘 구상하면 크게 어려울 것 없는 문제
빡구현으로 하되 무조건 녹는점들이 있음에 유의
'''
from collections import deque

def check(x,y):
    return 0<=x<2**N and 0<=y<2**N


def matrix_copy(x,y,gap):
    temp=[[] for _ in range(gap)]
    for i in range(gap):
        for j in range(gap):
            temp[i].append(matrix[x+i][y+j])

    rt_lst = [[] for _ in range(gap)]
    for i in range(gap):
        lst = temp[gap-1-i]
        # print(lst)
        for j in range(gap):
            rt_lst[j].append(lst[j])
    # print()
    return rt_lst
# 행렬 맞춤 복사 끝

def rotation(L):
    global matrix
    gap = 2**L
    for i in range(0,2**N,gap):
        for j in range(0,2**N,gap):
            temp = matrix_copy(i,j,gap)
            # print(*temp,sep='\n')
            # print()
            for p in range(0, gap):
                for q in range(0, gap):
                    matrix[i+p][j+q] = temp[p][q]

def melting():
    lst = []
    for i in range(2**N):
        for j in range(2**N):
            count =0
            if matrix[i][j]==0:continue
            for k in range(4):
                X = i + dx[k]
                Y = j + dy[k]
                if not check(X,Y):continue
                if matrix[X][Y] != 0:
                    count +=1
            # print(count)
            if count<=2:
                lst.append((i,j))
    return lst



N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(2**N)]
order = list(map(int, input().split()))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(len(order)):
    rotation(order[i])
    # print(*matrix, sep='\n')
    # print()
    lst = melting()
    for j in range(len(lst)):
        x, y = lst[j]
        matrix[x][y]-=1
mx = 0
visit = [[False]*2**N for _ in range(2**N)]
for i in range(2**N):
    for j in range(2**N):
        if matrix[i][j]==0:continue
        count = 1
        if not visit[i][j] and matrix[i][j]!=0:
            dq = deque()
            dq.append((i,j))
            visit[i][j]=True
            while dq:
                p, q = dq.popleft()
                for i in range(4):
                    X = p+dx[i]
                    Y = q+dy[i]
                    if check(X,Y) and not visit[X][Y] and matrix[X][Y]!=0:
                        visit[X][Y]=True
                        count+=1
                        dq.append((X,Y))
        mx = max(mx,count)

print(sum([sum(i) for i in matrix]))
print(mx)