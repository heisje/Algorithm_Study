N, L = map(int, input().split())
matrix = []

cnt = 0

for i in range(N):
    line = list(map(int, input().split()))
    skip = 0
    skip2 = 0
    for j in range(len(line) - 1):

        if skip2:
            skip2 -= 1              # 오른쪽으로 내려가는 경사로 체크용
        if skip:
            skip -= 1
            continue

        before = line[j]
        next = line[j + 1]
        if before == next:
            continue
        elif before == next + 1:    # 왼쪽이 한층  더 높다
            if N - (j + 1) < L:     # 남은 공간 중 길이 부족
                break               # 길끊김
            else:
                for k in range(j + 1, j + L + 1):
                    if line[k] != next:
                        break       # 길끊김
                else:
                    skip = L - 1      # 다음 L칸 동안은 경사로이므로 체크 하지말자
                    skip2 = 2*L
                    continue
                break               # 길이 끊긴 경우므로 다른 라인으로 가자

        elif before + 1 == next:    # 오른쪽이 한층 더 높다
            if j - L + 1 < 0:       # 왼쪽에 공간이 부족할 경우
                break
            else:
                if skip2:
                    skip2 = 0
                    break
                for k in range(j, j - L, -1):
                    if line[k] != before:
                        break
                else:
                    continue
                break
        else:
            break                   # 두칸이상 차이나면 불가능
    else:
        cnt += 1

    matrix.append(line)


for j in range(N):
    skip = 0
    skip2 = 0
    for i in range(N - 1):

        if skip2:
            skip2 -= 1  # 아래로 내려가는 경사로 체크용
        if skip:
            skip -= 1
            continue
        before = matrix[i][j]
        next = matrix[i + 1][j]
        if before == next:
            continue
        elif before == next + 1:  # 위쪽이 한층  더 높다
            if N - (i + 1) < L:  # 남은 공간 중 길이 부족
                break  # 길끊김
            else:
                for k in range(i + 1, i + L + 1):
                    if matrix[k][j] != next:
                        break  # 길끊김
                else:
                    skip = L - 1 # 다음 L칸 동안은 경사로이므로 체크 하지말자
                    skip2 = 2 * L
                    continue
                break  # 길이 끊긴 경우므로 다른 라인으로 가자

        elif before + 1 == next:  # 오른쪽이 한층 더 높다
            if i - L + 1 < 0:  # 왼쪽에 공간이 부족할 경우
                break
            else:
                if skip2:
                    break
                for k in range(i, i - L, -1):
                    if matrix[k][j] != before:
                        break
                else:
                    continue
                break
        else:
            break  # 두칸이상 차이나면 불가능
    else:
        cnt += 1


print(cnt)