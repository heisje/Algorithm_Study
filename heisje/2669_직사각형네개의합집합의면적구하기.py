# 100x100의 None값인 리스트 생성
# 포인트 두개를 입력받으면, None이라면 리스트안의 사각형 범위를 1로 변경 시키고 카운트를 증가시킴

li = [[None for _ in range(100)] for _ in range(100)]
counter = 0

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            if li[y][x] == None:
                counter += 1
                li[y][x] = 1

print(counter)

