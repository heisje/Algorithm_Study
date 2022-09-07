import sys
input = sys.stdin.readline

def sol():
    dp = [100001] * 100001

    for i in range(N+1):                            # 뒤로 -1 갈 경우를 생각하여 N 이전에 dp table 채우기
        dp[i] = N-i

    for i in range(N+1, K+1):                       # 순간이동을 한 뒤 숫자는 짝수이기 때문에 짝수를 기준으로 조건 분기
        if i % 2:                                   # i가 홀수라면
            dp[i] = min(dp[i-1]+1, dp[(i+1)//2]+2)  # 걷는 것과 i+1//2 번째에서 순간이동 하여 한 칸 뒤로 갔을 경우 중 작은 값 할당
        else:                                       # i가 2의 배수라면
            dp[i] = min(dp[i-1]+1, dp[i//2]+1)      # i-1에서 걷는것과 i//2 에서 순간이동 한 것 중 작은 값 할당

    return dp[K]

N, K = map(int, input().split())

print(sol())