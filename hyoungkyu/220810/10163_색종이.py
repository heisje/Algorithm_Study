import sys

input = lambda: sys.stdin.readline().strip()
N = int(input())

# 1001 x 1001 행렬 생성
m = []
for i in range(1001):
    b = []
    for j in range(1001):
        b.append(0)
    m.append(b)


for k in range(1, N+1):      # 겹치는 부분은 순서대로 덮어짐
    a, b, c, d = map(int, input().split())
    for j in range(a, a+c):  # 점 (a,b)에서 x축으로 c만큼을 k값으로 바꿈
        m[j][b:b+d] = [k]*d  # 점 (a,b)에서 y축으로 d만큼을 k값으로 바꿈
                             # 직사각형 형태 완성

for i in range(1,N+1):
    count = 0
    for k in m:              # m의 행마다
        count += k.count(i)  # 순서 i의 개수를 셈
    print(count)