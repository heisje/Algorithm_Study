X, Y = map(int, input().split())
num_store = int(input())

stores = [[] for i in range(num_store)]
for i in range(num_store):
    stores[i] = stores[i] + list(map(int, input().split()))

dong_1, dong_2 = map(int, input().split())

total = 0
for i in range(num_store):
    if dong_1 == 1:                                             # 상
        if stores[i][0] == 1:
            total += abs(dong_2 - stores[i][1])

        elif stores[i][0] == 2:

            if dong_2 + stores[i][1] > X:
                total += 2*X - dong_2 - stores[i][1] + Y
            else:
                total += dong_2 + stores[i][1] + Y

        elif stores[i][0] == 3:
            total += dong_2 + stores[i][1]

        elif stores[i][0] == 4:
            total += X - dong_2 + stores[i][1]

    elif dong_1 == 2:                                           # 하
        if stores[i][0] == 1:

            if dong_2 + stores[i][1] > X:
                total += 2*X - dong_2 - stores[i][1] + Y
            else:
                total += dong_2 + stores[i][1] + Y

        elif stores[i][0] == 2:
            total += abs(dong_2 - stores[i][1])

        elif stores[i][0] == 3:
            total += dong_2 + Y - stores[i][1]

        elif stores[i][0] == 4:
            total += X - dong_2 + Y - stores[i][1]

    elif dong_1 == 3:                                           # 좌
        if stores[i][0] == 1:
            total += dong_2 + stores[i][1]

        elif stores[i][0] == 2:
            total += Y - dong_2 + stores[i][1]

        elif stores[i][0] == 3:
            total += abs(dong_2 - stores[i][1])

        elif stores[i][0] == 4:
            if dong_2 + stores[i][1] > Y:
                total += 2 * Y - dong_2 - stores[i][1] + X
            else:
                total += dong_2 + stores[i][1] + X

    elif dong_1 == 4:                                           # 우
        if stores[i][0] == 1:
            total += X - stores[i][1] + dong_2

        elif stores[i][0] == 2:
            total += X - stores[i][1] + Y - dong_2

        elif stores[i][0] == 3:
            if dong_2 + stores[i][1] > Y:
                total += 2 * Y - dong_2 - stores[i][1] + X
            else:
                total += dong_2 + stores[i][1] + X

        elif stores[i][0] == 4:
            total += abs(dong_2 - stores[i][1])

print(total)