# 48ms

def main(N, li):
    dp = [0 for _ in range(N)]
    for n in range(N):                      # 왼쪽부터 차례로 dp테이블을 누적시킨다.
        count = 1
        # 왼쪽에 있는 중심점 보다 큰 개수를 Count에 누적시킨다.
        for left in range(0, n):
            if li[left] < li[n]:            # 중심점 보다 작으면
                if count < dp[left] + 1:    # count를 큰 값으로 갱신시킨다.
                    count = dp[left] + 1
        dp[n] = count
    print(N - max(dp))

N = int(input())
li = list(int(input()) for _ in range(N))
main(N, li)

# from collections import deque
# # 왼쪽을 탐색한다.
# # 오른쪽을 탐색한다.
# # 틀린 것이 있으면 왼쪽부터 가져온다.
# # 오른 쪽이 틀렸으면 오른쪽을 가져온다.
# # 중앙 점 까지 반복한다.

# # 인덱스 구조를 변형시키지 않기위해 visited를 사용한다.
# # 이미 처리가 된 곳이면 -1을,
# # 앞 데이터까지 변형이 됐으면 
# def left(num, li, collect):
#     print('move: ', num, li)
#     li.remove(num)
#     collect[num - 1] = num

# def right(num, li, collect):
#     print('move: ', num, li)
#     li.remove(num)
#     collect[num - 1] = num

# def main(N, li):
#     idx = 0
#     counter = 0
#     collect = [0 for _ in range(N)]
#     start = 0
#     print(li)
#     idx = 0
#     while li:
#         if li[idx - start] != idx + 1:
#             # 찾아서 삭제
#             left(idx + 1, li, collect)
#             start += 1
#             print('counter + 1', counter)
#             counter += 1
#         else:
#             left(idx + 1, li, collect)
#             start += 1
#         if li:
#             if li[N - idx - 1 - start] != N - idx:
#                 # 찾아서 삭제
#                 right(N - idx, li, collect)
#                 print('counter + 1', counter)
#                 counter += 1
#             else:
#                 left(idx + 1, li, collect)
#         idx += 1
#     print(li)
#     print(collect)
#     print(counter)

# N = int(input())
# li = deque(int(input()) for _ in range(N))
# main(N, li)