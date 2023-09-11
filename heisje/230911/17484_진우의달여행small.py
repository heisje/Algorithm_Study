# 40ms
# 우주선은 좌 아래 우로만 움직이고 같은 방향으로 두번 연속 움직일 수 없다.
# 연료의 최소값

N, M = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]

dp = [[[10000000, 100000000, 1000000000] for _ in range(M)] for _ in range(N)]

for m in range(M):
    for i in range(3):
        dp[0][m][i] = li[0][m]

for n in range(N-1):
    # 오른쪽 대각선
    for m in range(M-1):
        temp = min(dp[n][m][1], dp[n][m][2])
        if temp < dp[n+1][m+1][1]:
            dp[n+1][m+1][0] = temp + li[n+1][m+1]
    # 아래
    for m in range(M):
        temp = min(dp[n][m][0], dp[n][m][2])
        if temp < dp[n+1][m][1]:
            dp[n+1][m][1] = temp + li[n+1][m]
    # 왼쪽 대각선
    for m in range(1, M):
        temp = min(dp[n][m][0], dp[n][m][1])
        if temp < dp[n+1][m-1][2]:
            dp[n+1][m-1][2] = temp + li[n+1][m-1]
    
answer = []
for d in dp[-1]:
    answer.append(min(*d))
print(min(answer))

