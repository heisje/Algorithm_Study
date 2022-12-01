import sys
input = lambda :sys.stdin.readline().strip()

def move(wheel, x):
    a, b, c, d, e, f, g, h = wheel
    if x == 1:
        return [h, a, b, c, d, e, f, g]
    else:
        return [b, c, d, e, f, g, h, a]

wheels = [list(map(int, input())) for _ in range(4)]

K = int(input())

for _ in range(K):
    idx, d = map(int, input().split())

    idx -= 1
    left, right = idx - 1, idx + 1

    arr = []
    now = idx
    tmp = d

    while left >= 0:
        if wheels[left][2] == wheels[now][6]:
            break
        else:
            arr.append((left, -tmp))
            now, left, tmp = left, left-1, -tmp

    now = idx
    tmp = d

    while right < 4:
        if wheels[now][2] == wheels[right][6]:
            break
        else:
            arr.append((right, -tmp))
            now, right, tmp = right, right+1, -tmp

    for f in arr:
        a, b = f
        wheels[a] = move(wheels[a], b)

    wheels[idx] = move(wheels[idx], d)

result = 0

for i in range(4):
    if wheels[i][0] == 1:
        result += 2 ** i

print(result)