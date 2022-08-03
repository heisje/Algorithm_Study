n = int(input())

m = []
for i in range(101):
    b = []
    for j in range(101):
        b.append(0)
    m.append(b)

count = 0
for _ in range(n):
    x, y = map(int, input().split())
    for j in range(y, y+10):
        for i in range(x, x+10):
            m[j][i] = 1
for k in m:
    count += sum(k)
print(count)
