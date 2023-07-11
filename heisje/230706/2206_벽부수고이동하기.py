# 4900ms

import heapq
import sys
MAXSIZE = sys.maxsize

def main():
    hq = []
    heapq.heappush(hq, (1, 0, 0, 0))
    dp = [[MAXSIZE for _ in range(M)] for _ in range(N)]
    breakWallDp = [[MAXSIZE for _ in range(M)] for _ in range(N)]
    while hq:
        depth, wall, n, m = heapq.heappop(hq)
        if n == N - 1 and m == M - 1:
            print(depth)
            return
        for gn, gm in ((n+1, m), (n-1, m), (n, m+1), (n, m-1)):
            if 0 <= gn < N and 0 <= gm < M:
                if wall == 0:
                    if li[gn][gm] == 1:
                        if breakWallDp[gn][gm] > depth + 1:
                            breakWallDp[gn][gm] = depth + 1
                            heapq.heappush(hq, (depth + 1, 1, gn, gm))
                    elif li[gn][gm] == 0:
                        if dp[gn][gm] > depth + 1:
                            dp[gn][gm] = depth + 1
                            heapq.heappush(hq, (depth + 1, 0, gn, gm))
                elif wall == 1 and li[gn][gm] == 0:
                    if breakWallDp[gn][gm] > depth + 1:
                        breakWallDp[gn][gm] = depth + 1
                        heapq.heappush(hq, (depth + 1, 1, gn, gm))
    print(-1)
N, M = map(int, input().split())
li = [list(map(int, input())) for _ in range(N)]
main()