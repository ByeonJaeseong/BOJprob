'''
N-Queen 과 같은 방식으로 좌하- 우상대각선 좌상-우하 대각선 체크
전 탐 하면서 결괏값 체크
'''
def bishop(n,count):
    global matrix
    global result
    global cross_right, cross_left
    global N
    # print(n, count,cross_right)
    if n==2*N-1:
        result = max(result,count)
        return
    elif count + (2*N-1-n)<=result:
        return
    else:
        #########대각선으로 조사
        if n<N:
            for i in range(n+1):
                if matrix[i][n-i]==1 and not cross_right[2*i-n]:
                    cross_right[2*i-n]=True
                    bishop(n+1,count+1)
                    cross_right[2 * i - n] = False
            bishop(n + 1, count)

        else:
            # print("실행되었습니다.", 2*N-n-1, n)
            for i in range(2*N-n-1):
                if matrix[N-1-i][n-N+i+1]==1 and not cross_right[(2*N-n-2*i-2)]:
                    cross_right[(2*N-n-2*i-2)]=True
                    bishop(n+1,count+1)
                    cross_right[(2*N-n-2*i-2)] = False
            bishop(n + 1, count)



N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
result = 0
cross_right = [False]*(2*N-1)
bishop(0,0)
print(result)