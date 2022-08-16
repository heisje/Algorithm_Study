import sys
input = sys.stdin.readline

C, R = map(int,input().split())
N = int(input())
cnt = 0

# C*R이 N보다 크다면 배정할 수 없으므로
if N > C*R:
    print(0)
else:
    # 달팽이 껍데기 벗기기
    while N > 2 * (C + R - 2):      # N의 위치가 있는 곳까지 안으로 들어가기
        cnt += 1                    # 좌표 count를 위한 변수
        N -= 2 * (C + R - 2)        # 껍데기 벗기고 껍데기 숫자만큼 N에서 빼주기
        C -= 2                      # 가로와 세로 길이가 2씩 줄어듬
        R -= 2

    # N이 껍데기에 있는 순간 !!
    if N < R:                                       # N보다 R이 크면 N은 왼쪽 세로줄에 있다.
        print(1 + cnt, N + cnt)
    elif N < R+C:                                   # N이 R 보다는 크고 C 보다 작으면 껍데기 윗줄
        print(1 + cnt - R + N, cnt + R)
    elif N < 2 * R + C - 1:                         # N이 껍데기의 오른쪽 변에 있는 경우
        print(cnt + C, cnt + R - 1 - (N-R-C))
    else:                                           # N이 껍데기의 아랫변에 있는 경우
        print(cnt + C - 2 - (N-2*R-C), cnt + 1)
