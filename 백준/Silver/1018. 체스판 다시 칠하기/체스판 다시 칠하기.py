def search(x,y):
    count1 =0 #[0,0]이 흰색일때 맞는 흰색 격자 갯수 32-count1이 검은 격자 갯수
    count2 =0 #[0,0]의 검정일때 맞는 흰색 격자 갯수 32-count2이 검은 격자 갯수
    for i in range(x, x+8):
        for j in range(y, y+8):
            if (i+j)%2==0 and matrix[i][j]=='W':
                count1+=1
            if (i+j)%2==1 and matrix[i][j]=='W':
                count2+=1
    return min(32-(count1-count2),32-(count2-count1)) #흰검, 검흰 순서 중 최소 출력
M, N = map(int, input().split())
matrix = [list(input()) for _ in range(M)]
mn = 64 #최악의 값 
for i in range(M-7):
    for j in range(N-7):
        mn = min(mn, search(i,j)) # 최솟값 탐색
print(mn)