'''
1600*4*100(스티커 개수)*160
'''

def sticker(sx, sy, shape=[]):
    global matrix, st
    loc = set([])
    marker = True
    for i in range(R):
        for j in range(C):
            if shape[i][j]==0: continue

            if (sx+i,sy+j) in st:
                loc.add((sx+i,sy+j))
                continue
            else:
                marker=False
                break

        if not marker:
            break
    # print("loc", loc)
    if marker:
        while loc:
            value = loc.pop()
            st.remove(value)
            matrix[value[0]][value[1]] = 1
            # 스티커 붙이기
    # print(sx, sy, "sticker", marker)
    return marker

def move(R, C, shape=[]):
    marker = False
    for i in range(M-R+1):
        for j in range(N-C+1):
            marker = sticker(i, j, shape)
            if marker:
                break
        if marker:
            break
    return marker

def rotate(shape):
    copy_shape = [[0]*R for _ in range(C)]
    for i in range(C):
        for j in range(R):
            copy_shape[i][j] = shape[R-1-j][i]
    return copy_shape
M, N, K = map(int, input().split())
matrix = [[0]*N for _ in range(M)]
st = set([])
for i in range(M):
    for j in range(N):
        st.add((i,j))
# print(st)
# sticker 붙일 수 있는 위치 리스트
for i in range(K):
    R, C = map(int, input().split())
    shape = [list(map(int, input().split())) for _ in range(R)]
    # print(shape)
    for _ in range(4):
        # print(shape)
        dir = move(R,C,shape)
        if dir:
            break
        else:
            # print(i, "실행")
            shape = rotate(shape)
            R, C = len(shape), len(shape[0])
print(M*N-len(st))