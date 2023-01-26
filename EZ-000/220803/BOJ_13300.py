import sys

total, room = map(int, sys.stdin.readline().split())
# 표를 리스트 안에 그대로 옮겨옴
students = [[[0, 0], [1, 0]], [[0, 0], [1, 0]], [[0, 0], [1, 0]], [[0, 0], [1, 0]], [[0, 0], [1, 0]], [[0, 0], [1, 0]]]
# 반복문을 돌면서 성별과 학년에 맞게 중첩 리스트 내의 학생수 항목이 늘어남
for student in range(total):
    gender, grade = map(int, sys.stdin.readline().split())
    for n in range(1, 7):
        if gender == 0 and grade == n:
            students[n - 1][0][1] += 1
        elif gender == 1 and grade == n:
            students[n - 1][1][1] += 1

rooms = 0
# 나눠진 학생 수가 방 정원으로 나누어 떨어지는 경우와 아닌 경우로 분리해서 방의 개수를 세는 코드
for n in range(1, 7):
    girls = students[n - 1][0][1]
    boys = students[n - 1][1][1]

    if girls % room == 0:
        rooms += girls // room
    else:
        rooms += girls // room + 1

    if boys % room == 0:
        rooms += boys // room
    else:
        rooms += boys // room + 1

print(rooms)

'''mini_log
꽤 느린 코드이다. 100ms.
밑에 두 가지 나중에 해보자.
1. 마지막 부분을 반복문으로 바꾸기
2. 중첩 리스트 말고 다른 자료구조를 쓰기
'''
