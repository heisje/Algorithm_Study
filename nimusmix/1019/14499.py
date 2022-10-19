import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

def roll_dice(n):
    if n == 1:
        dice_info['T'], dice_info['B'], dice_info['E'], dice_info['W'] = dice_info['W'], dice_info['E'], dice_info['T'], dice_info['B']
    elif n == 2:
        dice_info['T'], dice_info['B'], dice_info['E'], dice_info['W'] = dice_info['E'], dice_info['W'], dice_info['B'], dice_info['T']        
    elif n == 3:
        dice_info['T'], dice_info['B'], dice_info['N'], dice_info['S'] = dice_info['S'], dice_info['N'], dice_info['T'], dice_info['B']
    elif n == 4:
        dice_info['T'], dice_info['B'], dice_info['N'], dice_info['S'] = dice_info['N'], dice_info['S'], dice_info['B'], dice_info['T']

N, M, x, y, K = map(int, input().split())
the_map = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

dice = [0] * 7
dice_info = {
    'T': 1,
    'B': 6,
    'N': 2,
    'S': 5,
    'E': 3,
    'W': 4}
direction = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}

pointer = deque()
pointer.append((y, x))

for c in commands:
    i, j = pointer[-1]
    di, dj = direction[c]
    ni, nj = i + di, j + dj
    
    if 0 <= ni < N and 0 <= nj < N:
        roll_dice(c)
        
        pointer.append((ni, nj))
        print(dice[dice_info['T']])
        
        if the_map[ni][nj] == 0:
            the_map[ni][nj] = dice[dice_info['B']]
        else:
            dice[dice_info['B']] = the_map[ni][nj]
            the_map[ni][nj] = 0