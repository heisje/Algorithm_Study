import sys
from itertools import combinations

heights = []
for n in range(9):
    height = int(sys.stdin.readline())
    heights.append(height)
heights.sort()

combi = list(combinations(heights, 7))

for c in combi:
    if sum(c) == 100:
        for n in c:
            print(n)
        break

'''
mini_log
1. 처음에 for문에 break를 안 넣어서 틀렸다.
합이 100이 되는 조합 한 가지만 출력하는 거니까
break를 꼭 넣어야한다!
2. 파이썬이 아니었다면 combination
모듈이 없어서 못 풀었을 것 같다.
조합이나 순열 자체를 구현해봐야지.
'''
