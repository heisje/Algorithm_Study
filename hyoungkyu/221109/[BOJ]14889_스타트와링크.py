# 실버2 / 3276ms
import sys
input = lambda:sys.stdin.readline().strip()

def f(cnt, k):
    global minV
    if cnt == N//2:                     # 반반 됐으면 시너지 구해서 minV와 비교
        s, l = 0, 0
        for y in range(N):
            for x in range(y+1, N):     # 대각선 대칭이므로 위쪽 인덱스만 구하면 됨
                if x == y: continue
                if check[y] and check[x]:           # 스타트팀 시너지 
                    s += S[y][x] + S[x][y]
                elif not check[y] and not check[x]: # 링크팀 시너지
                    l += S[y][x] + S[x][y]
        if abs(s-l) < minV:
            # print(f's : {s} / l : {l} / 이전 minV = {minV}')
            minV = abs(s-l)
        return

    for i in range(k, N-1):             # 한개씩 체크하면서 재귀
        if not check[i]:
            check[i] = 1
            f(cnt+1, i)
            if minV == 0:
                return
            check[i] = 0

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
minV = 100*(N//2)
check = [0] * N
f(0, 0)
print(minV)
