'''
조심해서 구현 합시다
문제 구상 및 이해 8분
stack을 잘 쓰면 의외로 쉽게 잘 접근할 수 있는 문제
dict -> 구슬 위치 번호에 다른 i, j값 저장해놓고
해결하기
번호 자체가 중요한건 아니니 list관리하기 편하게 0부터 저장하기

53분 -> 시간초과 -> 솔직히 방만하게 짠건 맞음
'''

from collections import deque

N, K = map(int, input().split())
# 배열 사이즈, 블리자드 횟수
matrix = [list(map(int, input().split())) for _ in range(N)]
order = [list(map(int, input().split())) for _ in range(K)]
bead_dic = dict()

sx, sy = N//2, N//2
upper, lower = N//2+1, N//2-1
dx = (0, 1, 0, -1)
dy = (-1, 0, 1, 0)
d = 0
count = -1
odd = 3
while True:
    if count== N**2-2: break
    if count == odd**2-2:
        odd +=2
        upper+=1
        lower-=1

    count +=1
    X, Y = sx+dx[d], sy+dy[d]
    if lower<=X<=upper and lower<=Y<=upper:
        bead_dic[count] = (X,Y)
        sx, sy = X, Y
    else:
        d = (d+1)%4
        X, Y = sx+dx[d], sy+dy[d]
        bead_dic[count] = (X,Y)
        sx, sy = X, Y
################ 배열 관리 성공 #########################
###################################################################################################################################3
loc_dic = {v:k for k, v in bead_dic.items()}
# print(loc_dic)
score = 0
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
bead = deque()
for i in range(N**2-1):
    x, y = bead_dic[i]
    if matrix[x][y] == 0 :continue
    bead.append(matrix[x][y])
# print(bead_dic)
#초기 구술값 셋팅

for k in range(K):
    d, S= order[k]
    d -= 1
    dest = set([])
    X, Y = N//2, N//2
    for s in range(S):
        X +=dx[d]
        Y +=dy[d]
        dest.add(loc_dic[(X,Y)])
        # 몇번째 위치의 구술인지 더해줌
    ########### 파괴될 구슬 위치 찾기 ##############

    len_b = len(bead)
    for i in range(len_b):
        v = bead.popleft()
        if i in dest:continue
        # 파괴 될 위치에 있으면 구슬 건너 뛰기
        bead.append(v)
    # 한칸씩 당기기
    # print(bead)
    ############## 당기기 끝 ############

    #########3 여기서부턴 폭발 ###########
    while True:
        init_length = len(bead)
        count = 1
        if not bead : break
        v = bead.popleft()
        bead.append(v)
        len_b = len(bead)
        for lb in range(1,len_b):
            v = bead.popleft()
            if v == bead[-1]:
                count+=1
                bead.append(v)
                if lb == len_b-1 and count>=4:
                    score += count * bead[-1]
                    for _ in range(count):
                        bead.pop()
            else:
                if count>=4:
                    score += count*bead[-1]
                    for _ in range(count):
                        bead.pop()
                    count = 1
                    bead.append(v)
                else:
                    count = 1
                    bead.append(v)
        if init_length == len(bead) or not bead:
            break
        # if not bead:break
        # 반복했으면 끝
    # print(bead)
    ############## 폭발 끝 #############
    # 여기서부터 복사
    len_bead = len(bead)
    now = 0
    count = 0
    size = 0
    for lb in range(len_bead):
        v = bead.popleft()
        if size >= N**2-2: continue
        if now == 0:
            now = v
            count = 1
            continue
        if now == v:
            count+=1
        else:
            bead.append(count)
            bead.append(now)
            size+=2
            now = v
            count = 1
    if len_bead>0 and size<N**2-2:
        bead.append(count)
        bead.append(now)
    # print(bead)

print(score)







