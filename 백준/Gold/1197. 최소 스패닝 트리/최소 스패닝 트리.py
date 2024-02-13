
def find(n):
    global group
    # print(n)
    if group[n]!=n:
        group[n] = find(group[n])
    return group[n]

def union(a, b):
    global group
    group[find(b)] = find(a)

M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
group = [i for i in range(M+1)]
matrix.sort(key = lambda x : (x[2]))
count = 0
breaker = 0
for i in range(N):
    if find(matrix[i][0])!=find(matrix[i][1]):
        union(matrix[i][0], matrix[i][1])
        count += matrix[i][2]
        breaker+=1
    if breaker==M-1:
        break
print(count)