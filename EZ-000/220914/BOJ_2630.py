import sys
input = lambda: sys.stdin.readline().rstrip()


def papercut(r, c, n):
    global zero, one
    up_left = paper[r][c]
    for i in range(r, r + n):
        for j in range(c, c + n):
            if paper[i][j] != up_left:
                for k in range(2):
                    for l in range(2):
                        papercut(r + k * n // 2, c + l * n // 2, n // 2)
                return

    if up_left == 0:
        zero += 1
    else:
        one += 1
    return


N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))
zero, one = 0, 0

papercut(0, 0, N)
print(zero)
print(one)
