'''
??? 이유를 알 수 없는 에러로 리트라이
'''

def move(n, rx, ry, bx, by, in_matrix):
    global mn, visit
    if n >=mn : return

    # print(*in_matrix, sep='\n')
    # 더 큰 케이스에는 해줄 필요가 없음
    for i in range(4):
        # 각 방향에 대해서 탐색을 진행 해주기
        # 단 bfs로 순서를 유지 해줘야함
        red = False
        blue = False
        # 어떤 색 공이 들어갔는지 체크해주기
        t_rx, t_ry, t_bx, t_by = rx, ry, bx, by
        temp_matrix = [x[:] for x in in_matrix[:]]
        # 원본 배열을 안건들기 위해서 복사
        for _ in range(2):
            # 어떤 공이 먼저 움직일 지 알 수 없으므로 두번 돌려주기
            while not red:
                # 빨간 공이 있는 경우 옴기기
                X = t_rx + dx[i]
                Y = t_ry + dy[i]
                if temp_matrix[X][Y] == '.':
                    # 옮길 칸이 .이면
                    temp_matrix[X][Y] = 'R'
                    #빨간 돌 옮겨가기
                    temp_matrix[t_rx][t_ry] = '.'
                    # 전 칸 초기화 하기
                    t_rx, t_ry =X, Y
                    # 좌표 옮기기
                elif temp_matrix[X][Y] == 'O':
                    # 만약 구멍이라면
                    temp_matrix[t_rx][t_ry]='.'
                    red = True
                    # 구멍에 들어 갔다고 체크해주기
                    break
                else:
                    # 앞에 빈칸이 아닌 무언가면 끊어주기
                    break
            while not blue:
                # print(X,Y)
                # 파란 공이 있는 경우 옴기기
                X = t_bx + dx[i]
                Y = t_by + dy[i]
                if temp_matrix[X][Y] == '.':
                    # 옮길 칸이 .이면
                    temp_matrix[X][Y] = 'B'
                    #빨간 돌 옮겨가기
                    temp_matrix[t_bx][t_by] = '.'
                    # 전 칸 초기화 하기
                    t_bx, t_by =X, Y
                    # 좌표 옮기기
                elif temp_matrix[X][Y] == 'O':
                    # 만약 구멍이라면
                    blue = True
                    # print("실행")
                    # 구멍에 들어 갔다고 체크해주기
                    break
                else:
                    # 앞에 빈칸이 아닌 무언가면 끊어주기
                    break
        # 옮기기 끝
        # 진행여부 체크하기
        if blue: continue
            #파란공이 들어간 경우 넘어가기
        if red:
            # 빨간공이 들어간경우
            mn = min(mn, n)
            # 최솟값 업데이트
        else: #안들어간 경우
            if not visit[t_rx][t_ry][t_bx][t_by]:
                # 옮겨간 자리에서 탐색한 적이 없는 경우
                visit[t_rx][t_ry][t_bx][t_by] = True
                move(n+1,t_rx,t_ry,t_bx,t_by,temp_matrix)
                visit[t_rx][t_ry][t_bx][t_by] = False
                # 다음 것 체크하러 갈 준비 시키기
            #이미 한데면 다시 탐색 안함


M, N = map(int, input().split())
matrix = [list(input()) for _ in range(M)]
visit = [[[[False]*N for _ in range(M)] for _ in range(N)] for _ in range(M)]
rx, ry = -1, -1
bx, by = -1, -1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(M):
    for j in range(N):
        if matrix[i][j] == 'B':
            bx, by = i, j
        if matrix[i][j] == 'R':
            rx, ry = i, j
mn = 11
visit[rx][ry][bx][by] = True
move(1, rx, ry, bx, by, matrix)
if mn>10:
    print(-1)
else:
    print(mn)
