N = int(input())
lst = list(map(int,input().split()))
index_lst= []
result_lst=[-1]*N
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
                    # print("temp_lst",temp_lst)
                    result_lst[temp_lst[1]]=lst[i]

                    # print(i, index, "실행되었습니다")
                else:
                    stk.append([lst[i],i])
                    break

        else:
            stk.append([lst[i],i])

    index_lst.append([index, i, lst[i]])

# print(index_lst)

# for i in index_lst:
#     for j in range(i[0], i[1]):
#         if result_lst[j]==-1:
#             result_lst[j]=i[2]

for i in result_lst:
    print(i, end= " ")
