'''
연산할 수 있는 갯수 10!
backtracking으로 접근해도 충분히 풀림

'''
#1부터 시작해야함
def calcul(n, plus, minus, product, division, value):
    global mx, mn
    if n == N:
        mx =  max(mx, value)
        mn = min(mn, value)
        return

    if plus>0:
        calcul(n+1, plus-1, minus, product, division, value+lst[n])

    if minus>0:
        calcul(n + 1, plus, minus-1, product, division, value - lst[n])

    if product>0:
        calcul(n + 1, plus, minus, product-1, division, value*lst[n])

    if division>0:
        if value>=0:
            calcul(n + 1, plus, minus, product, division-1, value // lst[n])
        else:
            calcul(n + 1, plus, minus, product, division-1, -((-1*value) // lst[n]))

N = int(input())
lst = list(map(int, input().split()))
# 연산할 숫자
plus, minus, product, division = map(int, input().split())
mx = -2_000_000_001
mn = 2_000_000_001
calcul(1, plus, minus, product, division, lst[0])
print(mx)
print(mn)