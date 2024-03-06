N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [0, -1 ,-1, -1, 0, 1, 1, 1]
dj = [-1, -1, 0, 1, 1, 1, 0, -1]
s4_i = [-1, -1, 1, 1]
s4_j = [-1, 1, 1, -1]

from collections import deque
cloud = deque()
cloud.append((N-1, 0))
cloud.append((N-1, 1))
cloud.append((N-2, 0))
cloud.append((N-2, 1))


visited = [[0]*N for _ in range(N)]


for a in range(1, M+1):
    d, s = map(int, input().split())
    d -= 1

    many = len(cloud)

    for _ in range(many):
        ci, cj = cloud.popleft()
        ci = (ci+s*di[d]) % N
        cj = (cj+s*dj[d]) % N
        visited[ci][cj] = a
        # cloud[i][0] = (cloud[i][0] + s*di[d]) % N
        # cloud[i][1] = (cloud[i][1] + s*dj[d]) % N

        arr[ci][cj] += 1


    for i in range(N):
        for j in range(N):
            if visited[i][j] == a:
                cnt = 0
                for d in range(4):
                    ni, nj = i + s4_i[d], j + s4_j[d]
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > 0:
                        cnt += 1
                arr[i][j] += cnt

    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and visited[i][j] != a:
                arr[i][j] -= 2
                cloud.append((i, j))





    # for i in range(many):
    #     cnt = 0
    #     ci, cj = cloud[i][0], cloud[i][1]
    #     for d in range(4):
    #         ni, nj = ci+s4_i[d], cj+s4_j[d]
    #         if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > 0:
    #             cnt += 1
    #
    #     arr[cloud[i][0]][cloud[i][1]] += cnt

    #
    # new = []
    # many = 0
    #
    # for i in range(N):
    #     for j in range(N):
    #        if arr[i][j] >= 2 and [i, j] not in cloud:
    #            new.append([i, j])
    #            arr[i][j] -= 2
    #            many += 1
    #
    #
    # cloud = new



ans = 0
for i in range(N):
    for j in range(N):
       ans += arr[i][j]

print(ans)