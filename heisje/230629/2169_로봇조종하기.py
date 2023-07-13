# 1112ms
# 입력받기
# 맨위를 왼쪽으로 옮기며 최대값 산출
# 중간을 왼, 오른쪽으로 옮기며 최대값 산출
# 맨 아래를 왼쪽으로 옮기며 최대값 산출

def main():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0 for _ in range(M)] for _ in range(N)]

    # 맨 윗줄 탐색
    dp[0][0] = grid[0][0]
    for m in range(1, M):
        dp[0][m] = dp[0][m-1] + grid[0][m]  # 앞의 값과 현재 값 누적

    # 종료 조건 - N이 1일 때
    if N == 1:
        return dp[0][M-1]

    # 중간 탐색
    if N >= 3:
        for n in range(1, N-1):
            # 기본값 넣기
            left = [0 for _ in range(M)]
            right = [0 for _ in range(M)]
            for m in range(M):
                left[m] = dp[n - 1][m] + grid[n][m]
                right[m] = dp[n - 1][m] + grid[n][m]
            # 왼, 오른쪽방향 탐색
            for m in range(1, M):
                # 왼(오른)쪽에서 온 것, 위에서 온것 비교
                if left[m - 1] + grid[n][m] > left[m]:
                    left[m] = left[m - 1] + grid[n][m]
                if right[-m] + grid[n][-m-1] > right[-m-1]:
                    right[-m-1] = right[-m] + grid[n][-m-1]
            # 비교
            for m in range(M):
                if left[m] < right[m]:
                    dp[n][m] = right[m]
                else:
                    dp[n][m] = left[m]

    # 마지막 줄 비교    
    # 왼쪽방향 탐색
    dp[N - 1][0] = dp[N - 2][0] + grid[N - 1][0]
    for m in range(1, M):
        # 왼쪽에서 온 것, 위에서 온것 비교
        if dp[N - 1][m - 1] + grid[N - 1][m] > dp[N - 2][m] + grid[N - 1][m]:
            dp[N - 1][m] = dp[N - 1][m - 1] + grid[N - 1][m]
        else:
            dp[N - 1][m] = dp[N - 2][m] + grid[N - 1][m]
    
    return dp[N - 1][M - 1]

print(main())