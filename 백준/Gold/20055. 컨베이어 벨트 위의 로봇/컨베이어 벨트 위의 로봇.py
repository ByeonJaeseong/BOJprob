'''
내구도 같이 이동
1에서 올라감
내구도는 로봇을 올리거나 로봇이 직접 이동할때만 감소
즉 같이 돌아갈때는 감소안함
2N에서 끝남
1. 한칸 돔(내구도가 도는거지)(OK)
2. 앞에 내구도가 다 닳지 않고 로봇이 없으면 이동
3. 내구도가 0이 아니면 로봇 올리기(OK)
4. 0인 칸의 개수가 K개 이상이면 과정 종료(OK)
내리는거 구현해야함
'''
import copy

def count(dura=[]):
    num = 0
    for i in range(len(dura)):
        if dura[i]==0:
            num+=1
    if num>=K:
        return True
    else:
        return False


N, K= map(int, input().split())
#N 벨트 길이, K 내구도 0의 개수
lst = list(map(int, input().split()))
# print(lst)
# 내구도
robot_loc = [False]*(2*N)
result = 0
while True:
    if count(lst):
        break
    else:
        result+=1
    # print(lst, robot_loc)
    temp_lst, temp_loc = lst[2*N-1], robot_loc[2*N-1]

    lst = [temp_lst]+lst[:2*N-1]
    # print(lst)
    robot_loc = [temp_loc]+robot_loc[:2*N-1]
    # 한캄 돔
    # print(lst, robot_loc)
    if robot_loc[N-1]:
        robot_loc[N-1]=False
    #한칸 돌고 로봇이 내릴 수 있으면
    for i in range(0,N-1):
        if not robot_loc[N-2-i]:continue
        # 로봇이 없다면 실행 안함

        if lst[N-1-i]!=0 and not robot_loc[N-1-i]:
            lst[N-1-i]-=1
            robot_loc[N-1-i]=True
            robot_loc[N-2-i]=False
        # 있으면 돌리기
    if robot_loc[N-1]:
        robot_loc[N-1]=False
    # 로봇이 이동한 후 내리면
    if lst[0] != 0:
        lst[0] -= 1
        robot_loc[0] = True
print(result)

