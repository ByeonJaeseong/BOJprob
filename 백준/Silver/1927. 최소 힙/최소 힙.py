import heapq
import sys
input = sys.stdin.readline
heap = []
N =int(input())
heapq.heapify(heap)
matrix = [int(input()) for _ in range(N)]
for i in range(N):
    k = matrix[i]
    if k ==0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,k)
