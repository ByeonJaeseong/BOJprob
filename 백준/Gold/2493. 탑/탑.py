N = int(input())
tem_lst = list(map(int,input().split()))
lst = []
for i in range(N):
    lst.append(tem_lst[N-i-1])
index_lst= []
result_lst=[0]*N
stk = []
stk.append([lst[0],0])# value, index
for i in range(1, N):
    index = i
    # print(stk)
    if not stk :
        stk.append([lst[i],i])
    else:
        if stk[-1][0]<lst[i]:
            while True:
                if index !=0 and stk and stk[-1][0]<lst[i]:
                    temp_lst=stk.pop()
                    result_lst[temp_lst[1]]=N-i
                else:
                    stk.append([lst[i],i])
                    break

        else:
            stk.append([lst[i],i])

    index_lst.append([index, i, lst[i]])
for i in range(len(result_lst)):
    print(result_lst[N-1-i], end= " ")
