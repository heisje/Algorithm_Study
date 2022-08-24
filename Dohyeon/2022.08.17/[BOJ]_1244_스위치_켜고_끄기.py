import sys

input = lambda: sys.stdin.readline().strip()

num_of_switch = int(input())
switch_list = list(map(int, input().split()))  # 스위치 초기 상태 리스트
num_of_people = int(input())


def change_switch(s_list, idx):
    if s_list[idx] == 1:
        switch_list[idx] = 0
    else:
        switch_list[idx] = 1


for i in range(num_of_people):
    a, b = map(int, input().split())
    if a == 1:                          # 남학생인 경우

        for j in range(num_of_switch):
            if (j + 1) % b == 0:  # b의 배수인지 확인한다
                change_switch(switch_list, j)



    else:                               # 여학생인 경우
        change_switch(switch_list, b - 1)
        k = 1
        while (True):
            try:                        # 인덱스 에러가 날 때 까지, 또는 양 옆이 대칭이 안될 때 까지
                if switch_list[b - 1 - k] == switch_list[b - 1 + k]:
                    if (b - 1 - k) < 0:  # 중요!!!!!!! try except 문에서 python은 음수 인덱스도 정상으로 처리하기 때문에 음수 인덱스가 error 처리 되지 않음

                        break
                    change_switch(switch_list, b - 1 - k)
                    change_switch(switch_list, b - 1 + k)
                    k = k + 1           # 한 칸 더 양 옆을 살펴본다.
                    continue
                else:
                    break
            except IndexError:
                break

for i in range(len(switch_list)):

    if (i + 1) % 20 == 0:
        print(switch_list[i])
    else:
        if i == len(switch_list) - 1:
            print(switch_list[i], end='')
        else:
            print(switch_list[i], end=' ')
