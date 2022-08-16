import sys
input = sys.stdin.readline

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

p = (p+t) % (w*2)       # 개미가 x축 방향을 따라 왕복을 제외하고 이동한 거리
q = (q+t) % (h*2)       # 개미가 y축 방향을 따라 왕복을 제외하고 이동한 거리

if p > w:               # p가 w보다 크면 반대방향으로 가고 있을 때
    p = w*2 - p         # 왕복 길이에서 p값을 빼면 현재 개미의 위치
if q > h:
    q = h*2 - q

print(p, q)
