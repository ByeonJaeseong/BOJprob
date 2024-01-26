M, N = map(int, input().split())
lst=list(map(int, input().split()))
# print(lst)
count = 0
for i in range(M-2):
    for j in range(i+1, M-1):
        for k in range(j+1, M):
            # print(i, j, k, lst[i], lst[j], lst[k])
            # print(N-lst[i]+lst[j]+lst[k], N-count)
            if 0 <= N-(lst[i]+lst[j]+lst[k])<=N-count:
                count= lst[i]+lst[j]+lst[k]
                # print(("실행되었습니다."))
print(count)