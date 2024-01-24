N = int(input())
lst = list(map(int, input().split()))
lst1 = [[lst[i], i] for i in range(N)]
# print(lst1)
lst2 = sorted(lst1)
# print(lst2)
temp = min(lst)
comp = 0
for i in range(N):
    if lst2[i][0]==temp:
        lst2[i][0] = comp
    else:
        comp +=1
        temp = lst2[i][0]
        lst2[i][0] = comp

# print(lst2)
lst3=[]
for i in range(N):
    lst3.append([lst2[i][1], lst2[i][0]])

result = sorted(lst3)

for i in range(N):
    print(result[i][1], end=" ")