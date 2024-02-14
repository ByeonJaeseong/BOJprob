'''
시간 비교용 sort 써보기
'''
N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort()
for i in range(N):
    print(lst[i])