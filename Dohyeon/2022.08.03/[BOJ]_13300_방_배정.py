N, K = map(int, input().split())
men_room = {i+1 :[[]] for i in range(6)}
women_room = {i+1: [[]] for i in range(6)}

room_count = 0

for i in range(N):
    s, g = map(int, input().split())
    if s == 0:
        if len(women_room[g][-1]) == K: # 방이 최대인원이다.
            women_room[g].append([]) # 새 방을 만든다.
            women_room[g][-1].append('a') # 사람이 있다는 표시
        else:
            women_room[g][-1].append('a')

    else:
        if len(men_room[g][-1]) == K: # 방이 최대인원이다.
            men_room[g].append([]) # 새 방을 만든다.
            men_room[g][-1].append('a') # 사람이 있다는 표시
        else:
            men_room[g][-1].append('a')

for i in range(6):
    room_count += len(women_room[i + 1]) # i + 1 학년이 쓰고있는 방 갯수 조사
    if len(women_room[i + 1][-1]) == 0: 
        room_count -= 1 # 빈 방이 있을 경우 1을 빼준다.
    room_count += len(men_room[i + 1])
    if len(men_room[i + 1][-1]) == 0:
        room_count -= 1


print(room_count)
