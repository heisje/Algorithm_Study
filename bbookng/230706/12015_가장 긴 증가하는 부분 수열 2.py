N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N
def solution(start, end, pivot):
    if start > end:
        return 0
    if start == end:
        return 1
    solution(start, pivot)

    return


for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))