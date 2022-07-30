N, K = map(int, input().split())
cnt = 0

students = [list(map(int, input().split())) for _ in range(N)]
# 각 성별의 학년만 리스트에 저장
girls = [g[1] for g in students if g[0] == 0]
boys = [b[1] for b in students if b[0] == 1]

for i in [girls, boys]:
    room = []                                       # 방의 개수가 정해진 학년을 추가할 리스트 생성
    for j in i:
        if j not in room:
            if i.count(j) % K == 0:                 # 각 학년의 학생수가 방의 최대 인원으로 나누어 떨어지면 몫을 카운트
                cnt += i.count(j) // K
            else:
                cnt += i.count(j) // K + 1          # 나누어 떨어지지 않으면 (몫+1)을 카운트
            room.append(j)
        
print(cnt)