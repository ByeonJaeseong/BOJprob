def dfs(x):
    global visit
    global adj
    global count
    if not visit[x]:
        visit[x]=True
        count +=1
        for i in adj[x]:
            if not visit[i]:
                dfs(i)


M = int(input()) # 컴퓨터수
N = int(input()) # 이어진 컴퓨터 수
adj = [[] for _ in range(101)] # 인접 리스트
visit = [False] * 101
count = 0
for i in range(N):
    P, Q = map(int, input().split())
    adj[P].append(Q)#인접행렬 업데이트
    adj[Q].append(P)  # 인접행렬 업데이트
    #시작점 0 끝점 99
# print(adj)
dfs(1)
print(count-1)