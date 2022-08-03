m = []
for i in range(101):
    b = []
    for j in range(101):
        b.append(0)
    m.append(b)

count = 0
for _ in range(4):
    a, b, c, d = map(int, input().split())
    for j in range(a, c):
        for i in range(b, d):
            m[j][i] = 1
for k in m:
    count += sum(k)
print(count)
