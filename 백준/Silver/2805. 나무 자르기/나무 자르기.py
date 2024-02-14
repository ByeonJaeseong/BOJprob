M, N = map(int, input().split()) # M 목재 #타겟값
lst = list(map(int, input().split()))
lst.sort()

s, e = 0, lst[M-1]
m = 0
while s<=e:
    m = (s+e)//2
    sm = sum([max(0, lst[i]-m) for i in range(M)])
    # print(m, sm)
    if sm==N:
        break
    elif sm<N:
        e = m - 1
    else:
        s = m + 1
sm = sum([max(0, lst[i]-m) for i in range(M)])
if sm<N:
    print(m-1)
else:
    print(m)