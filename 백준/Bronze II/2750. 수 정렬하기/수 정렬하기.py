def merge_sort(lst):
    # print(lst)
    if len(lst) == 1:
        return lst
    else:
        lst_1 = lst[0:len(lst)//2]
        lst_2 = lst[len(lst)//2:]
        lst1 = merge_sort(lst_1)
        lst2 = merge_sort(lst_2)
        temp_lst = []
        x1, x2 = 0, 0
        while x1<len(lst1) and x2<len(lst2):
            if lst1[x1]>lst2[x2]:
                temp_lst.append(lst2[x2])
                x2+=1
            else:
                temp_lst.append(lst1[x1])
                x1 += 1
        if x1 == len(lst1):
            # print("실")
            temp_lst.extend(lst2[x2:])
        else:
            # print("행")
            temp_lst.extend(lst1[x1:])
        # print("lst",lst,"temp",temp_lst, x1, x2)
    return temp_lst

N = int(input())
lst = [int(input()) for _ in range(N)]
# print(lst)
sort_lst =merge_sort(lst)
# print(sort_lst)
for i in range(N):
    print(sort_lst[i])
