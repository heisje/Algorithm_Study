import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
methods = {1: ([0], [1], [2], [3]), 2: ([0, 3], [1, 2]), 3: ([2, 0], [1, 0], [1, 3], [3, 2] ), 4: ([0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]), 5: ([], [0, 1, 2, 3])}

sensors = []
for i in range(N):
    for j in range(M):
        if 0 < arr[i][j] < 6:
            sensors.append((i, j, arr[i][j]))

_min = float('inf')

def solution(array, cnt):
    global _min

    if cnt == len(sensors):
        _min = min(_min, sum([line.count(0) for line in array]))
        return

    for i in methods[sensors[cnt][2]]:
        tmp = [j[:] for j in array]

        for j in i:
            nx, ny = sensors[cnt][0], sensors[cnt][1]

            while True:
                nx, ny = nx + directions[j][0], ny + directions[j][1]
                if not 0 <= nx < N or not 0 <= ny < M:
                    break
                if tmp[nx][ny] == 6:
                    break
                if not tmp[nx][ny]:
                    tmp[nx][ny] = -1

        solution(tmp, cnt+1)

solution(arr, 0)
print(_min)


