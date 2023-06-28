N, M = map(int, input().split())

area = []
for _ in range(N):
    area.append(list(map(int, input().split())))

for i in range(1, M):
    area[0][i] += area[0][i - 1]

for i in range(1, N):
    left = [0] * M
    right = [0] * M
    for j in range(M):
        if j == 0:
            left[j] = area[i][j] + area[i - 1][j]
            right[M - 1] = area[i][M - 1] + area[i - 1][M - 1]
        else:
            left[j] = area[i][j] + max(area[i - 1][j], left[j - 1])
            right[M - j - 1] = area[i][M - j - 1] + max(area[i - 1][M - j - 1], right[M - j])
    for j in range(M):
        area[i][j] = max(left[j], right[j])

print(area[N - 1][M - 1])
