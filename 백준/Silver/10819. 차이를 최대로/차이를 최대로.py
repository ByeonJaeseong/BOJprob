def abs_sum(m, temp=-101, sm=0):
    #깊이, 방문 위치, 절댓값 차 첫번째, 절댓값 두개 뽑았는지, 총합
    global mx, N
    global lst, visit
    if m>=N:
        mx = max(sm, mx)
    else:
        for i in range(N):
            if not visit[i]:
                visit[i]=True
                if temp == -101:
                    abs_sum(m+1,lst[i],sm)
                else:
                    abs_sum(m+1,lst[i],sm+abs(temp-lst[i]))
                visit[i]=False



N = int(input())
lst = list(map(int, input().split()))
mx = -2000
visit = [False] * N
abs_sum(0)
print(mx)