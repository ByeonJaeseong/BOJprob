'''
합 4 차4 1행 3행 x=y 합8
....x....
.A.I.D.x.
..x...x..
.x.x.x.x.
....x....
'''
import copy


def filling(n, sum1, sum2, sum3, sum4, sum5, sum6, result=[]):
    global matrix, visit, number, lst, marker, word, result_matrix
    # print("ehckr")
    if n>=12:
        if sum1 == 26 and sum2 == 26 and sum3 ==26 and sum4 == 26 and sum5 == 26 and sum6 == 26:
            marker =True
            result_matrix = result
            return
    elif sum1>26 or sum2>26 or sum3>26 or sum4>26 or sum5>26 or sum6>26 :
        return
    elif marker:
        return
    else:
        x = lst[n][0]
        y = lst[n][1]
        # print(x,y, sum1, sum2, sum3, sum4, sum5, sum6)
        if matrix[x][y] == 'x':
            for i in range(1,13):
                temp1, temp2, temp3, temp4, temp5, temp6 =sum1,sum2,sum3,sum4,sum5,sum6
                if not visit[i]:
                    visit[i]=True
                    matrix[x][y]=word[i]
                    if x+y==4:
                        temp1+=i
                    if y-x==4:
                        temp2+=i
                    if x==1 :
                        temp3+=i
                    if x==3:
                        temp4+=i
                    if x==y:
                        temp5+=i
                    if x+y==8:
                        temp6+=i
                    filling(n+1,temp1,temp2,temp3,temp4,temp5,temp6,result+[i])
                    visit[i]=False
                    matrix[x][y]='x'
        else:
            temp1, temp2, temp3, temp4, temp5, temp6 = sum1, sum2, sum3, sum4, sum5, sum6
            if x+y==4:
                temp1+=number[matrix[x][y]]
            if y-x==4:
                temp2+=number[matrix[x][y]]
            if x==1 :
                temp3+=number[matrix[x][y]]
            if x==3:
                temp4+=number[matrix[x][y]]
            if x==y:
                temp5+=number[matrix[x][y]]
            if x+y==8:
                temp6+=number[matrix[x][y]]
            filling(n+1,temp1,temp2,temp3,temp4,temp5,temp6, result+[number[matrix[x][y]]])



matrix=[list(input()) for _ in range(5)]
result_matrix =[]
number ={'A':1,'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9,'J':10 ,'K':11, 'L':12}
word ={1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I',10:'J' ,11:'K', 12:'L'}
visit = [False]*13
marker = False
for i in range(5):
    for j in range(9):
        if not matrix[i][j] in ['.', 'x']:
            visit[number[matrix[i][j]]]=True
lst = [[0,4], [1,1], [1, 3], [1,5], [1, 7], [2,2], [2,6], [3,1], [3,3], [3,5], [3,7], [4,4]]
filling(0,0,0,0,0,0,0)

for i in range(len(lst)):
    matrix[lst[i][0]][lst[i][1]]=word[result_matrix[i]]
for i in range(5):
    print(("").join(matrix[i]))