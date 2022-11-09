import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
cleaned = []
for _ in range(N):
    cleaned.append(list(map(int, input().split())))
cleaned[r][c] = 'v'

# [북, 동, 남, 서] / 왼쪽 = (idx + 3) % 4
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
vacuumed = 1
cnt = 0
while True:
    d = (d + 3) % 4
    dr, dc = delta[d]
    nr, nc = r + dr, c + dc
    if not cleaned[nr][nc]:
        vacuumed += 1
        cleaned[nr][nc] = 'v'
        r, c = nr, nc
        cnt = 0
    else:
        cnt += 1
        if cnt == 4:
            back = (d + 2) % 4
            dr, dc = delta[back]
            nr, nc = r + dr, c + dc
            if cleaned[nr][nc] == 1:
                break
            else:
                r, c = nr, nc
                cnt = 0
print(vacuumed)
