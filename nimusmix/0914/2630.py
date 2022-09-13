from itertools import product
import sys
input = lambda: sys.stdin.readline().strip()

def recur(x, y, maxN):                                              # maxN = 최대 길이
    if maxN == 2:                                                   # 최대 길이가 2일 경우에는
        step = list(product(range(2), repeat=2))                    # 리스트 전체를 순회하면서
        for k in step:
            rst[paper[x+k[0]][y+k[1]]] += 1                         # 해당하는 숫자의 rst 인덱스에 +1
    else:                                                           # 최대 길이가 2가 아닐 경우에는
        step = list(product(range(maxN//2), repeat=2))
        for i in range(x, maxN+x, maxN//2):                         # 가로, 세로를 3등분 한 시작점 단위로 i, j 설정
            for j in range(y, maxN+y, maxN//2):
                cnt = 0
                prev = paper[i][j]                                  # 시작점의 값을 prev에 저장
                for k in step:                                      # 중복 순열을 활용하여 종이를 순회하며
                    if paper[i+k[0]][j+k[1]] != prev: break         # 데이터가 prev와 같지 않은 경우 break
                    else: cnt += 1                                  # 데이터가 prev와 같은 경우 cnt += 1
                if cnt == (maxN//2) ** 2:                           # 순회가 종료된 후 cnt가 최대 길이//2의 제곱과 같으면 해당하는 숫자의 rst 인덱스에 +1
                    rst[prev] += 1
                else:                                               # cnt가 최대 길이//2의 제곱과 다르면 사각형 내에 다른 숫자가 있다는 의미이므로
                    recur(i, j, maxN//2)                            # maxN//2 해서 재귀 함수 호출

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
rst = [0, 0]

recur(0, 0, N)
for i in rst:
    if 0 in rst:                                                    # rst에 0이 있으면 한 가지 숫자만 있다는 것이므로
        if i: print(1)                                              # 값이 있는 걸 1로 바꿔준 다음 출력
        else: print(0)
    else: print(i)