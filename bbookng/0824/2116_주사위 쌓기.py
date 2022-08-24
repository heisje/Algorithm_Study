import sys
input = lambda : sys.stdin.readline().strip()

opp = [5, 3, 4, 1, 2, 0]    # 주사위 반대편 list 만들기

N = int(input())
cube = [list(map(int, input().split())) for _ in range(N)]

result = 0
for bottom in range(6):
    total = 0                                   # max 옆면 값 구하기
    now = bottom                                # 기준이 되는 바닥 숫자
    for i in range(N):                          # 주사위 갯수만큼 반복
        tmp = []                                # 바닥인 숫자를 담을 list
        tmp.append(cube[i][now])                # 바닥
        tmp.append(cube[i][opp[now]])           # 반대편은 위로 가겠죠 (옆면은 아니라는 뜻)
        if 6 not in tmp:                        # 6이 아래, 윗면 둘 다 아니면
            total += 6                          # 6 추가
        elif 5 not in tmp:                      # 4까지 마찬가지. 왜냐면 6,5가 아래, 윗 면이라도 최댓값은 무조건 4이상
            total += 5
        else:
            total += 4
        # tmp = [1, 2, 3, 4, 5, 6]
        # tmp.remove(cube[i][now])
        # tmp.remove(cube[i][opp[now]])
        # subtotal += max(tmp)

        if i == N-1:                            # N개까지 다 했다면 멈추자
            break
        now = cube[i+1].index(cube[i][opp[now]])# 아래 주사위의 윗면, 위 주사위의 아랫면이 같아야 하니까 그 숫자찾아서 index 설정

    result = max(result, total)                 # 첫번째 주사위 바닥을 기준으로 1-6까지 돌면서 max값 갱신

print(result)