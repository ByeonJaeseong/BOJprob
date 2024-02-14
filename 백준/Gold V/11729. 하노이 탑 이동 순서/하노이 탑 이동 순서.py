N = int(input())

onetotwo = [[] for _ in range(N)]
twotothree = [[] for _ in range(N)]
onetothree = [[] for _ in range(N)]
twotoone = [[] for _ in range(N)]
threetotwo = [[] for _ in range(N)]
threetoone = [[] for _ in range(N)]
onetotwo[0].append([1,2])
twotothree[0].append([2,3])
onetothree[0].append([1,3])
twotoone[0].append([2,1])
threetotwo[0].append([3,2])
threetoone[0].append([3,1])
# print(onetotwo[0]+[[1,2]])
for i in range(1, N):
    onetotwo[i] = onetothree[i-1] +[[1,2]]+threetotwo[i-1]
    onetothree[i] = onetotwo[i - 1] + [[1, 3]] + twotothree[i - 1]
    twotothree[i] = twotoone[i - 1] + [[2, 3]] + onetothree[i - 1]
    twotoone[i] = twotothree[i - 1] + [[2, 1]] + threetoone[i - 1]
    threetoone[i] = threetotwo[i - 1] + [[3, 1]] + twotoone[i - 1]
    threetotwo[i] = threetoone[i - 1] + [[3, 2]] + onetotwo[i - 1]
print(len(onetothree[N-1]))
for i in range(len(onetothree[N-1])):
    if i  != len(onetothree[N-1])-1:
        print(*onetothree[N-1][i])
    else:
        print(*onetothree[N - 1][i], end="")