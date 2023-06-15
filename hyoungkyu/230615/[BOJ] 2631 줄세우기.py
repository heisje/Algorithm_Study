# 48ms
N = int(input())
lst = [int(input()) for _ in range(N)]

DP = [0] * N
DP[0] = 1

for i in range(1, N):
    MAX = 0
    # 왼쪽에서 현재까지 증가하는 수들만 체크
    for j in range(i):
        if lst[i] > lst[j] and MAX < DP[j]:
            MAX = DP[j]
    DP[i] = MAX + 1

print(N-max(DP))