from collections import deque

def dfs(K):
    global adj_lst
    global visit
    visit[K]=True
    print(K, end=" ")
    for i in sorted(adj_lst[K]):
        if not visit[i]:
            visit[i]=True
            dfs(i)
def bfs(K):
    global adj_lst
    global visit
    dq = deque()
    visit[K]=True
    dq.append(K)
    while dq :
        value = dq.popleft()
        for i in sorted(adj_lst[value]):
            if not visit[i]:
                visit[i]=True
                dq.append(i)
        print(value, end=" ")

M, N, K = map(int, input().split())
adj_lst = [[] for _ in range(M+1)]
visit = [False] * (M+1)
for i in range(N):
    P, Q = map(int, input().split())
    adj_lst[P].append(Q)
    adj_lst[Q].append(P)
# print(adj_lst)
dfs(K)
visit = [False] * (M+1)
print()
bfs(K)
