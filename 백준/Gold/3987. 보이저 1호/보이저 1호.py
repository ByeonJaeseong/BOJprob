'''
리팩토링 할 생각으로 코드를 짜보자
어차피 사이즈가 N*M이라서
워스트 케이스 자체가 25000
걍 전체 돈 횟수가 N*M보다 1이라도 크면 계속 돌고 있음
'''
def check(x,y) :
    return 0<=x<M and 0<=y<N
M, N = map(int, input().split())
matrix = [list(input()) for _ in range(M)]
mx = 0
sx, sy = map(int, input().split())
dx = [-1, 0, 1 ,0]
dy = [0, 1, 0, -1]

rule1 = {0:3, 1:2, 2:1, 3:0} # \ 규칙
rule2 = {0:1, 1:0, 2:3, 3:2}# / 규칙
rule3 = {0:'U', 1:'R', 2:'D', 3:'L'}
#1번 1: 1->4, 4->1
#2번 2->3 3->2
# -> 자리 바꾸기
#3번 1 -> 0, 3->2
# 4번 2->3, 0->1
dir = 0
for i in range(4):

    D = i
    if matrix[sx-1][sy-1] == 'C':
        count = 0
        continue
    if matrix[sx-1][sy-1] == ("\ ".rstrip()):
        D = rule1[D]

    if matrix[sx-1][sy-1] == "/":
        D = rule2[D]

    count = 1
    #자기 자신도세서
    nowx, nowy = sx-1, sy-1
    while count <= 10*M*N:
        X, Y = nowx + dx[D], nowy + dy[D]
        if not check(X,Y) or matrix[X][Y]=='C':break
            #밖으로 나아가버리거나 블랙홀이면

        if check(X,Y)  and matrix[X][Y]=='.' :
            # 안에 있고 나아갈 수 있으면
            nowx, nowy = X, Y
            count +=1
            continue

        if check(X,Y) and matrix[X][Y]==("\ ".rstrip()):
            nowx, nowy = X, Y
            count+=1
            D = rule1[D]
            continue

        if check(X,Y) and matrix[X][Y]=="/":
            nowx, nowy = X, Y
            count+=1
            D = rule2[D]
            continue
    if mx<count:
        mx = count
        dir = i
    # print(count)
if mx > 10*M*N:
    print(rule3[dir])
    print('Voyager')
else:
    print(rule3[dir])
    print(mx)