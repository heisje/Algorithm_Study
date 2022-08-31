# 68ms / 실버3
import sys
input = lambda : sys.stdin.readline().strip()

DP = [0] * 101
DP[1] = 1
DP[2] = 1
DP[3] = 1
for i in range(4, 101):
    DP[i] = DP[i-3] + DP[i-2]

T = int(input())
for _ in range(T):
    print(DP[int(input())])