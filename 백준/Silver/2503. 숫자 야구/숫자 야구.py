import itertools


def number(n, numbers=[]):
    global matrix, lst, lst2, count
    if n == N:
        count +=1
        return
    strike = 0
    total = 0
    for i in range(3):
        if str(numbers[i])==lst2[n][i]:
            strike+=1
        if str(numbers[i]) in lst[n]:
            total +=1
    # print(numbers, strike, total)
    if str(strike) == matrix[n][1] and str((total-strike)) == matrix[n][2]:
        number(n+1, numbers)
    else:
        return



N = int(input())
matrix = [list(input().split()) for _ in range(N)]
lst = [set(list(matrix[i][0])) for i in range(N)]
lst2 = [list(matrix[i][0]) for i in range(N)]
# print(lst2)
count = 0
permu = list(itertools.permutations([1,2,3,4,5,6,7,8,9], 3))
for i in permu:
    number(0, list(i))
print(count)