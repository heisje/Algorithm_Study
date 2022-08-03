import sys

input = lambda: sys.stdin.readline().strip()

board = [[0] * 100 for _ in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int,input().split())
    for x in range(x1, x2):                     # 직사각형의 가로길이만큼
        for y in range(y1, y2):                 # 직사각형의 세로길이만큼
            board[x][y] = 1                     # 해당 좌표들을 색칠 (1로 변경)

result = 0

for i in range(len(board)):
    result += sum(board[i])

print(result)

