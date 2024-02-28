import heapq

M, N = map(int ,input().split())
lst =list(map(int, input().split()))
charge = []
lst.sort()
charge.append(lst.pop())
time = 0
while lst:
    if len(charge) <N:
        charge.append(lst.pop())
    else:
        heapq.heapify(charge)
        value = heapq.heappop(charge)
        for i in range(len(charge)):
            charge[i]-=value
        time += value
charge.sort()
time += charge[-1]
print(time)
