import sys
input = sys.stdin.readline

n = int(input())
ds = []
ls = []
max_h = 0
max_w = 0
for i in range(6):
    direction, length = map(int, input().split())
    ds.append(direction)
    ls.append(length)
    if direction == 1 or direction == 2:
        if max_w < length:
            max_w = length
    else:
        if max_h < length:
            max_h = length

in_sqr = []
in_h = 0
in_w = 0
idx = 0
while True:
    if idx > 2:
        temp_d = ds.pop(0)
        ds.append(temp_d)
        temp_l = ls.pop(0)
        ls.append(temp_l)
        idx = 2
    elif ds[idx] == ds[idx + 2] and ds[idx + 1] == ds[idx + 3]:
        in_h, in_w = ls[idx + 1], ls[idx + 2]
        break
    else:
        idx += 1

area = (max_h * max_w) - (in_h * in_w)
print(area * n)
