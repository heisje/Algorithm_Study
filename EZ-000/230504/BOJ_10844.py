N = int(input())

now = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]

for _ in range(1, N):
    temp = now[:]

    for n in range(1, 11):
        temp[n] = now[n - 1] + now[n + 1]
    now = temp

answer = sum(now)
print(answer % 1000000000)
