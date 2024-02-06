'''
3 5 6 1 문제수 난이도 합 최소 최대 (가장 쉽고 어려운 문제의)난이도 차이
1 2 3
'''

def score(n=0, m=0, sm=0, sco=[]):
    global N,L,R,X
    global lst, visit
    global count
    if n>=N:
        if len(sco) >= 2 and sco[-1] - sco[0] >= X and L <= sum(sco) <= R:
            # print(sco, "추가되었습니다1")
            count += 1
        return
    # elif len(sco)>=2 and sco[-1]-sco[0]>=X and L<=sum(sco)<=R:
    #     print(sco, "추가되었습니다2")
    #     count+=1
    #     return
    else:
        for i in range(m, N):
            if not visit[i]:
                visit[i]=True
                if sm+lst[i]<=R:
                    score(n+1, i+1, sm+lst[i], sco+[lst[i]])
                score(n + 1, i + 1, sm, sco)
                visit[i]=False




N, L, R, X = map(int, input().split())
lst = list(map(int, input().split()))
# print(sum(lst))
visit = [False]*N
count = 0
lst.sort()
score()
print(count)