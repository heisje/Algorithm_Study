import sys
input = lambda: sys.stdin.readline().strip()





''' 틀렸습니다
def area(arr):
    colors = {'R': 0, 'G': 0, 'B': 0}
    temp = []
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            temp += [j]
            if arr[i][j] != arr[i][j + 1]:
                colors[arr[i][j]] += 1
                if i != 0:
                    for k in temp:
                        now = arr[i][k]
                        idx = k
                        if now == arr[i - 1][k]:
                            colors[now] -= 1
                            for l in range(idx + 1, temp[-1] + 1):
                                if now == arr[i - 1][l] and now != arr[i - 1][l - 1] and now != arr[i - 1][l + 1]:
                                    colors[now] -= 1
                            break
                temp = []

    return sum(colors.values())


N = int(input())
color3 = ['N' * (N + 2)]
color2 = [''] * (N + 2)

for _ in range(N):
    color3 += ['N' + input() + 'N']
color3 += ['N' * (N + 2)]

for i1 in range(N + 2):
    for i2 in range(N + 2):
        if color3[i1][i2] == 'G':
            color2[i1] += 'R'
        else:
            color2[i1] += color3[i1][i2]

print(area(color3), area(color2))
'''
