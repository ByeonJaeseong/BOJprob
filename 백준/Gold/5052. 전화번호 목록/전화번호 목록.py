TC = int(input())
for _ in range(TC):
    N = int(input())
    bells = [input() for _ in range(N)]
    st1 = set([])
    st2 = set([])
    before_size = 0
    after_size = 0
    marker = True
    for i in range(1,11):
        for j in bells:
            if len(j)>i:
                st1.add(j[0:i])
            elif len(j)==i:
                st2.add(j)
        before_size=len(st1)
        after_size = len(st1-st2)
        if before_size != after_size:
            marker = False
    if marker :
        print("YES")
    else:
        print("NO")