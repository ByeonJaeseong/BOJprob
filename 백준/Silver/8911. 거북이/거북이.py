'''
움직인 곳 전부 마킹하고
가로 최대 세로 최대 해서 곱하면 됨
'''
TC = int(input())
for tc in range(TC):
    D = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    # L -> D -=1 R +=1
    sx, sy = 0, 0
    action = list(input())
    minx, maxx, miny, maxy = 0, 0, 0, 0
    for i in range(len(action)):
        if action[i] == 'F':
            sx, sy = sx + dx[D], sy + dy[D]
            minx = min(sx, minx)
            maxx = max(sx, maxx)
            miny = min(sy, miny)
            maxy = max(sy, maxy)

        elif action[i] == 'B':
            sx, sy = sx-dx[D], sy-dy[D]
            minx = min(sx, minx)
            maxx = max(sx, maxx)
            miny = min(sy, miny)
            maxy = max(sy, maxy)

        elif action[i] == 'L':
            D = (D-1)%4
        else :
            D = (D+1)%4

    print((maxx-minx)*(maxy-miny))
