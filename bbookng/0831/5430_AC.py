# import sys
# from collections import deque
# input = lambda: sys.stdin.readline().strip()
#
# T = int(input())
# for tc in range(T):
#     p = input()
#     n = int(input())
#     arr = deque(input()[1:-1].split(','))
#     cnt = 0
#     flag = True
#
#     if n == 0:
#         arr = []
#
#     for i in p:
#         if i == 'R':
#             cnt += 1
#             continue
#         elif i == 'D':
#             if not arr:
#                 flag = False
#                 break
#             else:
#                 arr.pop() if cnt % 2 else arr.popleft()
#
#     if flag:
#         if cnt % 2 == 0:
#             print('[' + ','.join(arr) + ']')
#         else:
#             arr.reverse()
#             print('[' + ','.join(arr) + ']')
#     else:
#         print('error')


import sys
input = lambda: sys.stdin.readline().strip()

opp = [1, 0]
T = int(input())
for _ in range(T):
    p = input()
    N = int(input())
    arr = list(input()[1:-1].split(','))
    flag = 1                                        # 뒤집는걸 표시
    left = 0
    right = len(arr) if not arr[0] == "" else 0     # 빈 리스트를 받을 경우 에러처리를 위한 조건문

    for i in p:                                     # 수행할 함수
        if i == "R":                                # R이면
            flag = opp[flag]                        # flag로 뒤집힌 상태인지 아닌지 표시
        else:                                       # D이면
            if flag:                                # flag가 1일때 정방향 이므로 left를 +1
                left += 1
            else:                                   # 0일때 역방향이므로 right를 +1
                right -= 1

    flag = -1 if not flag else 1                    # flag가 0일때 -1로 변경처리
    # left가 right 보다 크면 리스트에 든게 없으므로 error
    # left 부터 rigth 까지 result에 담고, flag에 따라서 배열 방향 결정
    result = arr[left:right][::flag] if left <= right else 'error'
    if result != 'error':
        result = '['+','.join(result)+']'
    print(result)