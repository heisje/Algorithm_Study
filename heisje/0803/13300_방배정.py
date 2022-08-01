# 30840	kb 108 ms
# 성별 학년을 입력받아 li[학년]{여성:인원, 남성:인원}으로 변경
# 학년별 성별이 존재하지 않으면 0
# 있으면 몫 + 1

N, Max_room_count = map(int, input().split())

#입력
li = [{0:0, 1:0} for _ in range(6)]
for i in range(N):
    gender, grade = map(int, input().split())
    li[grade - 1][gender] += 1

#방크기로 나누어줌
room_count = 0
for dic in li:
    for i in [0, 1]:
        girl = dic.get(i)
        room_count += girl // Max_room_count
        if girl % Max_room_count > 0:
            room_count += 1
    
#print(li)
print(room_count)