'''
3 5 6 1 문제수 난이도 합 최소 최대 (가장 쉽고 어려운 문제의)난이도 차이
1 2 3
'''

def score(n=0, sm=0, ln=0, mx=0, mn=0):
    global N,L,R,X
    global lst, visit
    global count
    if n>=N:
        if ln >= 2 and mx-mn >= X and L <= sm <= R:
            # print(ln, mx, mn)
            count += 1
        return
    elif sm>R:
        return
    else:
            if ln == 0:
                score(n+1, lst[n], 1, lst[n], lst[n])
            else:
                score(n + 1,  sm+lst[n], ln+1, lst[n], mn)
            score(n + 1,  sm, ln, mx, mn)





N, L, R, X = map(int, input().split())
lst = list(map(int, input().split()))
# print(sum(lst))
visit = [False]*N
count = 0
lst.sort()
score()
print(count)