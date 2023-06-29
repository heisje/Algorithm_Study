N, d, k, c = map(int, input().split())

sushi_go_round = []
for _ in range(N):
    sushi_go_round.append(int(input()))

for i in range(k - 1):
    sushi_go_round.append(sushi_go_round[i])

max_yum = set()
for i in range(N + k - 2):
    yum = set(sushi_go_round[i:i + k])
    if c not in yum:
        yum.add(c)
    if len(max_yum) < len(yum):
        max_yum = yum

print(len(max_yum))
