'''
왼쪽, 오른쪽에서 교차로 하나 씩 파괴
클러스터가 분리되고 밑에 지탱하는게 없으면 떨어짐
바닥은 가장 밑에칸 즉 M-1
사이즈 자체가 100*100*30000

구현해야될 대상
1. 왼쪽 오른쪽 측면에서 미네랄 하나씩 파괴 하기
2. 파괴한 후 그 층을 포함해서 클러스터가 분리되었는지 파악
3. 클러스터가 분리되고 떠있는지 확인
4. 떠있으면 밑으로 가라앉히기
'''
import sys
from collections import deque
# sys.stdin=open("input.txt",'r')

def check(x,y):
    global M, N
    return 0<=x<M and 0<=y<N
# 1번 구현 완료
def throw(h, odd_even): # h는 높이 #몇번째 던지는 건지 -> odd_even이 짝수면 왼쪽 홀수면 오른쪽
    global matrix
    if odd_even%2==0:
        # 0층이 아니라 1층부터 시작하니까 M-1-(h-1)
        # print(M,h)
        for i in range(N):
            if matrix[M-h][i]=='x':
                matrix[M-h][i]='.' #한개 부수기
                break
    else:
        for i in range(N):
            if matrix[M-h][N-1-i]=='x':
                matrix[M-h][N-1-i]='.' #한개 부수기
                break
    # if h==4 and odd_even==3:
    #     for i in range(M):
    #         print(matrix[i])

#2번 구현
#파괴한 층을 포함해서 바로 위층까지만 조사하면 됌-> 어차피 밑에 있는 층은 떨어지지 않을거고 떨어 질 건 위에 있는 층
def cluster(x, y, lst=[]): #높이 h에 있는 것과 h-1칸에 있는
    global matrix, dx, dy, visit
    dq = deque()
    dq.append([x,y])
    lst.append([x,y])
    visit[x][y]=True
    while dq:
        value = dq.popleft()
        # print(dq)
        for i in range(4):
            X = value[0]+dx[i]
            Y = value[1]+dy[i]
            if check(X, Y) and not visit[X][Y] and matrix[X][Y]=='x':
                # 방문 안한 곳에서 붙어있는 미네랄은 클러스터
                visit[X][Y]=True #방문처리하고
                lst.append([X,Y])
                dq.append([X,Y])
    # print("lst", lst)
    return lst
## 클러스터 파악

#3번, 4번 구현
#가장 밑 층이 M-1이 아니면 떠있는 것->가라 앉히기
def down(lst):
    global matrix
    mx = 0
    for i in range(len(lst)):
        mx = max(lst[i][0], mx)
    lst.sort(reverse=True)
    # print(lst, mx)

    mn = 100
    if mx!=M-1:
        for i in range(len(lst)):
            count =0
            # if lst[i][0]==lst[0][0] and matrix[lst[i][0]][lst[i][1]]=='x':
            have_under=True
            for j in range(len(lst)):
                if lst[i][1]==lst[j][1] and lst[i][0]<lst[j][0]:
                    have_under=False
                    break

            if have_under:
                for j in range(lst[i][0]+1, M):
                    # print(matrix[j][lst[i][1]])
                    if matrix[j][lst[i][1]]=='.':
                        count+=1
                    else:
                        break
            # print("mn",mn, "count",count)
            if count!=0:
                mn = min(mn,count)
        # print("mx", mx ,"mn", mn, "lst[0][0]", lst[0][0])
        if mn==100:
            return False
        else:
            for i in range(len(lst)):
                matrix[lst[i][0]+mn][lst[i][1]]='x'
                matrix[lst[i][0]][lst[i][1]] = '.'
            return True




M, N = map(int, input().split()) # M 행 # N 열
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
matrix = [list(input()) for _ in range(M)]
# for i in range(M):
#     print(matrix[i])

repeat = int(input()) # 작대기 횟수
height = list(map(int, input().split()))
for i in range(repeat):
    throw(height[i],i)
    visit = [[False]*N for _ in range(M)]
    # if height[i]!=M:
    for k in range(M):
        marker = False
        for j in range(N):
            if not visit[k][j] and matrix[k][j]=='x':
                # print("height", height[i],k,j)
                re_lst = cluster(k, j,[])
                # for t in range(M):
                #     print(matrix[t])
                # print()
                mark = down(re_lst)
                if mark:
                    marker=True
                    break
        if marker:
            break
    # else:
    #
    #     for j in range(N):
    #         if not visit[M-height[i]][j] and matrix[M-height[i]][j]=='x':
    #             re_lst = cluster(M-height[i], j,[])
    #             mark = down(re_lst)
    #             if mark:
    #                 break
    # # print(i+1, height[i])
    # for t in range(M):
    #     print(matrix[t])
    # print()

for k in range(M):
    if k == M-1:
        print(("").join(matrix[k]), end="")
    else:
        print(("").join(matrix[k]))