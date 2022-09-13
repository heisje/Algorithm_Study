from itertools import product
import sys
input = lambda: sys.stdin.readline().strip()

def recur(x, y, maxN):
    print('(', end='')
    if maxN == 2:
        step = list(product(range(2), repeat=2))
        for k in step:
            print(paper[x+k[0]][y+k[1]], end='')
    else:
        step = list(product(range(maxN//2), repeat=2))
        for i in range(x, maxN+x, maxN//2):
            for j in range(y, maxN+y, maxN//2):
                cnt = 0
                prev = paper[i][j]
                for k in step:
                    if paper[i+k[0]][j+k[1]] != prev: break
                    else: cnt += 1
                if cnt == (maxN//2) ** 2:
                    print(prev, end='')
                else:
                    recur(i, j, maxN//2)
    print(')', end='')

N = int(input())
paper = [list(map(int, input())) for _ in range(N)]
zero = one = 0

for i in range(N):
    for j in range(N):
        if paper[i][j] == 0: zero += 1
        elif paper[i][j] == 1: one += 1

if zero == N*N: print(0)
elif one == N*N: print(1)
else: recur(0, 0, N)