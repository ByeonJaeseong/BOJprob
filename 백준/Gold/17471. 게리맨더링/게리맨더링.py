import copy
from collections import deque
def gary(n, left=[], right=[]):
    global visit, block
    if n == N:
        if len(left) and len(right):
            block.append([left, right])
        return

    # 끝까지 간건 선거구가 안나눠 진것
    gary(n+1, left+[n], right)
    gary(n+1, left, right+[n])

def linked(left=set([]), right=set([])):
    global mn
    marker = True
    visit = [False]*N
    l = left.pop()
    left.add(l)
    dq = deque()
    dq.append(l)
    visit[l]=True
    left_sum = people[l]
    count =1
    while dq:
        value = dq.popleft()
        for i in range(1,matrix[value][0]+1):
            if not visit[matrix[value][i]] and matrix[value][i] in left:
                visit[matrix[value][i]] = True
                left_sum += people[matrix[value][i]]
                dq.append(matrix[value][i])
                count+=1
    r = right.pop()
    right.add(r)
    dq.clear()
    dq.append(r)
    visit[r]=True
    left_sum-=people[r]
    count+=1
    while dq:
        value = dq.popleft()
        for i in range(1,matrix[value][0]+1):
            if not visit[matrix[value][i]] and matrix[value][i] in right:
                visit[matrix[value][i]] = True
                left_sum -= people[matrix[value][i]]
                dq.append(matrix[value][i])
                count+=1
    # print(count)
    if count == N:
        mn = min(mn, abs(left_sum))


N = int(input())
people = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(N)]
matrix = [[matrix[i][0]]+[matrix[i][j+1]-1 for j in range(matrix[i][0])] for i in range(N)]


# print(matrix)

mn = 200000000
sm = sum(people)
block = []
gary(0, [], [])
# print(block)
for i in range(len(block)//2+1):
    linked(set(block[i][0]), set(block[i][1]))
if mn == 200000000:
    print(-1)
else:
    print(mn)