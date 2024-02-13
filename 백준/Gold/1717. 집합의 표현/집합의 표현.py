'''
0 a b -> a b 합치기
1 a b -> 같이 있는지 확인하기
'''

def find(x):
    global p
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(a,b):
    p[find(b)] = find(a)

M, N = map(int, input().split()) # M -> 집합의 개수
matrix = [list(map(int, input().split())) for _ in range(N)]
p = [ i for i in range(M+1)]
for i in range(N):
    if matrix[i][0]==0:
        union(matrix[i][1], matrix[i][2])
    else:
        if find(matrix[i][1])==find(matrix[i][2]):
            print("yes")
        else:
            print("no")