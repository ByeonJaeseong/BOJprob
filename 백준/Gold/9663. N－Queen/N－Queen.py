

# def N_queen_play(n,visit):
#     global N
#     marker = True
#     for i in range(n+1,N):
#         count =0
#         for j in range(N):
#             if visit[i][j]:
#                 count+=1
#         if count==N:
#             marker =False
#             break
#     return marker


def N_queen(n):
    global N
    global count
    if n==N: # 정지시키기
        count+=1
    else:
        for i in range(N):
            marker = True
            for j in range(0, n):
                if board[j][i] == 1:
                    marker = False
                    break
            if marker:
                for j in range(N + 1):
                    if n - j >= 0 and i - j >= 0:
                        if board[n - j][i - j] == 1:
                            marker = False
                            break
                    else:
                        break
            if marker:
                for j in range(N + 1):
                    if n - j >= 0 and i + j < N:
                        if board[n - j][i + j] == 1:
                            marker = False
                            break
                    else:
                        break
            if marker:
                board[n][i]=1
                N_queen(n+1)
                board[n][i]=0


N=int(input())
board = [[0]*N for _ in range(N)]
count =0
N_queen(0)
print(count)