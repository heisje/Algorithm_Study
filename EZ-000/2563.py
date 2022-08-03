import sys

arr = [[0] * 100 for _ in range(100)]

for _ in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            arr[i][j] = 1

area = 0
for a in arr:
    area += a.count(1)

print(area)
