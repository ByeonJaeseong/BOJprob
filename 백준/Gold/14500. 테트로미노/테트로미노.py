def solve(blocks, sm, cnt):
    global ans

    if sm + (4 - cnt) * mx <= ans:
        return

    if cnt == 4:
        ans = max(ans, sm)
        return

    # blocks.sort()
    # if str(blocks) in v_set:
    #     return
    # else:
    #     v_set.add(str(blocks))

    for b in blocks:
        bi, bj = divmod(b, M)
        for d in range(3):
            ni, nj = bi + di[d], bj + dj[d]
            if not (0 <= ni < N and 0 <= nj < M): continue
            if v[ni][nj]: continue

            v[ni][nj] = 1
            solve(blocks + [ni * M + nj], sm + arr[ni][nj], cnt+1)
            v[ni][nj] = 0

    return

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
mx = max([max(a) for a in arr])
ans = 0
# v_set = set()
v = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        v[i][j] = 1
        solve([i * M + j], arr[i][j], 1)
print(ans)
