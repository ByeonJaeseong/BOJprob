lst = list(input())
height = 10
for i in range(1, len(lst)) :
    if lst[i] == lst[i-1]:
        height+=5
    else:
        height+=10
print(height)
