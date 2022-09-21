import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())
M = int(input())
S = input()

cnt = 1
idx = ans = 0

while idx < M-2:
    if S[idx:idx+3] == "IOI":
        cnt += 2
        idx += 2
        if cnt == 1+N*2:
            cnt -= 2
            ans += 1
    else:
        cnt = 1
        idx += 1

print(ans)