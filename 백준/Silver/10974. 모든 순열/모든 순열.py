def printing(n,lst=[]):
    global N
    if n>=N:
        print(*lst)
    else:
        for i in range(N):
            if not visit[i]:
                visit[i]=True
                printing(n+1, lst+[i+1])
                visit[i]=False

N = int(input())
visit = [False]*N
printing(0)