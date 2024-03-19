'''
상어가 또나왔습니다
ㅋㅋㅋㅋㅋㅋㅋ
문제 읽기 시작 2시 40분
1의번호를 가진 어른상어 -> 모두 내쫓음
단, 1,000초가 넘어도 다른 상어가 격자에 남아 있으면 -1을 출력한다.
문제이해를 완벽히 하진 않았지만 컨셉은 알겠다 -> 45분
일단 느낌은 골드 1일듯?
2시 51분 리프레쉬 함
3시 27분 디버깅 시작 리프레시
'''

def check(x,y):
    return 0<=x<N and 0<=y<N

def shark_move():
    global smell
    lst = []
    for k in loc.keys():
        # 상어 꺼냄
        d, x, y = loc[k]
        marker = True
        for i in priority[k][d]:
            X = x+dx[i]
            Y = y+dy[i]
            if not check(X,Y):
                continue
            if not smell[X][Y]:
                # 아직 냄새를 안 퍼트린 데면
                lst.append((k,X,Y,i))
                # 상어 종류와 좌표로 관리
                marker = False
                break
        if not marker: continue
        # 상어가 냄새를 퍼뜨렸으면 넘어가기
        for i in priority[k][d]:
            X = x+dx[i]
            Y = y+dy[i]
            if not check(X,Y):continue
            if smell[X][Y][0][0] == k:
                # 자기가 냄새를 뿌린 곳이면
                smell[X][Y][0][1] = K+1
                matrix[x][y] = 0
                matrix[X][Y] = k
                loc[k] = (i,X,Y)
                # 한번씩 빼줄꺼기 때문에 미리 추가해놓기
                break
    # 상어 움직이기전에 냄새 1씩 줄여주기
    for i in range(N):
        for j in range(N):
            if not smell[i][j] : continue
            if smell[i][j][0][1] == 1:
                smell[i][j].pop()
            elif smell[i][j][0][1] == 0:
                continue
            else:
                smell[i][j][0][1] -=1
    # 냄새 한칸씩 줄여주기

    if lst:
        lst.sort()
        # print(lst)
        # 상어 번호, 위치
        for l in lst:
            s, x, y, d = l
            if not smell[x][y]:
                # print("시일행")
                smell[x][y].append([s,K])
                direction, p, q = loc[s]
                matrix[p][q] = 0
                matrix[x][y] = s
                loc[s] = (d, x, y)
            # 냄새가 비어 있으면
            else:
                # print("실행")
                # 이미 낮은 번호의 상어가 차지한 경우
                direction, p, q = loc[s]
                matrix[p][q] = 0
                # 보드에서 상어 지우기
                loc.pop(s)

                # 상어 후보에서 지우기
    # for t in range(N):
        # print(smell[t])
    # print()
    # print(*matrix, sep='\n')
    # print(loc)
    # print()



N, M, K = map(int,input().split())
# N 배열크기, M 상어 갯수, K 영역 지속 시간
matrix = [list(map(int, input().split())) for _ in range(N)]
smell = [[[] for _ in range(N)] for _ in range(N)]
priority = []
priority.append([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
dir = [0]+list(map(int, input().split()))
# print(dir)
loc = dict()
for i in range(N):
    for j in range(N):
        if matrix[i][j]!=0:
            loc[matrix[i][j]] = (dir[matrix[i][j]], i, j)
#상어의 방향
dx = (0, -1, 1, 0, 0)
dy = (0, 0, 0, -1, 1)

for _ in range(M):
    order = [[0,0,0,0]]+[list(map(int, input().split())) for _ in range(4)]
    priority.append(order)
    # 위, 아래 왼쪽, 오른쪽
    # 제로 패딩 했음에 유의
# print(priority)
for k, v in loc.items():
    smell[v[1]][v[2]].append([k,K])
    # 현재 자리에 뿌려주기
count =0
# print(smell)
for _ in range(1000):
    count+=1
    shark_move()
    if len(loc)==1:
        break

if len(loc) == 1:
    print(count)
else:
    print(-1)