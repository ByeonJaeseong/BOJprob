from collections import deque

def check(X):
    global N
    return 0<=X<=N

def dfs(X):
    global N
    dq = deque()
    if X!=1:
        dq.append([X * X, "*"])
        dq.append([2*X,"+"])
        dq.append([1,"/"])
    else:
        dq.append([2 * X, "+"])


    result =""
    while dq and X!=N:
        value = dq.popleft()
        if value[0] == N:
            result = value[1]
            break
        # print(value[0])
        if check(value[0]**2) and value[0]**2==N and value[0]!=1:
            result = value[1]+"*"
            break
        elif check(value[0]**2) and value[0]**2!=N and value[0]!=1:
            dq.append([value[0] ** 2, value[1] + "*"])

        if check(2*value[0]) and value[0]*2==N:
            result = value[1]+"+"
            break
        elif check(2*value[0]) and 2*value[0]!=N:
            dq.append([value[0] * 2, value[1] + "+"])


    if X==N:
        print(0)
    elif N==1:
        print("/")
    elif result=="":
        print(-1)
    else:
        print(result)

M,N = map(int, input().split())
dfs(M)