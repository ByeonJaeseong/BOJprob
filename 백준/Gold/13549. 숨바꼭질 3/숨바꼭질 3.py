from collections import deque
M, N = map(int, input().split())
dot = [100_001]*100_001
dq = deque()
dq.append(M)
dot[M]=0
while M!=N:
    M = dq.pop()
    if 2*M<100_001:
        if dot[2*M]==100_001 or dot[M]<dot[2*M]:
            dot[2*M]=dot[M]
            dq.appendleft(2*M)

    if M>0:
        if dot[M-1]==100_001 or dot[M-1]>dot[M]+1:
            dot[M-1]=dot[M]+1
            dq.appendleft(M-1)

    if M<100_000:
        if dot[M+1]==100_001 or dot[M+1]>dot[M]+1:
            dot[M+1]=dot[M]+1
            dq.appendleft((M+1))

    if(M==N):
        break
print(dot[N])