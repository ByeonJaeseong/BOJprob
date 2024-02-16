M, N = map(int, input().split())
lst = [int(input()) for _ in range(M)]
lst.sort(reverse=True)
count =0
for i in range(M):
    while lst[i]<=N:
        N-=lst[i]
        count+=1
print(count)