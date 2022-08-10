#실패
import sys

#최대 1001칸까지므로 0~1000 까지 만듬
N = int(input())
li = [[None for _ in range(1001)] for _ in range(1001)]
counter = [0 for _ in range(N)] #0을 N만큼 제작

for i in range(N):
    x1, y1, w, h = map(int, sys.stdin.readline().split())
    for y in range(y1, y1 + h):
        for x in range(x1, x1 + w):
            target = li[y][x]
            if target != i:
                if target != None:
                    counter[target] -= 1
                counter[i] += 1
                li[y][x] = i 
    
for num in counter:
    print(num)

if sum(counter) == 0:
    print(0)
