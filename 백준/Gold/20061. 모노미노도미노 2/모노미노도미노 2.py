'''
모노미노 도미노
시작 2시56분
제출
'''

from collections import deque

N = int(input())
order = [list(map(int, input().split())) for _ in range(N)]
# t, x, y -> t=1 1*1 t=2 1*2 t=3 2*1
green = deque()
blue = deque()
for _ in range(6):
    green.append([0, 0, 0, 0])
    blue.append([0, 0, 0, 0])
score = 0
for t, x, y in order:
    # x =
    if t == 1:
        for i in range(6):
            if green[i][y] !=0:
                green[i-1][y] = 1
                break
            if i == 5:
                green[5][y] = 1
        for i in range(6):
            if blue[i][x] !=0:
                blue[i-1][x] = 1
                break
            if i == 5:
                blue[5][x] = 1
    elif t == 2:
        for i in range(6):
            if green[i][y] or green[i][y+1] !=0:
                green[i-1][y], green[i-1][y+1] = 1, 1
                break
            if i == 5:
                green[5][y], green[5][y+1] = 1, 1
                #y값 고정
        for i in range(6):
            if blue[i][x] !=0:
                blue[i-1][x], blue[i-2][x] = 1, 1
                break
            if i == 5:
                blue[5][x], blue[4][x] = 1, 1
    else:
        for i in range(6):
            if green[i][y] !=0:
                green[i-1][y], green[i-2][y] = 1, 1
                break
            if i == 5:
                green[5][y], green[4][y] = 1, 1
        for i in range(6):
            if blue[i][x] or blue[i][x+1] !=0:
                blue[i-1][x], blue[i-1][x+1] = 1, 1
                break
            if i == 5:
                blue[5][x], blue[5][x+1] = 1, 1
    # 블록 내리기 끝
    for _ in range(6):
        g = green.popleft()
        if sum(g) != 4:
            green.append(g)
        else: score+=1
        b = blue.popleft()
        if sum(b) !=4:
            blue.append(b)
        else: score+=1
    for _ in range(6-len(green)):
        green.appendleft([0,0,0,0])
    for _ in range(6 - len(blue)):
        blue.appendleft([0, 0, 0, 0])

    if sum(blue[0])>0:
        blue.pop()
        blue.pop()
        blue.appendleft([0,0,0,0])
        blue.appendleft([0, 0, 0, 0])
    elif sum(blue[1])>0:
        blue.pop()
        blue.appendleft([0, 0, 0, 0])

    if sum(green[0])>0:
        green.pop()
        green.pop()
        green.appendleft([0,0,0,0])
        green.appendleft([0, 0, 0, 0])
    elif sum(green[1])>0:
        green.pop()
        green.appendleft([0, 0, 0, 0])
    # print("green")
    # print(*green,sep='\n')
    # print("blue")
    # print(*blue,sep='\n')
print(score)
print(sum([sum(g) for g in green])+ sum([sum(b) for b in blue]))