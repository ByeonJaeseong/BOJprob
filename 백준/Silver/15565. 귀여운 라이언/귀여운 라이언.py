'''
투포인터 쓰면 될듯? 내일 아침에 다시 풀어서 스트릭 유지
'''
M, N = map(int, input().split())
lst = list(map(int, input().split()))
# print(lst)
start, end = 0, 0
count = 0
length = 10**6+1
while end<=M:
    # print(count)
    if count==N:
        # print(start, end)
        length = min(length, end - start)
    if count<N:
        if end ==M:
            break
        if lst[end] == 1:
            count+=1
        end+=1

    else:
        if lst[start] == 1:
            count -=1
        start+=1
if length != 1000001:
    print(length)
else:
    print(-1)