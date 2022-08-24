import sys
input = lambda : sys.stdin.readline().strip()

dp = [0] * 1001                             # 1000까지 있으니까
n = int(input())
for i in range(n):
    a, b = map(int,input().split())
    dp[a] = b                               # dp table에 기둥의 높이 넣기

for i in range(dp.index(max(dp))):          # 왼쪽에서 max값 까지
    if dp[i] > dp[i + 1]:                   # 오른쪽에 있는 값이 자신보다 높아질때 까지 범위에 포함되므로 암튼 큰 값 나올떄 까지
        dp[i+1] = dp[i]                     # 테두리 씌우기

for i in range(1000, dp.index(max(dp)), -1):# 이건 오른쪽에서 max값 까지
        dp[i-1] = dp[i]                     # 마찬가지로 테두리 씌우기

print(sum(dp))


