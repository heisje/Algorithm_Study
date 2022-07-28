#https://www.acmicpc.net/problem/2563

#방법 1. 2차원 리스트에 1과 0을 채워서 1의 값을 구한다.
#방법 2. 도화지의 x,y값을 기준으로 겹치는 구간을 구해서 빼준다.

def list_on(li, x, y):
    count = 0
    for yy in range(y, y + 10):
        for xx in range(x, x + 10):
            if li[yy][xx] == 0:
                count += 1
            li[yy][xx] = 1
    return count

N = int(input())
li = [[0 for _ in range(101)] for _ in range(101)]
print(li)
count = 0
for _ in range(N):
    x, y = map(int, input().split())
    count += list_on(li, x, y)
print(count)