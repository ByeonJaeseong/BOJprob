from collections import deque
N = int(input())
dq = deque()
while N>0:
    if N % 2 ==0:
        dq.appendleft(N)
        N-=1
    else:
        dq.append(N)
        N-=1
print(*dq, sep=" ")