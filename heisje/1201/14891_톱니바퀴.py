from collections import deque
# 시뮬레이션 구현
# deque로 톱니바퀴를 돌리면서 구현한다.

# 돌리기
def gear_rotate(gear_arr, direction):
    if direction == 1:
        gear_arr.appendleft(gear_arr.pop())
    elif direction == -1:
        gear_arr.append(gear_arr.popleft())

arr = []
arr_lefts = [0,0,0,0]  #기어의 왼쪽을 전부 저장
arr_rights = [0,0,0,0]  #기어의 오른쪽을 전부 저장
for n in range(4):
    arr.append(deque(map(int, input())))

rotates = []  # 돌리기 저장
for n in range(int(input())):
    rotates.append(list(map(int, input().split())))

for gear, direction  in rotates:  #돌리기 저장
    gear -= 1
    # 기어의 번호에 따라
    # 좌극 우극를 구한 다음에
    for i in range(4):
        arr_lefts[i] = arr[i][6]
        arr_rights[i] = arr[i][2]
    # 돌린다.
    gear_rotate(arr[gear], direction)
    # 옆 기어의 좌 우극을 구한 다음에

    # 메인기어의 오른쪽 기어 테스트
    main = gear   # 메인
    right = gear + 1  # 오른쪽
    ri_di = direction * -1  # 돌리는 방향
    while 0 <= right < 4:
        if arr_rights[main] != arr_lefts[right]: #다르면
            #돈다
            gear_rotate(arr[right], ri_di)
        else:
            break 
        main = right  #다음꺼 테스트용
        right = right + 1
        ri_di = ri_di * -1
    # 메인기어의 왼쪽 기어 테스트
    left = gear - 1
    main = gear
    le_di = direction * -1
    while 0 <= left < 4:
        if arr_rights[left] != arr_lefts[main]:
            #돈다
            gear_rotate(arr[left], le_di)
        else:
            break
        main = left
        left = left - 1
        le_di = le_di * -1

result = 0
for n in range(4):
    if arr[n][0] == 1:
        result += (2**n)
    
print(result)

# 골드5 / 90분 / 92ms