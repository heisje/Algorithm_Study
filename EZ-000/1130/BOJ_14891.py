import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()


def gear_with(gn, gd, gs):
    direction = [0, 0, 0, 0]
    direction[gn - 1] = gd
    for minus in range(0, 3):
        now = direction[gn - 1 - minus]
        if now == 1:
            direction[gn - 2 - minus] = -1
        else:
            direction[gn - 2 - minus] = 1

    flag = [0, 0, 0, 0]
    flag[gn - 1] = 1
    # 왼쪽 탐색
    idx = gn - 1
    while True:
        idx -= 1
        if idx < 0:
            break
        if flag[idx + 1] and gears[idx + 1][2] != gears[idx + 2][6]:
            flag[idx] = 1
    # 오른쪽 탐색
    idx = gn - 1
    while True:
        idx += 1
        if 3 < idx:
            break
        if flag[idx - 1] and gears[idx][2] != gears[idx + 1][6]:
            flag[idx] = 1

    for idx in range(4):
        if flag[idx]:
            if direction[idx] == 1:
                temp = gears[idx + 1].pop()
                gears[idx + 1].appendleft(temp)
            else:
                temp = gears[idx + 1].popleft()
                gears[idx + 1].append(temp)


def scoring(gs):
    score = 0
    if gs[1][0]:
        score += 1
    if gs[2][0]:
        score += 2
    if gs[3][0]:
        score += 4
    if gs[4][0]:
        score += 8
    print(score)


gears = {}
for n in range(1, 5):
    gears[n] = deque(list(map(int, input())))

K = int(input())
for _ in range(K):
    N, D = map(int, input().split())
    gear_with(N, D, gears)

scoring(gears)
