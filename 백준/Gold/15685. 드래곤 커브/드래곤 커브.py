def dragon_curve(n, lst):
    global dir
    if n == g:
        dir = lst
        return lst

    new = []
    for i in range(1,len(lst)+1):
        new.append((lst[-i]+1)%4)

    dragon_curve(n+1, lst+new)

N = int(input())
dragon = [list(map(int, input().split())) for _ in range(N)]
dy = (0, -1, 0, 1)
dx = (1, 0, -1, 0)
st = set([])
for i in range(N):
    x, y, d, g = dragon[i]
    dir = []
    dragon_curve(0, [d])
    st.add((x,y))
    for j in dir:
        x, y = x+dx[j], y+dy[j]
        st.add((x,y))
count = 0
# print(st)
for i in range(102):
    for j in range(102):
        if (i,j) in st and (i+1 ,j) in st  and (i,j+1) in st and (i+1,j+1) in st:
            count+=1
print(count)