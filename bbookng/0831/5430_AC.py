# import sys
# from collections import deque
# input = lambda : sys.stdin.readline().strip()
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
#             print("[" + ",".join(arr) + "]")
#         else:
#             arr.reverse()
#             print("[" + ",".join(arr) + "]")
#     else:
#         print('error')


import sys
input = lambda : sys.stdin.readline().strip()

opp = [1,0]
T = int(input())
for _ in range(T):
    p = input()
    N = int(input())
    arr = list(input()[1:-1].split(','))
    flag = 1
    left = 0
    right = len(arr) if not arr[0] == "" else 0

    for i in p:
        if i == "R":
            flag = opp[flag]
        else:
            if flag:
                left += 1
            else:
                right -= 1

    flag = -1 if not flag else 1
    result = arr[left:right][::flag] if left <= right else 'error'
    if result != "error":
        result = '['+','.join(result)+']'
    print(result)