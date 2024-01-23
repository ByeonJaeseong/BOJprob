N = int(input())
lst = [float(input()) for _ in range(N)]
result_lst = []
mx = max(lst)
result_lst.append(mx)
for i in range(N):
    result = lst[i]
    for j in range(i+1, N):
        result *= lst[j]
        if result > mx :
            result_lst.append(result)
print('%.3f'%max(result_lst))