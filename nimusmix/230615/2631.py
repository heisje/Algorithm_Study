import sys
input = sys.stdin.readline

def sol():
    N = int(input())
    kids = [int(input()) for _ in range(N)]
    dp = [1 for _ in range(N)]
    
    for i in range(1, N):
        for j in range(0, i):
            if kids[i] > kids[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    print(N - max(dp))
    
sol()