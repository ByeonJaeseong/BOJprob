
''' 
코드를 예쁘게
'''


def search(n, player, team = []):
    global mn
    if n==N//2:
        total = 0
        team1 = []
        team2 = []
        for i in range(N):
            if i in team:
                team1.append(i)
            else:
                team2.append(i)

        for i in range(n):
            for j in range(i+1,n):
                t1, t2 = team1[i], team1[j]
                t3, t4 = team2[i], team2[j]
                total = total+matrix[t1][t2]+matrix[t2][t1]
                total = total - matrix[t3][t4] - matrix[t4][t3]
        mn = min(mn, abs(total))
        return
    if player>=N:
        return
    search(n+1, player+1, team+[player])
    #선수를 포함한 경우
    search(n, player+1, team)
    #선수를 포함하지 않은 경우

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
sm = sum([sum(matrix[i]) for i in range(N)])
mn = 2_100_000_000
search(0,0,[])
print(mn)
