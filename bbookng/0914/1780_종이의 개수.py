import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = [0, 0, 0]

def solution(x, y, n):
    tmp = arr[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if tmp != arr[i][j]:
                solution(x, y, n // 3)
                solution(x, y + n // 3, n // 3)
                solution(x, y + n // 3 * 2, n // 3)
                solution(x + n // 3, y, n // 3)
                solution(x + n // 3, y + n // 3, n // 3)
                solution(x + n // 3, y + n // 3 * 2, n // 3)
                solution(x + n // 3 * 2, y, n // 3)
                solution(x + n // 3 * 2, y + n // 3, n // 3)
                solution(x + n // 3 * 2, y + n // 3 * 2, n // 3)
                return

    if tmp == -1:
        result[0] += 1
    elif tmp == 0:
        result[1] += 1
    else:
        result[2] += 1

solution(0, 0, N)

for i in result:
    print(i)