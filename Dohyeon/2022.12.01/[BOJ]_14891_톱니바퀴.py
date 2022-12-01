 lines (54 sloc)  1.75 KB

class Gear:
    def __init__(self, gear_list):
        self.gear_list = gear_list

    def get_gearlist(self):
        return self.gear_list

    def get_left(self):
        return self.gear_list[6]

    def get_right(self):
        return self.gear_list[2]

    def get_top(self):
        return self.gear_list[0]

    def turn_right(self):
        tmp = self.gear_list.pop()
        self.gear_list.insert(0, tmp)

    def turn_left(self):
        tmp = self.gear_list.pop(0)
        self.gear_list.append(tmp)

factory = [Gear([0])] * 5
for j in range(1, 5):
    factory[j] = Gear(list(input()))

N = int(input())
for i in range(N):
    num, direction = map(int, input().split())
    moves = [[['dummy'], [False, 1], [False, -1], [False, 1], [False, -1]], [['dummy'], [False, -1], [False, 1], [False, -1], [False, 1]]]

    if (num - 1) % 2:
        f_direction = -direction
    else:
        f_direction = direction

    if f_direction == 1:
        f_move = moves[0]    # 첫번째 톱니가 시계방향
    else:
        f_move = moves[1]    # 첫번째 톱니가 반시계방향

    f_move[num][0] = True
    for j in range(num, 4):
        if factory[j].get_right() != factory[j + 1].get_left():
            f_move[j + 1][0] = True
        else:
            break
    for j in range(num, 1, -1):
        if factory[j].get_left() != factory[j - 1].get_right():
            f_move[j - 1][0] = True
        else:
            break
    for j in range(1, 5):
        if f_move[j][0]:
            if f_move[j][1] == 1:
                factory[j].turn_right()
            else:
                factory[j].turn_left()

total = 0
for j in range(1, 5):
    n = int(factory[j].get_top())
    total += n * (2 ** (j - 1))
print(total)