import sys
input= lambda: sys.stdin.readline().strip()


col, row = map(int, input().split())

# 종이 행렬 board..?
r = [0, row]
c = [0, col]

for _ in range(int(input())):
    x = list(map(int, input().split()))
    if x[0] == 0:
        r.append(x[1])      # row 방향 자를 위치 추가
    else:
        c.append(x[1])      # col 방향 자를 위치 추가

# 마구잡이로 입력된거 정렬
r.sort()
c.sort()


_max = 0
for i in range(1, len(r)):
    for j in range(1, len(c)):
        if (r[i] - r[i-1]) * (c[j] - c[j-1]) > _max:    # 세로 x 가로 해서 넓이 구하기
            _max = (r[i] - r[i-1]) * (c[j] - c[j-1])

print(_max)



