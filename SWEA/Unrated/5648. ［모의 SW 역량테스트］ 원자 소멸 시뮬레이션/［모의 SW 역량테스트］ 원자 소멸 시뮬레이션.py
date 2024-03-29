'''
n초 단위랑 n.5초 단위 위주로 검사
dict로 관리
엣지 찾고 나서 급하게 수정하느라 -> 왜 급했던거죠 시간은 충분했는데 ㅋㅋㅋ
찾고나서 수정을 잘못함 허허......
'''

def switch(d):
    if d == 0: return 1
    if d == 1: return 0
    if d == 2: return 3
    if d == 3: return 2


TC = int(input())
for tc in range(1, TC+1):
    dx = (0, 0, -1, 1)
    dy = (1, -1, 0, 0)
    N = int(input())
    input_quantum = [list(map(int, input().split())) for _ in range(N)]
    quantum_loc = dict()
    for i in range(N):
        x, y, d, e = input_quantum[i]
        quantum_loc[(x, y)] = (d, e)
    temp = set([])
    energy = 0
    for k, v in quantum_loc.items():
        x, y = k
        d, e = v
        X, Y = x+dx[d], y+dy[d]

        if (X,Y) in quantum_loc and quantum_loc[(X,Y)][0] == switch(d):
            temp.add((x,y))
            energy += quantum_loc[(x,y)][1]
    while temp:
        x, y = temp.pop()
        quantum_loc.pop((x,y))
    # 2020번을 하면 무조건 끝남
    for _ in range(2010):
        new_loc = dict()
        for k, v in quantum_loc.items():
            x, y = k
            d, e = v
            X, Y = x+dx[d], y+dy[d]
            # now_loc 갯수, d, e총합
            if (X,Y) in new_loc:
                new_loc[(X,Y)][0] += 1
                new_loc[(X, Y)][2] += e
            else:
                new_loc[(X,Y)] = [1,d,e]
        quantum_loc = dict()
        for k, v in new_loc.items():
            if v[0]>1:
                energy+=v[2]
                continue
                # 갯수가 여러개면 더해주고 넘어가기
            x, y = k
            _, d, e = v
            X, Y = x+dx[d], y+dy[d]
            d1 = switch(d)
            if (X,Y) in new_loc and new_loc[(X,Y)][0] == 1 and new_loc[(X,Y)][1] == d1:
                energy+=e
                continue
            quantum_loc[(x,y)] = (d,e)
        marker = False
        for k, v in quantum_loc.items():
            x, y = k
            d, e = v
            X, Y = x+dx[d], y+dy[d]
            for k1, v1 in quantum_loc.items():
                if k == k1: continue
                x1, y1 = k1
                d1, e1 = v
                X1, Y1 = x1+dx[d1], y1+dy[d1]
                if abs(x-x1)+abs(y-y1)>=abs(X1-X)+abs(Y1-Y):
                    marker=True
                    break
            if marker:break
        # print(quantum_loc)
        if not marker: break
    print(f'#{tc} {energy}')

