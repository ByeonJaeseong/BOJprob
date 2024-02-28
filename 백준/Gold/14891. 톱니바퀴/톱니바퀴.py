'''
톱니 8개 톱니바퀴 4개
하나를 회전 시키고 나면 다음은 영향을 받아서 회전
같은극이면 반대방향으로 회전
location 변수 4개 놓고 회전에 따라서
시계방향으로 가면 오른쪽 이동
반 시계 방향으로 가면 왼쪽 이동 이런식의 접근 가능
반대 방향은 +4를 해주면 확인 가능
'''
lst1 = list(map(int, input()))
lst2 = list(map(int, input()))
lst3 = list(map(int, input()))
lst4 = list(map(int, input()))
loc1 = 2
loc2 = [6, 2]
loc3 = [6, 2]
loc4 = 6
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
# print(lst1)
# print(lst2)
# print(lst3)
# print(lst4)
# print(matrix)
for i in range(N):
    # print(loc1, loc2, loc3, loc4, i)
    rotate = [0]*4
    marker = True
    matrix[i][1] = -matrix[i][1]
    if matrix[i][0] == 1:
        rotate[0]+=matrix[i][1]
        # 돌리고 2번이 돌아가는지 체크 아니면 그만 돌리기
        if lst1[loc1] != lst2[loc2[0]]:
            rotate[1] -= matrix[i][1]
        else:
            marker = False
        # 2번 돌아가면 3번 확인하기
        if lst2[loc2[1]] != lst3[loc3[0]] and marker:
            rotate[2] +=  matrix[i][1]
        else:
            marker=False
        # 3번 돌아가면 4번 확인하기
        if lst3[loc3[1]] != lst4[loc4] and marker:
            rotate[3] -= matrix[i][1]
        else:
            marker = False
    elif matrix[i][0] == 2:
        rotate[1] +=matrix[i][1]
        if lst2[loc2[0]] != lst1[loc1]:
            rotate[0] -= matrix[i][1]
        if lst2[loc2[1]] != lst3[loc3[0]]:
            rotate[2] -= matrix[i][1]
        else:
            marker = False
        # 3번 돌아가면 4번 확인하기
        if lst3[loc3[1]] != lst4[loc4] and marker:
            rotate[3] +=matrix[i][1]
        else:
            marker = False
    elif matrix[i][0] == 3:
        rotate[2]+=matrix[i][1]
        # 4번 확인하기
        if lst3[loc3[1]] != lst4[loc4]:
            rotate[3]-=matrix[i][1]
        # 2번 확인하기
        if lst3[loc3[0]] != lst2[loc2[1]] and marker:
            rotate[1]-=matrix[i][1]
        else:
            marker=False
        # 2번 돈 경우 1번 확인하기
        if lst2[loc2[0]] != lst1[loc1] and marker:
            rotate[0]+=matrix[i][1]
    else:
        rotate[3] +=matrix[i][1]
        # 돌리고 3번이 돌아가는지 체크 아니면 그만 돌리기
        if lst4[loc4] != lst3[loc3[1]]:
            rotate[2]-=matrix[i][1]
        else:
            marker = False
        # 2번 돌아가면 3번 확인하기
        if lst3[loc3[0]] != lst2[loc2[1]] and marker:
            rotate[1]+=matrix[i][1]
        else:
            marker=False
        # 3번 돌아가면 4번 확인하기
        if lst2[loc2[0]] != lst1[loc1] and marker:
            rotate[0]-=matrix[i][1]
        else:
            marker=False
    # print(rotate)
    loc1 = (loc1+rotate[0])%8
    loc2[0], loc2[1] = (loc2[0]+rotate[1])%8, (loc2[1]+rotate[1])%8
    loc3[0], loc3[1] = (loc3[0] + rotate[2]) % 8, (loc3[1] + rotate[2]) % 8
    loc4  = (loc4+rotate[3])%8

result = lst1[loc1-2] + lst2[loc2[1]-2] * 2 + lst3[loc3[1]-2] * 4 + lst4[ loc4-6] * 8
# print(loc1, loc2[1], loc3[1], loc4)
print(result)