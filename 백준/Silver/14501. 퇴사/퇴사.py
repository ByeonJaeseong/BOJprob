'''
전형적인 그리디 문제라 생각했는데
그리디 문제가 아니라 백트래킹 문제인듯
'''

def work(n,price):
    global mx
    if n==N:
        mx = max(mx, price)
        return

    if n+matrix[n][0]<=N:
        work(n+matrix[n][0], price+matrix[n][1])
    work(n + 1, price)


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
mx = 0
work(0,0)
print(mx)
