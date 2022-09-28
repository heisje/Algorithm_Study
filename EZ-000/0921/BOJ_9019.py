import sys
input = sys.stdin.readline


N, M = map(int, input().split())
board = []
for _ in range(N):
    board += [list(map(int, input().split()))]

s = 0

# 1. 선형 테트로미노
for i in range(N):
    for j in range(M - 3):
        temp = board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i][j + 3]
        if s < temp:
            s = temp
        temp = 0

for i in range(N - 3):
    for j in range(M):
        temp = board[i][j] + board[i + 1][j] + board[i + 2][j] + board[i + 3][j]
        if s < temp:
            s = temp
        temp = 0

# 2. 정방 테트로미노
for i in range(N - 1):
    for j in range(M - 1):
        temp = board[i][j] + board[i][j + 1] + board[i + 1][j] + board[i + 1][j + 1]
        if s < temp:
            s = temp
        temp = 0

# 3. ㄱㄴ 테트로미노
for i in range(N - 2):
    for j in range(M - 1):
        temp1 = board[i][j] + board[i + 1][j] + board[i + 2][j] + board[i + 2][j + 1]
        temp2 = board[i][j] + board[i + 1][j] + board[i + 2][j] + board[i][j + 1]
        temp3 = board[i][j] + board[i][j + 1] + board[i + 1][j + 1] + board[i + 2][j + 1]
        if s < temp1:
            s = temp1
        if s < temp2:
            s = temp2
        if s < temp3:
            s = temp3
        temp1 = 0
        temp2 = 0
        temp3 = 0

for i in range(N - 2):
    for j in range(1, M):
        temp = board[i][j] + board[i + 1][j] + board[i + 2][j] + board[i + 2][j - 1]
        if s < temp:
            s = temp
        temp = 0

# 4. Z 테트로미노
for i in range(N - 2):
    for j in range(M - 1):
        temp = board[i][j] + board[i + 1][j] + board[i + 1][j + 1] + board[i + 2][j + 1]
        if s < temp:
            s = temp
        temp = 0

for i in range(N - 2):
    for j in range(1, M):
        temp = board[i][j] + board[i + 1][j] + board[i + 1][j - 1] + board[i + 2][j - 1]
        if s < temp:
            s = temp
        temp = 0

for i in range(N - 1):
    for j in range(1, M - 1):
        temp = board[i][j] + board[i][j + 1] + board[i + 1][j - 1] + board[i + 1][j]
        if s < temp:
            s = temp
        temp = 0

for i in range(N - 1):
    for j in range(M - 2):
        temp = board[i][j] + board[i][j + 1] + board[i + 1][j + 1] + board[i + 1][j + 2]
        if s < temp:
            s = temp
        temp = 0

# 5. ㅗ 테트로미노 ㅗ
for i in range(1, N - 1):
    for j in range(1, M - 1):
        temp = board[i][j] + board[i - 1][j - 1] + board[i + 1][j] + board[i + 1][j + 1]
        if s < temp:
            s = temp
        temp = 0

for i in range(N - 2):
    for j in range(M - 1):
        temp = board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i + 1][j + 1]
        if s < temp:
            s = temp
        temp = 0

for i in range(N - 2):
    for j in range(M - 1):
        temp = board[i][j] + board[i + 1][j] + board[i + 1][j + 1] + board[i + 2][j]
        if s < temp:
            s = temp
        temp = 0

for i in range(1, N - 2):
    for j in range(1, M):
        temp = board[i][j] + board[i - 1][j - 1] + board[i + 1][j] + board[i + 2][j]
        if s < temp:
            s = temp
        temp = 0

print(s)
