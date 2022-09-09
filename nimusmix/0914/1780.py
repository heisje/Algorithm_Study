from itertools import product
import sys
input = lambda: sys.stdin.readline().strip()

def sol(x, y, maxn):
    global minus, zero, plus
    if maxn == 3:
        for k in li:
            if paper[x+k[0]][y+k[1]] == -1: minus += 1
            elif paper[x+k[0]][y+k[1]] == 0: zero += 1
            elif paper[x+k[0]][y+k[1]] == 1: plus +=1
    else:
        for i in range(x, maxn, maxn//3):
            for j in range(y, maxn, maxn//3):
                prev = paper[i][j]
                cnt = Ecnt = 0
                for k in li:
                    if cnt == Ecnt and paper[i+k[0]][j+k[1]] == prev:
                        cnt += 1
                    Ecnt += 1
                if cnt == 9:
                    if prev == -1: minus += 1
                    elif prev == 0: zero += 1
                    elif prev == 1: plus += 1
                else:
                    if maxn//3 >= 3: sol(i, j, maxn//3)

N = int(input())
paper = [tuple(map(int, input().split())) for _ in range(N)]
paperset = []

for l in range(len(set(paper))):
    if list(set(paper))[0][l] not in paperset:
        paperset.append(list(set(paper))[0][l])

minus = zero = plus = 0
li = list(product([0,1,2], repeat=2))

sol(0, 0, N)
print(minus)
print(zero)
print(plus)

print(paperset)
print(list(set(paper)))