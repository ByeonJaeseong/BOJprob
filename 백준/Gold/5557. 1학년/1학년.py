N = int(input())
lst = list(map(int, input().split()))
traget_lst = [0]*21
temp_list = [0]*21
traget_lst[lst[0]]=1
for i in range(1,N-1):
    # print(traget_lst)
    for j in range(21):
        if traget_lst[j]!=0 :
            if j-lst[i]>=0:
                temp_list[j-lst[i]]+=traget_lst[j]
            if j +lst[i]<=20:
                temp_list[j+lst[i]]+=traget_lst[j]
        else:
            continue
    for j in range(21):
        traget_lst[j] = temp_list[j]
    temp_list = [0]*21

print(traget_lst[lst[N-1]])
