N = int(input())
lst = list(map(int, input().split()))
count = 3_000_000_001
real_value = 3_000_0001
result = [0, 0,  0]
lst.sort()
'''정렬 해놓은 상황에서 투포인터를 사용하면
이게 어차피 끽해봐야 5000*5000
'''
for i in range(N-2):
    j = i+1
    k = N-1
    marker = False
    while j<k:
        value = lst[i]+lst[j]+lst[k]
        if abs(value)<count:
            count = abs(value)
            result[0] = i
            result[1] = j
            result[2] = k

        if value == 0 :
            marker = True
            break
        elif value>0:
            k-=1
        else :
            j+=1

    if marker :
        break
print(lst[result[0]], lst[result[1]], lst[result[2]])