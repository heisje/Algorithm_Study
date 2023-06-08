# 모든 수를 돌면서
# 그 수를 제외한 양 옆의 리스트를 더해주고
# 작으면 오른쪽 포인터를 내리고
# 크면 왼쪽 포인터를 올리자

# 408ms

import sys
input = sys.stdin.readline

def check(idx, li):
    target = li[idx]
    others = li[:idx]
    if idx < len(li) - 1:
        others += li[idx + 1:]
    
    left = 0
    right = len(others) - 1
    while left < right:
        if target < others[left] + others[right]:
            right -= 1
        elif target > others[left] + others[right]:
            left += 1
        elif target == others[left] + others[right]:
            return 1
    return 0

def main(N, li):
    answer = 0
    for idx in range(N):
        answer += check(idx, li)
    print(answer)

N = int(input())
li = sorted(list(map(int, input().split())))

if N < 3:
    print(0)
else:
    main(N, li)








# # 한자리 숫자를 기준으로 이분탐색을 하여 찾는다.
# import sys
# input = sys.stdin.readline

# def check(target, li):
#     # print('체크시작',target, li)
#     for leftIdx in range(len(li)):
#         # left와 마지막 점 사이
#         left = li[leftIdx]
#         rightList = li[leftIdx + 1:len(li)]
        
#         while rightList:
#             right = rightList[len(rightList) // 2]
#             # print(rightList)
#             # print(left, right)
#             if left + right == target:
#                 return 1
#             if len(rightList) == 1:
#                 break
#             if left + right > target:
#                 rightList = rightList[:len(rightList) // 2]
#                 # print('down')
#             if left + right < target:
#                 rightList = rightList[len(rightList) // 2+1:]
#                 # print('up')
            
#     return 0


# def main(N, li):
#     answer = 0
#     li.sort()
#     for i in range(2, N):
#         leftList = li[0:i]
#         rightList = []
#         # 같은 숫자일 시 rightList에 추가한다.
#         if i < N - 2:
#             for j in range(i + 1, N):
#                 if li[i] == li[j]:
#                     rightList.append(li[j])
#                 else:
#                     break
        
#         temp = check(li[i], leftList+rightList)
#         # print(temp)
#         answer += temp
#     print(answer)
        
# N = int(input())
# li = list(map(int, input().split()))

# if N < 3:
#     print(0)
# else:
#     main(N, li)