import math

def find(n):
    global group
    if group[n]!=n:
        group[n] = find(group[n])
    return group[n]

def union(a, b):
    global group
    group[find(b)] = find(a)

N = int(input())
matrix = [list(map(float, input().split())) for _ in range(N)]
group = [i for i in range(N+1)]
adj = []
for i in range(N):
    for j in range(i+1, N):
        dist = math.sqrt((matrix[i][0]-matrix[j][0])**2+(matrix[i][1]-matrix[j][1])**2)
        adj.append([i, j, dist])
adj.sort(key = lambda x : (x[2]))
# print(adj)
count = 0
if N!=1:
    for i in range(len(adj)):
        if find(adj[i][0])!=find(adj[i][1]):
            union(adj[i][0], adj[i][1])
            count += adj[i][2]
    print(count)
else:
    print(0)
