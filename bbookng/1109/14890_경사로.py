import sys
input = sys.stdin.readline

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

def solution(check):
    flag = False
    for i in range(1, N):
        if abs(check[i-1] - check[i]) > 1:      # 차이가 1 이상이면 경사로 놓을 수 없음
            return flag
        if check[i] < check[i-1]:               # 전의 칸이 더 클 경우
            for j in range(L):
                # 범위 안에 있고 경사로가 놓여있지 않고 높이가 같을 때
                if i + j < N and not visited[i + j] and check[i] == check[i + j]:
                    visited[i + j] = 1
                else:
                    return flag
        elif check[i] > check[i-1]:             # 뒤의 칸이 더 클 경우
            for j in range(L):
                if i - j - 1 >= 0 and not visited[i - j - 1] and check[i - 1] == check[i - j - 1]:
                    visited[i - j - 1] = 1
                else:
                    return flag
    flag = True
    return flag

for i in range(N):
    visited = [0] * N
    if solution(arr[i]):
        result += 1

for j in range(N):
    visited = [0] * N
    tmp = [arr[i][j] for i in range(N)]
    if solution(tmp):
        result += 1

print(result)

