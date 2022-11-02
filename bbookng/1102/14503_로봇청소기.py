import sys
input = sys.stdin.readline

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def solution(x, y, d):
    arr[x][y] = 2
    result = 1

    while True:
        for _ in range(4):
            d = (d + 3) % 4
            nx, ny = x + directions[d][0], y + directions[d][1]
            if 0 <= nx < N and 0 <= ny < M and not arr[nx][ny]:
                arr[nx][ny] = 2
                result += 1
                x, y = nx, ny
                break
        else:
            x, y = x - directions[d][0], y - directions[d][1]
            if arr[x][y] == 1:
                return result

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(solution(r, c, d))