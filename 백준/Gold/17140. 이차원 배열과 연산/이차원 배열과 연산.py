'''
'''

def operation():
    new = []
    for i in range(lenR):
        numb = dict()
        for j in range(lenC):
            if matrix[i][j]==0:continue
            if matrix[i][j] in numb:
                numb[matrix[i][j]]+=1
            else:
                numb[matrix[i][j]] = 1
        lst = []
        for k, v in numb.items():
            # v갯수랑 k숫자
            lst.append((v,k))
        lst.sort()
        app = []
        for v, k in lst:
            app.append(k)
            app.append(v)
        new.append(app)
    mx = min(100, max([len(n) for n in new ]))
    for i in range(len(new)):
        if len(new[i]) < mx:
            for _ in range(mx-len(new[i])):
                new[i].append(0)
            else:
                new[i] = new[i][:mx]
    return new


R, C, K = map(int, input().split())
R, C = R-1, C-1
#matrix[R][C] == K 인 케이스까지 걸리는 시간
matrix = [list(map(int, input().split())) for _ in range(3)]
time = 0
for _ in range(102):
    if 0<=R<len(matrix) and 0<=C<len(matrix[0]) and matrix[R][C] == K:
        break
    time +=1
    lenR = len(matrix)
    lenC = len(matrix[0])
    if lenR>=lenC:
        matrix = operation()
        # print(*matrix,sep='\n')
        # print()
    else:
        matrix = list(map(list, zip(*matrix)))
        lenR, lenC = lenC, lenR
        matrix = operation()
        matrix = list(map(list, zip(*matrix)))

if time>100:
    print(-1)
else:
    print(time)