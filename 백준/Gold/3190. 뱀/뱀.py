'''
1.먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
2.만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
3.만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
4.만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
N 보드크기 K 사과개수
X초 뱀위치 0, 0 오른쪽 향해 있음 L 반시계 R 시계
'''

from collections import deque

def check(x,y):
    return 0<=x<N and 0<=y<N

N = int(input())
K = int(input())
apple_loc = [list(map(int, input().split())) for _ in range(K)]
apple =set([])
for i in range(K):
    apple.add((apple_loc[i][0]-1, apple_loc[i][1]-1))
L = int(input())
order = [list(input().split()) for _ in range(L)]
INF = 30_000_000
order = [[int(order[i][0]), order[i][1]] for i in range(L)]+[[INF, 'D']]
# print(*order, sep='\n')
snake = deque()
# 뱀은 꼬리 하나만 사라지고 머리 하나만 늘어나는 형태
# 즉 꼬리 하나를 빼주고 머리를 늘려주는 형태를 만들려면 deque을 쓰자
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
d = 1
snake.append((0,0))
snake_check = set([])
snake_check.add((0,0))
count = 0
for i in range(L+1):
    marker = False
    while True:
         # print(snake, snake_check)
         count +=1
         tx, ty = snake[0]
         x,y = snake[-1]
         X,Y = x+dx[d], y+dy[d]
         snake.append((X,Y))
         if (X,Y) in snake_check or not check(X,Y):
             marker = True
             break
         #부딛치면 끊기
         if (X,Y) in apple:
             apple.remove((X,Y))
             snake_check.add((X,Y))
         else:
             snake.popleft()
             snake_check.remove((tx,ty))
             snake_check.add((X,Y))
         if order[i][0]==count:
             break
    if marker:
        break
    if order[i][1] == 'L':
        d = (d-1)%4
    else:
        d = (d+1)%4
print(count)
