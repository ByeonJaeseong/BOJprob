'''
읽기 시작 3시 7분

정리하면서 읽자
1. 물고기의 수가 가장 적은 어항에 한마리 넣기
 -> 여러개면 모두 한 마리씩 넣기
2. 어항 쌓기 가장 왼쪽에 있는 어항을 그 어항의 오른쪽 어항에 올려놓기
3. 두개 이상 쌓여 있는 어항 공중 부양 후 90도 회전후 왼쪽 끝에 내려 놓기
   -> 계속 반복 어항 아래가 비기 전까지
4. 물고기 조절 -> 모든 인접한 두 어항에 대해서 물고기 수 차이를 구함 -> 그리고 5로 나눈 몫이 0보다크면 나눠 주기
5. 끝나면 바닥에 다시 놓기 왼쪽 밑행부터 올라가서 다 놓고 오른쪽행
6. 다시 공중 부양 왼쪽 꺼 뒤집엇 위로 오른쪽거는 그대로 -> 2번 반복
7 -> 물고기 조절 어게인
8- > 순서대로 바닥에 놓기
''잠시 휴식 3시 10분 ~ 14분''
문제 이해 및 정리 10분
빡구현이네 엉엉
'''

N, K =map(int,input().split())
# 어항 갯수, 차이 최솟값
lst = list(map(int, input().split()))
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
count = 0
while True:
    count+=1
    # 1. 물고기의 수가 가장 적은 어항에 한마리 넣기
    #  -> 여러개면 모두 한 마리씩 넣기
    mn = min(lst)
    for i in range(N):
        if lst[i] == mn: lst[i]+=1
    # 2. 어항 쌓기 가장 왼쪽에 있는 어항을 그 어항의 오른쪽 어항에 올려놓기
    temp_lst = []
    temp_lst.append([lst[0]])
    temp_lst.append(lst[1:])
    while True:
        t_lst = []
        for j in range(len(temp_lst[-1])):
            # 맨 밑의 갯수 만큼 반복하겠죠?
            ap_lst = []
            # 더해줄 것
            if len(temp_lst[0])<=j: break
            # 여러개 있는게 끝났으면
            for i in range(len(temp_lst)):
                ap_lst.append(temp_lst[i][j])
            ap_lst.reverse()
            t_lst.append(ap_lst)
        t_lst.append(temp_lst[-1][j:])

        # print(t_lst)
        if len(t_lst[-1])>=len(t_lst[0]):
            temp_lst=t_lst
        else:
            break
    # print(temp_lst)
    #########여기까지 구현 완료 ############
    ########## 물고기 조절 들어 갑시다
    sm_lst = [[0]*len(t) for t in temp_lst]
    # print(sm_lst)
    for i in range(len(temp_lst)):
        for j in range(len(temp_lst[i])):
            M1, N1 = len(temp_lst), len(temp_lst[i])
            for k in range(4):
                X = i + dx[k]
                Y = j + dy[k]
                # print(X,Y,M1,N1,i)
                if 0<=X<M1 and 0<=Y<N1 and 0<=Y<len(temp_lst[X]) and ((temp_lst[i][j]-temp_lst[X][Y])//5) >0:
                    v = (temp_lst[i][j]-temp_lst[X][Y])//5
                    sm_lst[i][j]-=v
                    sm_lst[X][Y]+=v
    for i in range(len(temp_lst)):
        for j in range(len(temp_lst[i])):
            temp_lst[i][j] += sm_lst[i][j]
    lst.clear()
    for j in range(len(temp_lst[-1])):
        for i in range(1,len(temp_lst)+1):
            if j >= len(temp_lst[-i]):continue
            lst.append(temp_lst[-i][j])
    # print(lst)
    lst = [lst]
    for _ in range(2):
        temp_lst = []
        for i in range(1, len(lst)+1):
            tm = len(lst[-i])
            ap = lst[-i][:tm//2]
            # print(ap)
            ap.reverse()
            temp_lst.append(ap)
        for i in range(len(lst)):
            tm = len(lst[-i])
            ap = lst[i][tm // 2:]
            temp_lst.append(ap)
        # print(temp_lst)
        lst = temp_lst


    temp_lst = [l[:] for l in lst]
    sm_lst = [[0]*len(t) for t in temp_lst]
    # print(sm_lst)
    for i in range(len(temp_lst)):
        for j in range(len(temp_lst[i])):
            M1, N1 = len(temp_lst), len(temp_lst[i])
            for k in range(4):
                X = i + dx[k]
                Y = j + dy[k]
                # print(X,Y,M1,N1,i)
                if 0<=X<M1 and 0<=Y<N1 and 0<=Y<len(temp_lst[X]) and ((temp_lst[i][j]-temp_lst[X][Y])//5) >0:
                    v = (temp_lst[i][j]-temp_lst[X][Y])//5
                    sm_lst[i][j]-=v
                    sm_lst[X][Y]+=v
    for i in range(len(temp_lst)):
        for j in range(len(temp_lst[i])):
            temp_lst[i][j] += sm_lst[i][j]
    # print(lst)

    lst.clear()
    for j in range(len(temp_lst[-1])):
        for i in range(1,len(temp_lst)+1):
            if j >= len(temp_lst[-i]):continue
            lst.append(temp_lst[-i][j])
    # print(lst)
    if (max(lst)-min(lst))<=K:
        break
print(count)