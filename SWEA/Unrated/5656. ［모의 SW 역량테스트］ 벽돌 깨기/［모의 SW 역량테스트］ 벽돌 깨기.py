from collections import deque

def check(x, y) : return 0<=x<M and 0<=y<N

def combination(lst = []):
    if len(lst) == K:
        play(lst)
        return
    for i in range(N):
        combination(lst+[i])

def play(lst = []):
    global mn
    if mn == 0 : return
    count = 0
    board = [m[:] for m in matrix]
    for i_ in range(len(lst)):
        if sum([sum(b) for b in board]) == 0 : break
        x = lst[i_]
        target, ran = -1, -1
        for i in range(M):
            if board[i][x] != 0:
                target, ran = i, board[i][x]
                break

        if target == -1:
            continue
        dq = deque()
        next_dq = deque()
        dq.append((target, x, board[target][x]))
        board[target][x] = 0

        while dq or next_dq:
            p, q, v = dq.popleft()
            # print(*board, sep='\n')
            # print()
            for i in range(1,v):
                for j in range(4):
                    X, Y = p+dx[j]*i, q+dy[j]*i
                    if check(X,Y) and board[X][Y]>0:
                        next_dq.append((X,Y, board[X][Y]))
                        board[X][Y] = 0

            if not dq:
            # 중력작용 끝
                dq, next_dq = next_dq, dq
                # if lst == [2, 2, 6]:
                #     print(*board,sep='\n')
                #     print(dq, next_dq)
        for j in range(N):
            lst_ = []
            for i in range(M):
                if board[i][j] != 0:
                    lst_.append(board[i][j])
            # lst_.reverse()
            for i in range(1, M + 1):
                if lst_:
                    v = lst_.pop()
                    board[-i][j] = v
                    continue
                else:
                    board[-i][j] = 0
    for i in range(M):
        for j in range(N):
            if board[i][j]>0:
                count+=1
    mn = min(mn, count)





TC = int(input())
for tc in range(1,TC+1):
    K, N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(M)]
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    mn = 1_000_000_000
    combination([])
    print(f'#{tc} {mn}')