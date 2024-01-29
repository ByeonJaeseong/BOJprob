N = int(input())
lst = []
count = 1
for i in range(N):
    lst.append(int(input()))

init = lst.pop()
for i in range(1, N):
    value = lst.pop()
    if init < value:
        init = value
        count+=1
print(count)