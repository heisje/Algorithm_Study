import sys
input = lambda : sys.stdin.readline().strip()

W, H = map(int,input().split())
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
s, l = map(int,input().split())

total = 0
for ms, ml in arr:
    if ms == s:                                             # 같은 방향에 있을 경우
        total += abs(l-ml)

    elif s+ms == 3:                                         # 각각 남, 북 위치일 때
        total += min(l + ml, 2 * W - l - ml) + H

    elif s+ms == 7:                                         # 동, 서 위치일 때
        total += min(l + ml, 2 * H - l - ml) + W

    elif s+ms == 4:                                         # 북, 서 일 때
        total += l + ml

    elif s+ms == 6:                                         # 남, 동 일 때
        total += (W-l)+(H-ml) if s == 2 else (W-ml) + (H-l)


    else:                                                   # 남, 서 혹은 동, 북 일 때
        if s == 1:                                          # 경비원이 북쪽에 있을 때
            total += (W-l) + ml
        elif s == 2:                                        # 경비원이 남쪽에 있을 때
            total += l + (H-ml)
        elif s == 3:                                        # 경비원이 서쪽에 있을 때
            total += (H-l) + ml
        else:                                               # 경비원이 동쪽에 있을 때
            total += l + (W-ml)

print(total)

