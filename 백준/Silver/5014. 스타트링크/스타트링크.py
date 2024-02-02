from collections import deque

def bfs(X):
    global G
    global U
    global D
    global F
    global visit
    global length
    dq = deque()
    dq.append(X)
    visit[X]=True
    while dq:
        value = dq.popleft()
        # print(value)
        # print(visit)
        if G in [value+U, value-D]:
            length[G]+=length[value]+1
            break
        # print(value+U, visit[value+U], length[value], length[value+U])
        if 0<(value+U)<=F and not visit[value+U]:
            visit[value+U] = True
            length[value+U]=length[value]+1

            dq.append(value+U)
        # print(value + U, visit[value + U], length[value], length[value + U])
        # print()
        # print(value - D, visit[value - D], length[value], length[value -D])
        if 0<(value-D)<=F and not visit[value-D]:
            visit[value-D] = True
            length[value-D]=length[value]+1
            dq.append(value-D)
        # print(value - D, visit[value - D], length[value], length[value - D])

F, S, G, U, D = map(int, input().split())
visit = [False]*(F+1)
visit[0] = True
length = [0]*(F+1)
bfs(S)
# print(length)
if S==G:
    print(0)
elif length[G]==0:
    print("use the stairs")
else:
    print(length[G])

