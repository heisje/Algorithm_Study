import copy

num_of_dice = int(input())

dice = [[] for i in range(num_of_dice)]

for i in range(num_of_dice):
    dice[i] = dice[i] + list(map(int, input().split()))

total_max = 0
for i in range(6):                              # 가장 밑에 깔린 주사위의 아랫면을 결정, 방법은 6가지
    round_max = 0
    round_dice = copy.deepcopy(dice)
    upside = 0
    for j in range(num_of_dice):
        if j == 0:                              # 가장 아래 주사위 일 떄
            if i == 0:                          # 0번 인덱스는 5번 인덱스와 연결되어있음
                upside = round_dice[j][5]
            elif i == 1:                        # 1번은 3번
                upside = round_dice[j][3]
            elif i == 2:                        # 2번은 4번
                upside = round_dice[j][4]
            elif i == 3:
                upside = round_dice[j][1]
            elif i == 4:
                upside = round_dice[j][2]
            elif i == 5:
                upside = round_dice[j][0]
            del round_dice[j][i]                # 아랫면을 제거해준다
            round_dice[j].remove(upside)        # 윗면을 제거해준다
        else:
            down_side_idx = round_dice[j].index(upside)
            if down_side_idx == 0:
                upside = round_dice[j][5]
            elif down_side_idx == 1:
                upside = round_dice[j][3]
            elif down_side_idx == 2:
                upside = round_dice[j][4]
            elif down_side_idx == 3:
                upside = round_dice[j][1]
            elif down_side_idx == 4:
                upside = round_dice[j][2]
            elif down_side_idx == 5:
                upside = round_dice[j][0]
            del round_dice[j][down_side_idx]    # 아랫면을 제거해준다.
            round_dice[j].remove(upside)        # 윗면을 제거해준다.

        round_max += max(round_dice[j])
    if round_max > total_max:
        total_max = round_max

print(total_max)




