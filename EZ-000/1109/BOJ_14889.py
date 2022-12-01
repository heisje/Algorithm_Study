from itertools import combinations
import sys
input = sys.stdin.readline


def calc_stats(all_stats, team):
    stats = 0
    for i in range(teamN):
        for j in range(i, teamN):
            a = team[i]
            b = team[j]
            stats += all_stats[a][b] + all_stats[b][a]
    return stats


N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, input().split())))

teamN = int(N / 2)
combs = list(combinations(range(0, N), teamN))
L = int(len(combs) / 2)

min_dif = 100 * teamN
for idx in range(L):
    start = combs[idx]
    link = combs[-idx - 1]
    startS = calc_stats(S, start)
    linkS = calc_stats(S, link)

    temp = abs(startS - linkS)
    if temp < min_dif:
        min_dif = temp

print(min_dif)
