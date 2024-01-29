N = int(input())
lst = []
temp = 0
stk = []
result = []
visit = [False]*(N+1)
marker = True
for i in range(N):
    lst.append(int(input()))
# print(lst)
for j in range(1, lst[0] + 1):
    stk.append(j)
    visit[j] = True
    result.append("+")
stk.pop()
result.append("-")
# print(stk)
for i in range(1, N):
    temp = lst[i]
    if len(stk)==0:
        # print("실행")
        for j in range(1, temp+1):
            if not visit[j]:
                stk.append(j)
                visit[j]=True
                result.append("+")
    if stk[-1]<temp:
        # print(temp, "시일행 되었습니다")
        for j in range(stk[-1], temp+1):
            if not visit[j]:
                stk.append(j)
                visit[j]=True
                result.append("+")
    if stk[-1] == temp :
        stk.pop()
        result.append("-")
        # print(temp, "실행되었습니다")
# print(result)
# print(stk)
if not stk:
    for i in range(len(result)):
        print(result[i])
else:
    print("NO")

