import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
tt = 1

board = [[0]*1001 for _ in range(1001)]

for x in range(1, n+1):
    a, b, c, d = map(int, input().split())
    for j in range(a, a+c):
        board[j][b:b+d] = [x]*d
    tt += 1
    
for nn in range(1, n+1):
    digit = 0
    for mm in board:
       digit += mm.count(nn)
    print(digit)