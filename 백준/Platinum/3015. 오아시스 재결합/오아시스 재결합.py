from collections import deque
N = int(input())
dq = deque()
count  = 0
for _ in range(N):
    value = int(input())
    if not dq:
        dq.append([value,1])
        continue
    while dq:
        marker = True
        if dq[-1][0]<value:
            p, q = dq.pop()
            count+=q
        elif dq[-1][0] == value:
            if len(dq)==1:
                count+=dq[-1][1]
                break
            else:
                count+=dq[-1][1]
                count+=1
                break
        else:
            count+=1
            break
    # print(value, dq, count)
    if not len(dq):
        dq.append([value,1])
        continue

    if dq[-1][0]==value:
        p, q = dq.pop()
        dq.append([p, q+1])
    else:
        dq.append([value,1])
print(count)