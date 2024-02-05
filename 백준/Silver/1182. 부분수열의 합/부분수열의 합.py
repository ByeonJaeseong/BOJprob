'''5 0
-7 -3 -2 5 8
'''

def sub_sm(n, m, temp_sm):
    global M
    global N
    global visit
    global lst
    global sm
    global count
    # print(visit, temp_sm)
    if n>=M:
        return
    else:
        if temp_sm==sm:
            count+=1
        for i in range(m+1,M):
            if not visit[i]:
                visit[i]=True
                temp_sm+=lst[i]
                sub_sm(n+1,i, temp_sm)
                temp_sm-=lst[i]
                visit[i]=False

M, N = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
visit = [False]*M
count = 0
sm = N
for i in range(M):
    visit[i]=True
    sub_sm(i, i, lst[i])
    # print(count)
print(count)