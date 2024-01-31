from collections import deque

def bfs(x) :
    global lst
    global visit
    global length
    global end
    dq = deque()
    dq.append(x)
    visit[x]=True
    while dq :
        value = dq.popleft()
        if value == end:
            break
        for i in lst[value]: # 인접행렬 불러오기
            if not visit[i]:
                length[i] = length[value]+1
                visit[i]=True
                dq.append(i)



N = int(input()) # 사람수
start, end = map(int, input().split())
M = int(input()) # 엣지 수
lst = [[] for _ in range(N+1)]
visit = [False]*(N+1)
length = [0]*(N+1)
for i in range(M):
    P, Q = map(int, input().split())
    lst[P].append(Q)
    lst[Q].append(P)
bfs(start)
# print(visit)
# print(length)
if length[end]:
    print(length[end])
else:
    print(-1)