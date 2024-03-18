'''
이해 끝 7분 -> 검은색에는 중력 작용 안함에 주의
반시계 방향으로 돌림에 주의
시간 1초 메모리 1024
검은색 -1 무지개 0 일반 M가지색 , 사방이 인접
블록집합 -> 일반블록 1개 이상 총 블록개수 2개 이상 검은색 포함 X 일반블록색 같아야함
기준 블록 -> 무지개 블록이 아닌 일반 블록 중에서 블록  행, 열이 제일 작은 것
주의 해야 할 점 -> 무지개 블록은 중복으로 포함 가능
1.크기가 가장 큰 블록 그룹을 찾는다. 그러한 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹, 그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것을, 그 것도 여러개이면 열이 가장 큰 것을 찾는다.
2.1에서 찾은 블록 그룹의 모든 블록을 제거한다. 블록 그룹에 포함된 블록의 수를 B라고 했을 때, B2점을 획득한다.
3.격자에 중력이 작용한다.
4.격자가 90도 반시계 방향으로 회전한다.
5.다시 격자에 중력이 작용한다.
구현시작하고 55분에 첫 제출
-> 틀렸습니다.
1시간 33분째에 두번째 틀림
'''
import copy
from collections import deque

def check(x,y):
    return 0<=x<N and 0<=y<N

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
score = 0
while True:
    # print(*matrix, sep='\n')
    # print()
    mx = 0
    mx_queue = deque()
    mx_rainbow = 0
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    # queue의 가장 앞에 들어가는게 기준 블럭
    visit = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 기준 블럭을 기준으로 탐색합시다
            count = 1
            # 자기 자신 넣었음
            rainbow = 0
            if not visit[i][j] and matrix[i][j]>=1:
                # print("실행")
                dq = deque()
                dq.append((i,j))
                visit[i][j]=True
                temp_deque = deque()
                temp_deque.append((i,j))
                while dq:
                    x, y = dq.popleft()
                    for k in range(4):
                        X = x+dx[k]
                        Y = y+dy[k]
                        if check(X,Y) and not visit[X][Y]:
                            if matrix[X][Y]==0:
                                # 무지개 블럭이면 무지개 체크, 개수체크, 방문체크, 더해주기
                                rainbow +=1
                                count +=1
                                visit[X][Y]=True
                                dq.append((X,Y))
                                temp_deque.append((X,Y))
                            elif matrix[X][Y] == matrix[i][j]:
                                count += 1
                                visit[X][Y] = True
                                temp_deque.append((X,Y))
                                dq.append((X, Y))
                            # 방문 안햇고
                # print(temp_deque)
                # BFS 탐색 끝났고
                if count<2 or mx>count :
                    while temp_deque:
                        x, y =temp_deque.pop()
                        if matrix[x][y] == 0:
                            visit[x][y] = False
                    continue

                # 블록갯수가 1개면 할 것이 없음
                # 블록 갯수가 최댓값이 아니어도 할 게 없음
                if mx<count:
                # 최댓값이 갱신되면 그냥 하면 됨
                    mx = count
                    #최댓값 갱신
                    mx_queue.clear()
                    # 최대블럭 갱신
                    mx_rainbow = rainbow
                    # 무지개 블럭값 갱신
                    while temp_deque:
                        x, y =temp_deque.pop()
                        mx_queue.append((x,y))
                        if matrix[x][y] == 0:
                            visit[x][y] = False
                            #무지개 블럭 재사용
                    continue
                # 중복되긴 하지만 디버깅을 위해서 적어주기
                if mx == count:
                    # 같은 경우에 무지개 블록의 개수 비고
                    if rainbow < mx_rainbow:
                        while temp_deque:
                            x, y = temp_deque.pop()
                            if matrix[x][y] == 0:
                                visit[x][y] = False
                        continue
                        # 무지개 블럭수가 더 적으면 지나가기
                    # 그 외의 케이스는 행이 크고 열이 큰 순이므로
                    # 무조건 갱신됨
                    mx = count
                    # 최댓값 갱신
                    mx_queue.clear()
                    # 최대블럭 갱신
                    mx_rainbow = rainbow
                    # 무지개 블럭값 갱신
                    while temp_deque:
                        x, y = temp_deque.pop()
                        mx_queue.append((x,y))
                        if matrix[x][y] == 0:
                            visit[x][y] = False
                            # 무지개 블럭 재사용
                    continue
    ################## 여기까지 1번 구현 완료################
    # print(mx_queue)
    if not mx_queue:
        # 더이상 진행할 수 없으면 끝내기
        break
    score += len(mx_queue)**2
    while mx_queue:
        x,y = mx_queue.pop()
        matrix[x][y]=-2
    # print(*matrix, sep='\n')
    # print()
    # 사용할 수 없는  값으로 바꿔주기
    # 중력 구현하기
    for t in range(2):
        for j in range(N):
            start = N-1
            for i in range(N-1, -1, -1):
                # print(i,start)
                if matrix[i][j]==-2:
                    continue
                    # 빈자리라 체크해주기
                if matrix[i][j]>=0:
                    # 블럭이 있으면
                    # print(*matrix,sep='\n')
                    matrix[start][j]=matrix[i][j]
                    if start!=i:
                        matrix[i][j] = -2
                    start-=1
                if matrix[i][j]==-1:
                    #검정 블럭이면
                    start = i-1
                    # 중력 작용 안함 -> 그 위에 떨어지도록 설계
        # print(*matrix, sep='\n')
        # print("실행")
        if t == 1:break
        for _ in range(3):
            matrix = list(map(list, zip(*matrix[::-1])))
    # print(*matrix, sep='\n')
    # print()
print(score)




