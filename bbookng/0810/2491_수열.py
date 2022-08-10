# import sys
# input = sys.stdin.readline
#
# n = int(input())
# arr = list(map(int, input().split()))
#
# result = 1
# up = 1
# down = 1
#
# for i in range(n-1):
#     if arr[i] <= arr[i + 1]:
#         up += 1
#         if up > result:
#             result = up
#         else:
#             result
#     else:
#         up = 1
#
# for j in range(n-1):
#     if arr[j] >= arr[j + 1]:
#         down += 1
#         if down > result:
#             result = down
#         else:
#             result
#     else:
#         down = 1
#
# print(result)

import sys
input = sys.stdin.readline

def sol(arr):
    result = [1] * N                    # N만큼 list 만들어서 기본값 1로 설정 (1개부터 count 하니까)
    for i in range(1, N):
        if arr[i] >= arr[i - 1]:        # 전의 수보다 크면
            result[i] += result[i-1]    # 누적합
    return result                       # result를 반환

N = int(input())
arr = list(map(int,input().split())) # 커지는 수열 계산하기
arr2 = arr[::-1]                    # 거꾸로 다시 계산 (작아지는 수열)

# 각각 result 중에서 max 뽑고 그 중에 다시 max
print(max(max(sol(arr)), max(sol(arr2))))




