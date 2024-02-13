import math
def sPrime(n, prime):
    global N, result
    if n==N:
        result.append(prime)
    else:
        if is_prime(prime*10+1):
            sPrime(n+1, prime*10+1)

        if is_prime(prime * 10 + 3):
            sPrime(n + 1, prime * 10 + 3)

        if is_prime(prime * 10 + 7):
            sPrime(n + 1, prime * 10 + 7)

        if is_prime(prime * 10 + 9):
            sPrime(n + 1, prime * 10 + 9)


def is_prime(n):
    sq_n = int(math.sqrt(n))
    visit = [False]*(sq_n+1)
    visit[0], visit[1] = True, True
    marker = True
    for i in range(sq_n+1):
        if not visit[i]:
            if n%i==0:
                marker = False
                break
            else:
                for j in range(i, sq_n+1):
                    if j%i==0:
                        visit[j]=True
    return marker


N = int(input())
result = []
sPrime(1,2)
sPrime(1,3)
sPrime(1,5)
sPrime(1,7)
result.sort()
for i in result:
    print(i)