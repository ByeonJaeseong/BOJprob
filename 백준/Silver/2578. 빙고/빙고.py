
def bingo_search(x, y):
    temp = 0
    global count
    global visit
    global bingo
    for i in range(5):
        if visit[i][y] :
            temp+=1
        else :
            break
    if temp == 5:
        count+=1
    temp = 0
    for i in range(5):
        if visit[x][i] :
            temp+=1
        else :
            break
    if temp == 5:
        count+=1
    temp = 0

    if x==y:
        for i in range(5):
            if visit[i][i]:
                temp += 1
            else:
                break
    if temp == 5:
        count+=1
    temp = 0

    if x+y == 4:
        for i in range(5):
            if visit[i][4-i]:
                temp += 1
            else:
                break
    if temp == 5:
        count += 1
    temp = 0

def mark(n):
    global bingo
    for i in range(5):
        for j in range(5):
            if bingo[i][j]==n :
                # print("리턴되었습니다")
                return [i, j]
                break


bingo = [list(map(int, input().split())) for _ in range(5)]
call = [list(map(int, input().split())) for _ in range(5)]
visit = [[False]*5 for _ in range(5)]
count = 0
numbers = 0
for i in range(5):
    marker = False
    for j in range(5):
        # print(bingo)
        # print(call)
        # print(call[i][j], mark(call[i][j]))
        x, y = mark(call[i][j])[0], mark(call[i][j])[1]
        visit[x][y] = True
        bingo_search(x, y)
        numbers+=1
        # print (count)
        # if numbers==15:break
        if count>=3:
            marker = True
            break
    if marker : break

# for i in range(5):
#     print(visit[i])
print(numbers)