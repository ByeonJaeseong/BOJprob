from collections import deque
def check(X):
    return 0<=X<200_001

def move(X):
    global length
    global N
    global count
    dq = deque()
    dq.append(X)
    length[X]=0
    while dq :
        value = dq.popleft()
        p1 =value+1
        p2 =value-1
        p3 =2*value
        lst = [p1, p2, p3]

        for i in lst:
            if check(i) and length[i]>=length[value]+1:
                length[i]=length[value]+1
                dq.append(i)
        if N==p1 and length[N]==length[value]+1:
            count+=1
        if N==p2 and length[N]==length[value]+1:
            count+=1
        if N==p3 and length[N]==length[value]+1:
            count+=1




M, N = map(int, input().split())
length = [100_001]*200_001
count = 0
move(M)
# print(length[:600])
if M==N:
    print(0)
    print(1)
else:
    print(length[N])
    print(count)