# 108ms
import heapq

# 다익스트라 문제
def resolve(SIZE, li):
    hq = []
    dp = [[float('inf') for _ in range(SIZE)] for _ in range(SIZE)]
    heapq.heappush(hq, (li[0][0], 0, 0))
    while hq:
        value, r, c = heapq.heappop(hq)
        if r == SIZE - 1 and c == SIZE - 1:
            return value
        for dr, dc in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            gr = r + dr
            gc = c + dc
            if 0 <= gr < SIZE and 0 <= gc < SIZE:
                newValue = value + li[gc][gr]
                if newValue < dp[gr][gc]:
                    dp[gr][gc] = newValue
                    heapq.heappush(hq, (newValue, gr, gc)) 

def main(N):
    SIZE = int(input())
    li = []
    if SIZE == 0:
        return False
    
    # 지도입력 받음
    for _ in range(SIZE):
        li.append(list(map(int, input().split())))
    
    # 문제풀이
    answer = resolve(SIZE, li)
    print(f'Problem {N}: {answer}')
    return True

N = 1
while main(N):
    N += 1
