from math import lcm
import sys
input = lambda: sys.stdin.readline().strip()
print = sys.stdout.write

T = int(input())
for tc in range(T):
    M, N, x, y = map(int, input().split())
    LCM = lcm(M, N)

    for ans in range(x, LCM+1, M):
        if (ans-x) % M == 0 and (ans-y) % N == 0:
            print(ans)
            break
    else: print(-1)