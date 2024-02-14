
N = int(input())
lst = list(map(int, input().split()))
dp = [1]*N
sub_lst = [[lst[i]] for i in range(N)]
for i in range(N):
    # print()
    for j in range(i+1, N):
        # print()
        if lst[j]>lst[i] and (dp[i] +1) > dp[j] :
            # print()
            sub_lst[j] = sub_lst[i]+[lst[j]]
        if lst[j]>lst[i]:
            dp[j]=max(dp[i]+1, dp[j])
rx = 0
mx = 0
for i in range(N):
   if mx<dp[i]:
       mx = dp[i]
       rx=i
print(mx)
print(*sub_lst[rx])
