import sys

input = lambda: sys.stdin.readline().strip()

N = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * (N+1)

for i in range(N-1, -1, -1):                    # 마지막 날부터 순회
    T, P = schedule[i]                          # day i의 상담에 걸리는 시간과 금액
    
    if i + T > N:                               # day i의 상담이 퇴사일 이후에 끝난다면
        dp[i] = dp[i+1]                         # 상담을 진행하지 않음.
    else:                                       # day i의 상담이 퇴사일 이전에 끝난다면
        dp[i] = max(dp[i+1], P + dp[i+T])       # 상담을 진행하지 않았을 때의 수익과
                                                # (day i의 상담액 + 상담이 종료된 익일의 수익) 중 큰 값을 저장
print(dp[0])