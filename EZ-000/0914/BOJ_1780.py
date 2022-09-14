import sys
input = lambda: sys.stdin.readline().rstrip()


def papercut(r, c, n):
    global minus, zero, one
    up_left = paper[r][c]
    for i in range(r, r + n):
        for j in range(c, c + n):
            if paper[i][j] != up_left:
                for k in range(3):
                    for l in range(3):
                        papercut(r + k * n // 3, c + l * n // 3, n // 3)
                return

    if up_left == -1:
        minus += 1
    elif up_left == 0:
        zero += 1
    else:
        one += 1
    return


N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))
minus, zero, one = 0, 0, 0

papercut(0, 0, N)
print(minus)
print(zero)
print(one)

""" 참고
https://dailymapins.tistory.com/m/270
"""
