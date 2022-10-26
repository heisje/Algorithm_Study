import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N+1)                                            # dp table 생성

for i in range(N-1, -1, -1):                                # 마지막날 부터 돌기
    if i + arr[i][0] > N:                                   # 퇴사 날을 초과하면
        dp[i] = dp[i+1]                                     # 상담할 수 없기 때문에 다음날 값 그대로 할당
    else:
        dp[i] = max(dp[i+1], dp[i+arr[i][0]] + arr[i][1])   # dp[i+1]의 보상, i번째 상담을 했을 경우의 보상 비교

print(dp[0])

