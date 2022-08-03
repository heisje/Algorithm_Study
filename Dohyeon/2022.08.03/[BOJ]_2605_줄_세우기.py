num = int(input()) # 학생 수
stud_list = list(map(int, input().split())) # 학생들이 뽑은 표
initial_list = list(range(1, num + 1)) # 학생들의 초기 위치

for i in range(num):
    initial_list.insert(i - stud_list[i], initial_list[i])
    initial_list.pop(i + 1)
for j in initial_list:
    print(j, end = ' ')