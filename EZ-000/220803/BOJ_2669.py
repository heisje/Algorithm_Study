import sys

arr = [[0] * 100 for _ in range(100)]

for _ in range(4):
    x, y, i, j = map(int, sys.stdin.readline().split())
    for n in range(x, i):
        for m in range(y, j):
            arr[n][m] = 1

area = 0
for a in arr:
    area += a.count(1)

print(area)
