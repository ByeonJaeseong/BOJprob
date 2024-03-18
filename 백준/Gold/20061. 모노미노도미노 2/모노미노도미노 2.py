'''
출력 :
점수
들어있는 블럭의 갯수

진정한 빡구현의 시험대가 될 느낌?

조심해야될 점 -> 사라지는 건 한칸만 내려감
0, 1일 때에는 -> 전부 내려감
입력값 t, x, y
t 1 -> 1*1
2 -> 1*2 열로 2칸 (x,y), (x,y+1)
3 -> 2*1 행으로 두칸 (x,y) (x+1,y)

갑분 추가시간 없음이므로 dq을 써서 관리하기로 함
왜냐 -> 특별 구간을 관리할 필요가 있음
'''
from collections import deque

def blue_move(t,x,y):
    global score, blue
    # print("실행")
    landing = -1
    if t == 1:
        for i in range(6):
            if blue[i][x]:
                blue[i-1][x]=True
                landing = i-1
                break
            if i ==5:
                blue[i][x]=True
                landing = i
    elif t==2:
        for i in range(6):
            if blue[i][x]:
                blue[i-1][x]=True
                blue[i-2][x]=True
                landing = i - 1
                # print("실행")
                break
            if i ==5:
                blue[i][x]=True
                blue[i-1][x] = True
                # print("시이일행")
                landing = i
    else:
        for i in range(6):
            if blue[i][x] or blue[i][x+1]:
                blue[i-1][x]=True
                blue[i-1][x+1]=True
                landing = i - 1
                break
            if i ==5:
                blue[i][x]=True
                blue[i][x+1] = True
                landing = i

   #####점수
    if t in [1,3]:
        marker = True
        for i in range(4):
            if not blue[landing][i]:
                marker = False
                break
        if marker:
            # print("점수더하기")
            score+=1
            temp_dq = deque()
            for i in range(landing):
                temp_dq.append(blue.popleft())
            blue.popleft()
            while temp_dq:
                blue.appendleft(temp_dq.pop())
            blue.appendleft([False]*4)
    # 파란색에서 한줄 줄이는 것 까지 함

    else:
        marker1 = True
        marker2 = True
        for i in range(4):
            if not blue[landing][i]:
                marker1 = False
                break
        for i in range(4):
            if not blue[landing-1][i]:
                marker2 = False
                break
        if marker1 and marker2:
            score += 2
            temp_dq = deque()
            for i in range(landing-1):
                temp_dq.append(blue.popleft())
            blue.popleft()
            blue.popleft()
            while temp_dq:
                blue.appendleft(temp_dq.pop())
            blue.appendleft([False]*4)
            blue.appendleft([False] * 4)
        elif marker1 and not marker2:
            score += 1
            temp_dq = deque()
            for i in range(landing):
                temp_dq.append(blue.popleft())
            blue.popleft()
            while temp_dq:
                blue.appendleft(temp_dq.pop())
            blue.appendleft([False]*4)
        elif not marker1 and marker2:
            score += 1
            temp_dq = deque()
            for i in range(landing - 1):
                temp_dq.append(blue.popleft())
            blue.popleft()
            while temp_dq:
                blue.appendleft(temp_dq.pop())
            blue.appendleft([False] * 4)


def green_move(t,x,y):
    global score, green
    landing = -1
    if t == 1:
        for i in range(6):
            if green[i][y]:
                green[i-1][y]=True
                landing = i-1
                break
            if i==5:
                green[i][y]=True
                landing = i
    elif t==3:
        for i in range(6):
            if green[i][y]:
                green[i-1][y]=True
                green[i-2][y]=True
                landing = i - 1
                break
            if i==5:
                green[i][y]=True
                green[i-1][y] = True
                landing = i
    else:
        for i in range(6):
            if green[i][y] or green[i][y+1]:
                green[i-1][y]=True
                green[i-1][y+1]=True
                landing = i - 1
                break
            if i ==5:
                green[i][y]=True
                green[i][y+1]=True
                landing = i
    if t in [1,2]:
        marker = True
        for i in range(4):
            if not green[landing][i]:
                marker = False
                break
        if marker:
            score+=1
            temp_dq = deque()
            for i in range(landing):
                temp_dq.append(green.popleft())
            green.popleft()
            while temp_dq:
                green.appendleft(temp_dq.pop())
            green.appendleft([False]*4)
    #초록색에서 한줄 줄이는 것 까지 함

    else:
        marker1 = True
        marker2 = True
        for i in range(4):
            if not green[landing][i]:
                marker1 = False
                break
        # print(green[landing-1])
        for i in range(4):
            if not green[landing-1][i]:
                marker2 = False
                break
        if marker1 and marker2:
            score += 2
            temp_dq = deque()
            for i in range(landing-1):
                temp_dq.append(green.popleft())
            green.popleft()
            green.popleft()
            while temp_dq:
                green.appendleft(temp_dq.pop())
            green.appendleft([False]*4)
            green.appendleft([False] * 4)
        elif marker1 and not marker2:
            # print("실행2")
            score += 1
            temp_dq = deque()
            for i in range(landing):
                temp_dq.append(green.popleft())
            green.popleft()
            while temp_dq:
                green.appendleft(temp_dq.pop())
            green.appendleft([False]*4)
        elif not marker1 and marker2:
            # print("실행1", landing)
            score += 1
            temp_dq = deque()
            for i in range(landing - 1):
                temp_dq.append(green.popleft())
            green.popleft()
            while temp_dq:
                green.appendleft(temp_dq.pop())
            green.appendleft([False] * 4)


blue = deque()
green = deque()

for _ in range(6):
    blue.append([False] * 4)
    green.append([False]*4)
N = int(input())
order = [list(map(int, input().split())) for _ in range(N)]
# 명령 횟수
score = 0
for i in range(N):
    t, x, y = order[i]
    blue_move(t,x,y)
    green_move(t,x,y)
    if blue[0][0] or blue[0][1] or blue[0][2] or blue[0][3]:
        blue.pop()
        blue.pop()
        blue.appendleft([False]*4)
        blue.appendleft([False] * 4)
        # print("1")
    elif blue[1][0] or blue[1][1] or blue[1][2] or blue[1][3]:
        blue.pop()
        blue.appendleft([False] * 4)
        # print('2')
    if green[0][0] or green[0][1] or green[0][2] or green[0][3]:
        green.pop()
        green.pop()
        green.appendleft([False]*4)
        green.appendleft([False] * 4)
        # print(3)
    elif green[1][0] or green[1][1] or green[1][2] or green[1][3]:
        green.pop()
        green.appendleft([False] * 4)
    #     print(4)
    # print("blue")
    # print(*blue, sep='\n')
    # print("green")
    # print(*green, sep='\n')
print(score)
block = 0
for i in range(6):
    for j in range(4):
        if blue[i][j]:
            block+=1
        if green[i][j]:
            block += 1
print(block)