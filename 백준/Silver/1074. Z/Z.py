N, r, c = map(int, input().split())
result = []
for i in range(N):
    result.append(r // 2**(N-1-i))
    result.append(c // 2**(N-1-i))
    r = r % 2 ** (N-1-i)
    c = c % 2 ** (N - 1 - i)
cal = 0
# print(result)
for i in range(2*N):
    if result[i]!=0:
        cal+=2**(2*N-i-1)
print(cal)