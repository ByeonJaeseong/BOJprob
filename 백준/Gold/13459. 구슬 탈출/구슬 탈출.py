'''
구상 7분
빨강 공만 홀에 넣기가 목표
R,B의 종착점 위치를 여러번 넣어가면서 탐색하고
R이 이미 방문한 종착점에 온다하면 return

디버깅이 안되서 1시간 남겨놓고 코드 뒤집어 엎음
근데 맞춘 코드는 전 코드인 어이없는 이유

디버깅이 안되길래 로직적으로 뭐가 틀린거지를 참 고민을 많이하다가 코드를 뒤집어 엎었다.
내가 눈에 안보이더라도 로직적인 오류가 있을 수 있을테니 그냥 코드를 뒤집어 엎고 전 코드 로직과 동일한 코드를 다시 만들었다.
실은 코드를 작성하면서 빼먹은게 많았는데, 빨간돌을 움직이고 나서 자리를 안비켜줘서 파란돌이 못왔다던가
기타 등등의 이유는 많았지만 결정적인 로직의 문제는 백트리캥을 하면서 돌릴때 초기화를 안시켜 준 것이 문제였다.
이게 참 당황스러운데 지금까지 이런식의 실수가 단 한번도 없다보니 당연히 백트래킹 파트는 의심을 안했다.
그러다보니 계속해서 디버깅이 안되고 어디가 틀린거지 싶은 생각이 많이 들었다.
솔직히 이와 유사한 문제들이 많기때문에 처음에 이 문제를 보고 쉽게 풀 수 있을 것이라고 생각했는데, 그렇지 못한게 좀 아쉽다.
실수리스트가 적층이 되가는게 시험장에서 실수를 안할 가능성이 높아져서 좋아해야할지 아니면 오늘 실수를 했다는 것에 대해서
아쉬워 해야 할지는 약간 애매한 감이 있다.

늘 그랬듯이 코드를 짜다가 싸이클이 다가오면 갈아 엎는 편이다. 요즘은 좀 빈도수가 많아져서 문제인데, 빈도수는 줄여나가는 쪽으로 연습할것이다.
코드를 갈아엎고 같은 로직을 짜더라도 의미는 있는 것 같다. 단 단순 로직 반복이라서 사실상 리팩토링 하듯이 코드에 주석을 하나씩 달았다.
그러다 보니 눈에 안보이던 부분이 잡히고 디버깅에 성공할 수 있는 길이 생겼던 것 같다.
참 요즘 싸이클을 타면서 문제가 풀리는게 웃기지만 웃기지만은 않다.

어찌됐든 시간내에 디버깅한 것은 만족스럽지만 너무 고생스럽게 푼 점은 반성해야할 점이다.
이번에 이런 실수를 해봤으니 다음에는 조금더 조심하게 되지 않을까 싶다. 애초에 구현하고 첫 제출은 50분 밖에 안걸렸다.
디버깅 및 코드 재작성 시간이 1시간이 걸린 것이지.

비슷한 실수는 반복하지 않는 것이 좋다. 실수를 안하는게 불가능 하다라는 것을 인지하고 있어서
최대한 많은 실수를 인지하고 있는 것이 좋을 것 같다.

다량의 실수로 실력이 감퇴되기전에 다수의 실수로 실력을 높이는 과정으로 가야겠다

+ 문제는 비슷한 문제가 골3였으나 그보단 살짝 어려워서 골 2~골1수준의 문제라고 생각은 했다.
++ 문제 자체는 아이디어만 얻으면 구현하기가 어렵지는 않은 문제이나 처음 접할때는 당황스러운 문제이다.

리뷰끝
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
    print(0)
else:
    print(1)
