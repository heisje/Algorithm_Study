N, M = map(int, input().split())

area = []
for _ in range(N):
    area.append(list(map(int, input().split())))

for i in range(N):
    # 첫 번째 행은 오른쪽으로만 진행 가능
    if i == 0:
        for j in range(1, M):
            area[0][j] += area[0][j - 1]
    else:
        left = [0] * M    # 왼쪽 dp 테이블
        right = [0] * M   # 오른쪽 dp 테이블

        left[0] = area[i][0] + area[i - 1][0]
        right[M - 1] = area[i][M - 1] + area[i - 1][M - 1]

        for j in range(1, M):
            # 진행 방향과 한 행 위의 값 중 큰 값을 더함
            left[j] = area[i][j] + max(area[i - 1][j], left[j - 1])
            right[M - j - 1] = area[i][M - j - 1] + max(area[i - 1][M - j - 1], right[M - j])

        for j in range(M):
            area[i][j] = max(left[j], right[j])    # 왼쪽과 오른쪽 중 큰 값으로 갱신

print(area[N - 1][M - 1])
