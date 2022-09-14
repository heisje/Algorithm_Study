# 실버2 / 4140ms
import sys
input = lambda:sys.stdin.readline().strip()

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

a = b = c = 0                   # a : -1의 개수, b : 0의 개수, c : 1의 개수
def fn(x, y, N):                # 배열의 시작 좌표, N : 부분배열의 크기
    global a
    global b
    global c
    if N == 1:                  # N이 1이면 각각의 요소가 배열이 되므로 다 더해줌
        if lst[x][y] == -1:
            a += 1
            return
        elif lst[x][y] == 0:
            b += 1
            return
        else:
            c += 1
            return

    flag = False
    for i in range(N):          # 순차적으로 돌면서 다르면 break
        for j in range(N):
            tmp = lst[x + i][y + j]
            if y + j > y and lst[x + i][y + j] != lst[x + i][y + j - 1]:
                flag = True
                break
            elif x + i > x and lst[x + i][y + j] != lst[x + i - 1][y + j]:
                flag = True
                break
        if flag:
            break
    else:                       # 순차적으로 다 돌면 다 같은 숫자이므로 그 숫자 카운트를 올림
        if tmp == -1:
            a += 1
            return
        elif tmp == 0:
            b += 1
            return
        else:
            c += 1
            return

    if flag:                    # 배열 안의 숫자가 다르다면
        for i in range(0, N, N//3):     # 9개로 쪼개서 재귀 ㄱㄱ
            for j in range(0, N, N//3):
                fn(x+i, y+j, N//3)
fn(0, 0, N)
print(a)
print(b)
print(c)