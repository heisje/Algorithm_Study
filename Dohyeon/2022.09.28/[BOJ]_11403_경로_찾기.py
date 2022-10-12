N = int(input())

matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):

            if matrix[i][k] and matrix[k][j]:
                matrix[i][j] = 1

for i in range(N):
    print(*matrix[i])

