M, N = map(int, input().split())
lst = [int(input()) for _ in range(M)]
lst.sort(reverse=True)
count =0
for i in range(M):
    if lst[i]<=N:
        count+=N//lst[i]
        N= N%lst[i]
print(count)