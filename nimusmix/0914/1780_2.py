from itertools import product
import sys
input = lambda: sys.stdin.readline().strip()

def recur(x, y, maxN):                                              # maxN = 최대 길이
    if maxN == 3:                                                   # 최대 길이가 3일 경우에는
        step = list(product(range(3), repeat=2))                    # 리스트 전체를 순회하면서
        for k in step:
            rst[paper[x+k[0]][y+k[1]]+1] += 1                       # 해당하는 숫자의 rst 인덱스에 +1
    else:                                                           # 최대 길이가 3이 아닐 경우에는
        step = list(product(range(maxN//3), repeat=2))
        for i in range(x, maxN+x, maxN//3):                         # 가로, 세로를 3등분 한 시작점 단위로 i, j 설정
            for j in range(y, maxN+y, maxN//3):
                cnt = 0
                prev = paper[i][j]                                  # 시작점의 값을 prev에 저장
                for k in step:                                      # 중복 순열을 활용하여 종이를 순회하며
                    if paper[i+k[0]][j+k[1]] != prev: break         # 데이터가 prev와 같지 않은 경우 break
                    else: cnt += 1                                  # 데이터가 prev와 같은 경우 cnt += 1
                if cnt == (maxN//3) ** 2:                           # 순회가 종료된 후 cnt가 최대 길이//3의 제곱과 같으면 해당하는 숫자의 rst 인덱스에 +1
                    rst[prev+1] += 1                                # ex) 최대 길이가 27일 경우 81일 때
                else:                                               # cnt가 최대 길이//3의 제곱과 다르면 사각형 내에 다른 숫자가 있다는 의미이므로
                    recur(i, j, maxN//3)                            # maxN//3 해서 재귀 함수 호출

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
rst = [0, 0, 0]

recur(0, 0, N)
for i in rst:
    if rst.count(0) == 2:                                           # rst에 0이 2개면 한 가지 숫자만 있다는 것이므로
        if i: print(1)                                              # 값이 있는 걸 1로 바꿔준 다음 출력
        else: print(0)
    else: print(i)