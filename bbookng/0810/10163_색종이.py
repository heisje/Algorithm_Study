import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
board = [[0] * 1001 for _ in range(1001)]

xs = []
for i in range(n):
    x1, y1, x2, y2 = map(int,input().split())
    xs.append((x1, x2))
    for x in range(x1, x1 + x2):
        for y in range(y1, y1 + y2):
            board[x][y] = i+1


for i in range(n):
    result = 0
    x1, x2 = xs[i]
    for j in range(x1, x1+x2+1):
        result += board[j].count(i+1)

    print(result)


