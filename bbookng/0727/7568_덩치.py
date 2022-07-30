import sys

n = int(input())

arr = []

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))


for w1, h1 in arr:                  # arr을 2중으로 돌며 weight, height 비교
    rank = 1
    for w2, h2 in arr:
        if w1 < w2 and h1 < h2:     # weight와 height가 둘 다 작으면 rank + 1
            rank += 1
    print(rank, end=" ")





