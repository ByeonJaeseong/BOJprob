'''
3시 33분 시작
'''
N, K = map(int, input().split())
lst = list(map(int, input().split()))
# print(lst)
time = 0
while True:
    time+=1
    mn = 10_000_000
    for i in range(N):
        mn = min(mn, lst[i])
    for i in range(N):
        if lst[i] == mn : lst[i]+=1
    # print(lst)
    ### 여긴 구현 완료
    lst = [[lst[0]],lst[1:]]
    # print(*lst, sep='\n')
    while True:
        new_lst = []
        # print(lst[-1])
        marker = True
        for j in range(len(lst[-1])):
            temp = []
            for i in range(len(lst)):
                if j<len(lst[i]):
                    temp.append(lst[i][j])
                else:
                    temp.clear()
                    marker= False
                    break
            if not marker:
                temp = lst[-1][j:]
                # print(temp)
                new_lst.append(temp)
                break
            temp.reverse()
            new_lst.append(temp)
        if len(new_lst[-1])<len(new_lst[0]):break
        # print(*new_lst, sep='\n')
        # print("실행됨")
        if len(new_lst[-1]) == len(new_lst[0]):
            lst = new_lst
            break
        lst = new_lst
    # print("공중부양")
    # print(*lst, sep='\n')
    # 여기서 물고기 조절작업 해야함
    new_lst = [[0]*len(l) for l in lst]
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if j+1<len(lst[i]):
                if lst[i][j]>lst[i][j+1]:
                    value = (lst[i][j]-lst[i][j+1])//5
                    new_lst[i][j] -=value
                    new_lst[i][j+1] +=value
                else:
                    value = (-lst[i][j] + lst[i][j + 1]) // 5
                    new_lst[i][j] += value
                    new_lst[i][j + 1] -= value
            if i+1<len(lst):
                if lst[i+1][j]>lst[i][j]:
                    value = (lst[i+1][j]-lst[i][j])//5
                    new_lst[i+1][j] -=value
                    new_lst[i][j] +=value
                else:
                    value = (-lst[i+1][j] + lst[i][j]) // 5
                    new_lst[i+1][j] += value
                    new_lst[i][j] -= value
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            lst[i][j] += new_lst[i][j]
    # print("물고기 조절")
    # print(*lst, sep='\n')

    new_lst = []
    for j in range(len(lst[-1])):
        for i in range(1, len(lst)+1):
            if j >=len(lst[-i]):break
            new_lst.append(lst[-i][j])
    lst = [new_lst]
    # print("평탄화")
    # print(lst)
    # 평탄화 끝남

    for _ in range(2):
        new_lst = []
        for i in range(len(lst)):
            temp = lst[i][:len(lst[0])//2][:]
            temp.reverse()
            new_lst.append(temp)
        new_lst.reverse()
        for i in range(len(lst)):
            new_lst.append(lst[i][len(lst[0])//2:])
        lst = new_lst
        # print("인쇄")
        # print(*lst,sep='\n')
    # print("공중부양2")
    # print(*lst, sep='\n')
    # print()
    new_lst = [[0]*len(l) for l in lst]
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if j+1<len(lst[i]):
                if lst[i][j]>lst[i][j+1]:
                    value = (lst[i][j]-lst[i][j+1])//5
                    new_lst[i][j] -=value
                    new_lst[i][j+1] +=value
                else:
                    value = (-lst[i][j] + lst[i][j + 1]) // 5
                    new_lst[i][j] += value
                    new_lst[i][j + 1] -= value
            if i+1<len(lst):
                if lst[i+1][j]>lst[i][j]:
                    value = (lst[i+1][j]-lst[i][j])//5
                    new_lst[i+1][j] -=value
                    new_lst[i][j] +=value
                else:
                    value = (-lst[i+1][j] + lst[i][j]) // 5
                    new_lst[i+1][j] += value
                    new_lst[i][j] -= value
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            lst[i][j] += new_lst[i][j]
    # print("물고기 조절")
    # print(*lst, sep='\n')
    # print()
    new_lst = []
    for j in range(len(lst[-1])):
        for i in range(1, len(lst)+1):
            if j >=len(lst[-i]):break
            new_lst.append(lst[-i][j])
    lst = new_lst
    # print(lst)
    if max(lst)-min(lst)<=K:break
print(time)
