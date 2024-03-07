'''
코드 엎음
순수 heapq만 써서 관리할 예정
엎은 코드 1트 전체 5트 -> 시간초과
엎은 코드 2트 데이터 업데이트 하는 시간 및 초기화 하는시간 수정
엎은 코드 3트 list형을 tupel로 변환
엎은 코드 4트 함수 호출을 없앰
엎은 코드 5트 -> heap구조를 없ㅂ앰
'''
from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
# N 배열의 값, M 나무의 정보, K년이 지난 후
matrix = [list(map(int, input().split())) for _ in range(N)]
# 영양분 추가 정보
tree_init = [list(map(int, input().split())) for _ in range(M)]
tree = [(tree_init[i][2], tree_init[i][0]-1, tree_init[i][1]-1) for i in range(M)]
tree.sort()
dq = deque()
dq.extend(tree)
# print(dq)
# 나무의 초기 상태 저장하는 배열
nori = [[5]*N for _ in range(N)]
dx = (-1,-1,-1,0,0,1,1,1)
dy = (-1,0,1,-1,1,-1,0,1)
for _ in range(K):
    # tree 값에 따라서

    fall = []
    now_nori = [x[:] for x in matrix]
    repeat = len(dq)
    for _ in range(repeat):
        n, x, y = dq.popleft()
        # 봄 + 여름 로직 구현
        #영양소를 추간한 적이 없고 값이 더 크면
        if nori[x][y]>=n:
            nori[x][y] -= n
            dq.append((n+1, x, y))
            if (n+1)%5 == 0:
                fall.append((x,y))
        else:
            now_nori[x][y] += n//2
        # 여름 구현 끝
    while fall:
        p, q = fall.pop()
        for l in range(8):
            X = p + dx[l]
            Y = q + dy[l]
            if 0<=X<N and 0<=Y<N:
                dq.appendleft((1,X,Y))
    for i in range(N):
         for j in range(N):
             nori[i][j] += now_nori[i][j]
print(len(dq))