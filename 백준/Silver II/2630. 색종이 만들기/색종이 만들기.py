
def divide(matrix):
    global white, blue
    if len(matrix) == 1:
        if matrix[0][0] == 1:
            blue +=1
            return
        else:
            white +=1
            return

    n = len(matrix)
    matrix1 = [matrix[i][0:n//2] for i in range(n//2)]
    matrix2 = [matrix[i][0:n//2] for i in range(n//2, n)]
    matrix3 = [matrix[i][n//2:] for i in range(n//2)]
    matrix4 = [matrix[i][n//2:] for i in range(n//2, n)]
    st1 = set([])
    st2 = set([])
    st3 = set([])
    st4 = set([])

    for i in range(n//2):
        for j in range(n//2):
            st1.add(matrix1[i][j])
            st2.add(matrix2[i][j])
            st3.add(matrix3[i][j])
            st4.add(matrix4[i][j])

    if len(st1) == 1:
        if st1.pop() == 1:
            blue +=1
        else:
            white +=1
    else:
        divide(matrix1)

    if len(st2) == 1:
        if st2.pop() == 1:
            blue +=1
        else:
            white +=1
    else:
        divide(matrix2)

    if len(st3) == 1:
        if st3.pop() == 1:
            blue +=1
        else:
            white +=1
    else:
        divide(matrix3)

    if len(st4) == 1:
        if st4.pop() == 1:
            blue +=1
        else:
            white +=1
    else:
        divide(matrix4)

blue = 0
white = 0
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
st = set([])
for i in range(N):
    for j in range(N):
        st.add(matrix[i][j])
if len(st)==1:
    if st.pop()==1:
        blue+=1
    else:
        white+=1
else:
    divide(matrix)
print(white, blue, sep="\n")