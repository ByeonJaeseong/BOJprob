'''
문제 이해 하는데 4분
실은 구상이랄 것보단 빡구현에 가깝고 2*2*2 큐브에서 했던 로직이긴 함
동시에 주사위 굴리기와 같은 로직이라고 생각 해야 할 듯 함

34분쯤 종이접기 시작
59분 첫 제출 틀렸습니다. -> 25%
1시간 39분쯤 2번째 제출함 -> 25% 의미 없지만 함수를 리턴형식으로 바꿔봄
'''

def rotation(S, d):
    global FS, US, DS, BS, RS, LS
    if S == 'F':
        if d == '+':
            FS = list(map(list, zip(*FS[::-1])))
            US[2][0], US[2][1], US[2][2], RS[0][0], RS[1][0], RS[2][0], DS[0][2], DS[0][1], DS[0][0], LS[2][2], LS[1][2], LS[0][2] = \
                LS[2][2], LS[1][2], LS[0][2], US[2][0], US[2][1], US[2][2], RS[0][0], RS[1][0], RS[2][0], DS[0][2], DS[0][1], DS[0][0]
            return
        else:
            FS = list(map(list, zip(*FS)))[::-1]
            US[2][0], US[2][1], US[2][2], RS[0][0], RS[1][0], RS[2][0], DS[0][2], DS[0][1], DS[0][0], LS[2][2], LS[1][2], LS[0][2] = \
                RS[0][0], RS[1][0], RS[2][0], DS[0][2], DS[0][1], DS[0][0], LS[2][2], LS[1][2], LS[0][2], US[2][0], US[2][1], US[2][2]
            return

    if S == 'B':
        if d == '+':
            BS = list(map(list, zip(*BS[::-1])))
            DS[2][0], DS[2][1], DS[2][2], RS[2][2], RS[1][2], RS[0][2], US[0][2], US[0][1], US[0][0], LS[0][0], LS[1][0], LS[2][0] = \
                LS[0][0], LS[1][0], LS[2][0], DS[2][0], DS[2][1], DS[2][2], RS[2][2], RS[1][2], RS[0][2], US[0][2], US[0][1], US[0][0]
            return
        else:
            BS = list(map(list, zip(*BS)))[::-1]
            DS[2][0], DS[2][1], DS[2][2], RS[2][2], RS[1][2], RS[0][2], US[0][2], US[0][1], US[0][0], LS[0][0], LS[1][0], LS[2][0] = \
                RS[2][2], RS[1][2], RS[0][2], US[0][2], US[0][1], US[0][0], LS[0][0], LS[1][0], LS[2][0], DS[2][0], DS[2][1], DS[2][2]
            return

    if S == 'R':
        if d == '+':
            RS = list(map(list, zip(*RS[::-1])))
            US[2][2], US[1][2], US[0][2], BS[2][2], BS[1][2], BS[0][2], DS[2][2], DS[1][2], DS[0][2], FS[2][2], FS[1][2], FS[0][2] = \
                FS[2][2], FS[1][2], FS[0][2], US[2][2], US[1][2], US[0][2], BS[2][2], BS[1][2], BS[0][2], DS[2][2], DS[1][2], DS[0][2]
            return
        else:
            RS = list(map(list, zip(*RS)))[::-1]
            US[2][2], US[1][2], US[0][2], BS[2][2], BS[1][2], BS[0][2], DS[2][2], DS[1][2], DS[0][2], FS[2][2], FS[1][2], FS[0][2] = \
                BS[2][2], BS[1][2], BS[0][2], DS[2][2], DS[1][2], DS[0][2], FS[2][2], FS[1][2], FS[0][2], US[2][2], US[1][2], US[0][2]
            return

    if S == 'L':
        if d == '+':
            LS = list(map(list, zip(*LS[::-1])))
            US[0][0], US[1][0], US[2][0], FS[0][0], FS[1][0], FS[2][0], DS[0][0], DS[1][0], DS[2][0], BS[0][0], BS[1][0], BS[2][0] = \
                BS[0][0], BS[1][0], BS[2][0], US[0][0], US[1][0], US[2][0], FS[0][0], FS[1][0], FS[2][0], DS[0][0], DS[1][0], DS[2][0]
            return
        else:
            LS = list(map(list, zip(*LS)))[::-1]
            US[0][0], US[1][0], US[2][0], FS[0][0], FS[1][0], FS[2][0], DS[0][0], DS[1][0], DS[2][0], BS[0][0], BS[1][0], BS[2][0] = \
                FS[0][0], FS[1][0], FS[2][0], DS[0][0], DS[1][0], DS[2][0], BS[0][0], BS[1][0], BS[2][0], US[0][0], US[1][0], US[2][0]
            return

    if S == 'U':
        if d == '+':
            US = list(map(list, zip(*US[::-1])))
            BS[2][0], BS[2][1], BS[2][2], RS[0][2], RS[0][1], RS[0][0], FS[0][2], FS[0][1], FS[0][0], LS[0][2], LS[0][1], LS[0][0] = \
                LS[0][2], LS[0][1], LS[0][0], BS[2][0], BS[2][1], BS[2][2], RS[0][2], RS[0][1], RS[0][0], FS[0][2], FS[0][1], FS[0][0]
            return
        else:
            US = list(map(list, zip(*US)))[::-1]
            BS[2][0], BS[2][1], BS[2][2], RS[0][2], RS[0][1], RS[0][0], FS[0][2], FS[0][1], FS[0][0], LS[0][2], LS[0][1], LS[0][0] = \
                RS[0][2], RS[0][1], RS[0][0], FS[0][2], FS[0][1], FS[0][0], LS[0][2], LS[0][1], LS[0][0], BS[2][0], BS[2][1], BS[2][2]
            return

    if S == 'D':
        if d == '+':
            DS = list(map(list, zip(*DS[::-1])))
            FS[2][0], FS[2][1], FS[2][2], RS[2][0], RS[2][1], RS[2][2], BS[0][2], BS[0][1], BS[0][0], LS[2][0], LS[2][1], LS[2][2] = \
                LS[2][0], LS[2][1], LS[2][2], FS[2][0], FS[2][1], FS[2][2], RS[2][0], RS[2][1], RS[2][2], BS[0][2], BS[0][1], BS[0][0]
            return
        else:
            DS = list(map(list, zip(*DS)))[::-1]
            FS[2][0], FS[2][1], FS[2][2], RS[2][0], RS[2][1], RS[2][2], BS[0][2], BS[0][1], BS[0][0], LS[2][0], LS[2][1], LS[2][2] = \
                RS[2][0], RS[2][1], RS[2][2], BS[0][2], BS[0][1], BS[0][0], LS[2][0], LS[2][1], LS[2][2], FS[2][0], FS[2][1], FS[2][2]
            return

TC = int(input())
for _ in range(TC):
    N = int(input())
    # 실행 횟수
    order = list(input().split())
    US = [['w', 'w', 'w'] for _ in range(3)]
    DS = [['y', 'y', 'y'] for _ in range(3)]
    FS = [['r', 'r', 'r'] for _ in range(3)]
    BS = [['o', 'o', 'o'] for _ in range(3)]
    LS = [['g', 'g', 'g'] for _ in range(3)]
    RS = [['b', 'b', 'b'] for _ in range(3)]
    for i in order:
        rotation(i[0],i[1])
    print(*US[0], sep="")
    print(*US[1], sep="")
    print(*US[2], sep="")
