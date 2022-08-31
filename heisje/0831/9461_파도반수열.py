#아이디어: 그냥 수열규칙을 열심히 고민해봤따.... 그랬는데 이전꺼랑 5번째 전꺼를 더하는거였다...

T = int(input())
for _ in range(T):
    N = int(input())
    dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12] + [-1] * 100
    i = 10
    while i <= N - 1:
        dp[i] = dp[i - 1] + dp[i - 5]
        i += 1
    print(dp[N - 1])