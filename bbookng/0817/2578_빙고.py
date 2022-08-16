import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for i in range(5)]
numbers = []
check = [[0]*5 for _ in range(5)]
for i in range(5):
    numbers.extend(map(int, input().split()))

for idx in range(len(numbers)):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == numbers[idx]:
                check[i][j] = 1

                tmp = 0
                # 가로줄 확인
                for l in check:
                    if sum(l) == 5:
                        tmp += 1

                # 세로줄 확인
                for j in range(5):
                    t = 0
                    for i in range(5):
                        if check[i][j]:
                            t += 1
                    if t == 5:
                        tmp += 1

                # 대각선 확인
                t = 0
                for i in range(5):
                    if check[i][i]:
                        t += 1
                    if t == 5:
                        tmp += 1
                t = 0
                for i in range(5):
                    if check[i][4 - i]:
                        t += 1
                    if t == 5:
                        tmp += 1
                if tmp >= 3:
                    print(idx + 1)
                    exit()

                break

