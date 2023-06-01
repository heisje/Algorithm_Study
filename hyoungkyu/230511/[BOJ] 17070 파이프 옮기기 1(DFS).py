# 골드5 / 868ms (pypy3)
import sys

input = lambda:sys.stdin.readline().strip()

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# status -> -1 : 가로, 0 : 대각선, 1 : 세로

def dfs(arr, i, j, status):
    answer = 0
    # 오른쪽으로 밀 경우
    if (status == -1 or status == 0) and j+1 < N and not arr[i][j+1]:
        if i == N-1 and j+1 == N-1:
            return 1
        if j+1 != N-1:
            answer += dfs(arr, i, j+1, -1)
    # 아래로 밀 경우
    if (status == 1 or status == 0) and i+1 < N and not arr[i+1][j]:
        if i+1 == N-1 and j == N-1:
            return 1
        if i+1 != N-1:
            answer += dfs(arr, i+1, j, 1)
    # 대각선으로 밀 경우
    if i+1 < N and j+1 < N and not arr[i][j+1] and not arr[i+1][j+1] and not arr[i+1][j]:
        if i+1 == N-1 and j+1 == N-1:
            return 1
        answer += dfs(arr, i+1, j+1, 0)
    return answer

ans = dfs(arr, 0, 1, -1)
print(ans)