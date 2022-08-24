import sys

N = int(sys.stdin.readline())
pillars = []
maxH = 0
maxHL = 0
maxL = 0

for _ in range(N):
    L, H = map(int, sys.stdin.readline().split())
    pillars.append([L, H])
    if H > maxH:
        maxH = H
        maxHL = L
    if L > maxL:
        maxL = L

pList = [0] * (maxL + 1)

for left, height in pillars:
    pList[left] = height

area = 0
tempH = 0
for idx in range(maxHL + 1):
    if pList[idx] > tempH:
        tempH = pList[idx]
    area += tempH
tempH = 0
for idx in range(maxL, maxHL, -1):
    if pList[idx] > tempH:
        tempH = pList[idx]
    area += tempH

print(area)
