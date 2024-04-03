'''
시작시간 1시 7분
일반 블록 적어도 하나, 일반 블록색 모두 같아야함
검은색 블록(-1) 포함 X, 무지개 블록(0) 상관 X
블록의 개수는 2보다 커야함
'''

from collections import deque

def check(x,y) : return 0<=x<N and 0<=y<N

def gravity():
    global matrix

    for j in range(N):
        lst = []
        for i in range(1,N+1):

            if matrix[-i][j] == -2: continue
            if matrix[-i][j] != -1:
                lst.append(matrix[-i][j])
            if matrix[-i][j] == -1:
                for _ in range(i-len(lst)-1):
                    lst.append(-2)
                lst.append(-1)
        for _ in range(N-len(lst)):
            lst.append(-2)
        for i in range(N):
            v = lst.pop()
            matrix[i][j] = v



N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
score = 0
while True:
    visit = [[False]*N for _ in range(N)]
    sx, sy, num_rainbow, mx, remove_block = 0, 0, 0, 0, set([])
    for i in range(N):
        for j in range(N):
            if not visit[i][j] and matrix[i][j]>0:
                rainbow = set([])
                block = set([])
                block.add((i,j))
                visit[i][j] = True
                dq = deque()
                dq.append((i,j))
                count = 1
                while dq:
                    x, y = dq.popleft()
                    for k in range(4):
                        X, Y = x+dx[k], y+dy[k]
                        if check(X,Y) and not visit[X][Y] and matrix[X][Y] in [0, matrix[i][j]]:
                            visit[X][Y] = True
                            dq.append((X,Y))
                            count+=1
                            block.add((X,Y))
                            if matrix[X][Y] == 0:
                                rainbow.add((X,Y))
                if count>mx:
                    mx, num_rainbow, sx, sy, remove_block = count, len(rainbow), i, j, block
                elif count == mx:
                    if num_rainbow < len(rainbow):
                        mx, num_rainbow, sx, sy, remove_block = count, len(rainbow), i, j, block
                    elif num_rainbow == len(rainbow):
                        if sx<i:
                            mx, num_rainbow, sx, sy, remove_block = count, len(rainbow), i, j, block
                        elif sx == i:
                            if sy<j:
                                mx, num_rainbow, sx, sy, remove_block = count, len(rainbow), i, j, block
                while rainbow:
                    x, y = rainbow.pop()
                    visit[x][y] = False
                    # 재활용

    if len(remove_block)>=2:
        score += len(remove_block)**2
    else: break
    while remove_block:
        x, y = remove_block.pop()
        matrix[x][y] = -2
    gravity()
    matrix = list(map(list, zip(*matrix)))[::-1]
    gravity()

print(score)