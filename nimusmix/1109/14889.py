from itertools import combinations
import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())
stat = [list(map(int, input().split())) for  _ in range(N)]
minS = 20001

team = set(range(N))
for team_a in combinations(range(N), N//2):
    team_b = list(team - set(team_a))

    a_score = b_score = 0
    for i in range(N//2):
        for j in range(i+1, N//2):
            a_score += stat[team_a[i]][team_a[j]]
            a_score += stat[team_a[j]][team_a[i]]
            b_score += stat[team_b[i]][team_b[j]]
            b_score += stat[team_b[j]][team_b[i]]

    minS = min(minS, abs(a_score - b_score))

print(minS)