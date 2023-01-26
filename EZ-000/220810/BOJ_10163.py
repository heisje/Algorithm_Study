import sys

N = int(sys.stdin.readline())
arr = [[0] * 1001 for _ in range(1001)]

for order in range(1, N + 1):
    x, y, w, h = map(int, sys.stdin.readline().split())
    for n in range(x, x + w):
        for m in range(y, y + h):
            arr[n][m] = order

for order in range(1, N + 1):
    area = 0
    for a in arr:
        area += a.count(order)
    print(area)
    