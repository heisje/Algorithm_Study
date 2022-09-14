# 실버1 / 76ms
import sys

input = lambda: sys.stdin.readline().strip()

N = int(input())
lst = [list(map(int, input())) for _ in range(N)]


def fn(x, y, N):
    if N == 1:  # 한칸짜리면 바로 출력
        print(lst[x][y], end='')
        return

    flag = False
    for i in range(N):
        for j in range(N):
            if lst[x + i][y + j] != lst[x][y]:  # 구간을 나눠야 한다면
                flag = True  # 바로 break
                break
        if flag:
            break
    else:  # 구간을 나누지 않아도 되면(=다 똑같다면)
        print(lst[x][y], end='')  # print
        return
    print('(', end='')  # 구간 나누기 전에 '(' 출력
    for i in range(0, N, N // 2):  # 구간 나눠서 함수 또 진행
        for j in range(0, N, N // 2):
            fn(x + i, y + j, N // 2)
    print(')', end='')  # 구간 나누고 나서 각 숫자 출력 후 ')' 출력


fn(0, 0, N)