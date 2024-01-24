import math
N = int(input())
count = 0
# print(int(math.sqrt(N)))
for i in range(1, int(math.sqrt(2*N))+1):
    if (2*N)%i ==0:
        if (i % 2 == 0 and (int((2*N)/i))%2 ==1) or (i % 2 == 1 and (int((2*N)/i))%2 ==0):
            #print(i)
            count+=1
print(int(count))