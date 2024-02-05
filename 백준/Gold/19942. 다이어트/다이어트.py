'''백트래킹 연습하기에 아주좋은 문제인듯?
주어진 숫자에서 최소 비용을 찾기
최소비용을 기준으로 백트래킹 해가면서 최솟값이하인 경우만 탐색지속
6
단백질 지방 탄수화물 비타민
100 70 90 10
단백질 지방 탄수화물 비타민 가격
30 55 10 8 100
60 10 10 2 70
10 80 50 0 50
40 30 30 8 60
60 10 70 2 120
20 70 50 4 4
'''
def cost(n, i, temp_cost, lst=[]):
    global N
    global target_cost
    global target_lst
    global matrix
    global d,jb,t,b
    if td<=d and tj<=jb and tt<=t and tb<=b:
        if target_cost> temp_cost:
            target_cost = temp_cost
            target_lst=lst
    else:
        for j in range(i,N):
            if not visit[j] and target_cost>temp_cost:#전부다 값이 넘는경우는 아닌경우
                visit[j]=True
                temp_cost += matrix[j][4]
                d += matrix[j][0]
                jb += matrix[j][1]
                t += matrix[j][2]
                b += matrix[j][3]
                cost(n+1, j, temp_cost,lst+[j+1])
                visit[j]=False
                temp_cost -= matrix[j][4]
                d -= matrix[j][0]
                jb -= matrix[j][1]
                t -= matrix[j][2]
                b -= matrix[j][3]


N =int(input())
td, tj, tt, tb = map(int, input().split()) # 타겟값
matrix = [list(map(int, input().split())) for _ in range(N)]
target_cost = 500*15
target_lst=[]
visit = [False]*N
d = 0
jb = 0
t = 0
b = 0
cost(0,0,0,[])
if target_cost == 500*15:
    print(-1)
else:
    print(target_cost)
    print(*target_lst)