# 112ms
import sys
input = lambda: sys.stdin.readline().strip()

N, K = map(int, input().split())
lst = list(map(int, input().split()))
maxV = sum(lst[0:K])
tmp = maxV

for i in range(K, N):
    tmp = tmp - lst[i-K] + lst[i]
    if maxV < tmp:
        maxV = tmp

print(maxV)