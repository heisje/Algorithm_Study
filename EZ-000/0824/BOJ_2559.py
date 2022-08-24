import sys
# 왜 이게 통과되는지 모르겠다.
def accum(n, k, temperatures):
    max_sum = sum(temperatures[:k])
    temp = max_sum
    for i in range(n - k):
        temp = temp - temperatures[i] + temperatures[k + i]
        if temp > max_sum:
            max_sum = temp
    return max_sum


N, K = map(int, sys.stdin.readline().split())
temps = list(map(int, sys.stdin.readline().split()))

print(accum(N, K, temps))
