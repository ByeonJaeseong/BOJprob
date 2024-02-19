'''
PQ를 바탕으로 짜야지 시간통과 되는 문제

'''
import heapq

def dijkstra(start):
    global M,N,X
    dijk = [2_000_000_000] * (N + 1)
    visit = [False] * (N + 1)
    dijk[start] = 0
    heap = []
    heapq.heappush(heap, [0,start])
    while heap:
        # print(heap)
        value = heapq.heappop(heap)

        if value[1]==X and start!=X: break

        if visit[value[1]] and start!=X: continue

        visit[value[1]]=True
        for j in range(1, N+1):
            if matrix1[value[1]][j] == 0: continue
            if visit[j] : continue
            dijk[j] = min(dijk[j], dijk[value[1]] + matrix1[value[1]][j])
            heapq.heappush(heap, [dijk[j],j])
    # print(dijk)
    return dijk

N, M, X = map(int,input().split())\
#M 도로 갯수 N 마을 갯수
matrix = [list(map(int, input().split())) for _ in range(M)]
matrix1 = [[0]*(N+1) for _ in range(N+1)]
length = [0]*(N+1)
#인접행렬 셋팅
for i in range(M):
    x,y,l = matrix[i]
    matrix1[x][y]=l
# for i in range(N):
#     print(matrix1[i])
for i in range(1,N+1):
    dijk = [2_000_000_000]*(N+1)
    visit = [False]*(N+1)
    result = dijkstra(i)
    # print(result)
    if i == X:
        for i in range(N+1):
            length[i] += result[i]
    else:
        length[i] += result[X]
print(max(length[1:]))




