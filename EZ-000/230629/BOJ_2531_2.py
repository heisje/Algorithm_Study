N, d, k, c = map(int, input().split())

sushi_go_round = []
for _ in range(N):
    sushi_go_round.append(int(input()))

count = 0
yum_sushi = [0] * (d + 1)
for sushi in sushi_go_round[:k]:
    if not yum_sushi[sushi]:
        count += 1
    yum_sushi[sushi] += 1

max_count = count

for i in range(k, N + k - 1):
    if N - 1 < i:
        i = i % N
    pre_sushi = sushi_go_round[i - k]
    now_sushi = sushi_go_round[i]

    if not yum_sushi[now_sushi]:
        count += 1
    yum_sushi[now_sushi] += 1

    yum_sushi[pre_sushi] -= 1
    if not yum_sushi[pre_sushi]:
        count -= 1

    if not yum_sushi[c]:
        count += 1

    if max_count < count:
        max_count = count

    if not yum_sushi[c]:
        count -= 1

print(max_count)
