import sys

N = int(input())
li = [[None for _ in range(1001)] for _ in range(1001)]
counter = [0 for _ in range(N)]

for i in range(N):
    x1, y1, w, h = map(int, sys.stdin.readline().split())
    x2 = x1 + w
    y2 = y1 + h
    for y in range(y1, y2):
        for x in range(x1, x2):
            target = li[y][x]
            if target != i:
                if target != None:
                    counter[target] -= 1
                counter[i] += 1
                li[y][x] = i 
for num in counter:
    print(num)

if sum(counter) == 0:
    print(0)
