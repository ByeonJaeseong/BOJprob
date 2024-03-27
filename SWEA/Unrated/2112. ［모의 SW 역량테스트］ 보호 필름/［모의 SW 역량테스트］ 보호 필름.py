def test_board(matrix=[]):
    for j in range(W):
        count = 0
        now = -1
        mx = 0
        for i in range(D):
            if now != matrix[i][j]:
                now = matrix[i][j]
                mx = max(mx, count)
                count=1
            else:
                count+=1
        mx = max(mx, count)
        if mx<K:
            return False
    return True


TC = int(input())

for tc in range(1, TC+1):
    D, W, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(D)]
    test = []
    checker = test_board(board)
    stack = []
    if checker:
        mn = 0
    else:
        stack.append((0, 0, []))
        mn = D-1
    while stack:
        n, c, lst = stack.pop()
        if mn <= c: continue
        if mn == 0:break
        if n == D-1 or c <= K:
            temp = [b[:] for b in board]
            for i in lst:
                p, q = i
                for j in range(W):
                    temp[p][j] = q
            marker = test_board(temp)
            if marker:
                mn = min(mn, c)
                continue
        if c < K and n < D:
            stack.append((n + 1, c + 1, lst + [(n,0)]))
            stack.append((n + 1, c + 1, lst + [(n,1)]))
            stack.append((n + 1, c, lst))

    print(f'#{tc} {mn}')