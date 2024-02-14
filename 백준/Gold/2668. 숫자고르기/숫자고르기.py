'''
사이클인지 아닌지를 찾고 사이클인 것들을 합해서 최댓값을 구하고 끝
'''


def is_cycle(n,st=set([])):
    global start, lst, visit
    if cycle[n] or visit[n] : return
    if n in st: return
    if start == lst[n]:
        cycle[n] = True
    elif lst[n]<=N:
        st.add(n)
        cycle[n] = is_cycle(lst[n], st)

    return cycle[n]



N = int(input())
mx = 0
lst = [0] + [int(input()) for _ in range(N)]
visit = [False]*(N+1)
cycle = [False]*(N+1)
for i in range(1, N+1):
    if i == lst[i]:
        visit[i]=True
        cycle[i]=True
for i in range(1, N+1):
    start = i
    is_cycle(i, set([]))
    visit[i]=True

result = ""
for i in range(1, N+1):
    if cycle[i]:
        mx+=1
        result+=str(i)+"\n"

print(mx)
print(result)

