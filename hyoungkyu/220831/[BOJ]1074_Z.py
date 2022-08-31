# 72ms / 실버1
import sys
input = lambda : sys.stdin.readline().strip()

def f(N, ni1, nj1):
    global cnt
    if N == 1:                                      # Z로 수를 늘릴 수 있다면 (=영역을 나눌 필요가 없다면)
        cnt -= 1
        for i in range(2):                          # Z 순서대로 카운트 증가
            for j in range(2):
                cnt += 1
                if ni1+i == r and nj1+j == c:       # 목표위치 도달 시 cnt값 반환
                    return cnt
    else:                                           # 영역을 나눠야 한다면
        ni1, ni2 = ni1, ni1 + (2**N) - (2**(N-1))   # 영역의 중앙을 기준으로 나눔
        nj1, nj2 = nj1, nj1 + (2**N) - (2**(N-1))
        N -= 1                                      # 영역 축소
        if r < ni1 + 2**N and c < nj1 + 2**N:       # 원래 영역의 2사분면일 경우
            f(N, ni1, nj1)
        elif r < ni1 + 2**N and c >= nj1 + 2**N:    # 원래 영역의 1사분면일 경우
            cnt += ((2**N)**2)
            f(N, ni1, nj2)
        elif r >= ni1 + 2**N and c < nj1 + 2**N:    # 원래 영역의 3사분면일 경우
            cnt += ((2**N)**2) * 2
            f(N, ni2, nj1)
        elif r >= ni1 + 2**N and c >= nj1 + 2**N:   # 원래 영역의 4사분면일 경우
            cnt += ((2**N)**2) * 3
            f(N, ni2, nj2)

N, r, c = map(int, input().split())
cnt = 0
f(N, 0, 0)
print(cnt)