# 56ms
P, M = map(int, input().split())
rooms = []
for _ in range(P):
    p, name  = input().split()
    p = int(p)

    for room in rooms:
        # 방 입장
        if len(room[1]) < M and room[0] - 10 <= p <= room[0] + 10:
            room[1].append((name, p))
            break
    else:
        # 방 생성
        rooms.append([p, [(name, p)]])
            
for room in rooms:
    if len(room[1]) == M:
        print("Started!")
    else:
        print("Waiting!")
    for player in sorted(room[1]):
        print(str(player[1]) + " " + player[0])
