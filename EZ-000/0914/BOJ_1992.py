import sys
input = lambda: sys.stdin.readline().rstrip()


def quadtree(r, c, n):
    up_left = image[r][c]
    for i in range(r, r + n):
        for j in range(c, c + n):
            if image[i][j] != up_left:
                print('(', end='')
                quadtree(r, c, n // 2)
                quadtree(r, c + n // 2, n // 2)
                quadtree(r + n // 2, c, n // 2)
                quadtree(r + n // 2, c + n // 2, n // 2)
                print(')', end='')
                return
    print(up_left, end='')


N = int(input())
image = []
for _ in range(N):
    image.append(list(map(int, list(input()))))

quadtree(0, 0, N)

"""참고
https://honggom.tistory.com/134
"""
