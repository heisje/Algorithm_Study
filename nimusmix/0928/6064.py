from math import lcm
import sys
input = lambda: sys.stdin.readline().strip()

T = int(input())
for tc in range(T):
    M, N, x, y = map(int, input().split())
    LCM = lcm(M, N)

    for ans in range(x, LCM+1, M):
        if (ans-y) % N == 0:
            print(ans)
            break
    else: print(-1)