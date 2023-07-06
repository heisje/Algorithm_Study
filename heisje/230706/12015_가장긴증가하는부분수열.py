# pypy3 568ms
import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))
dp = [0]

for idx, value in enumerate(li):
    left = 0
    right = len(dp) - 1
    while left <= right:
        middle = (left + right) // 2
        # 값이 같으면 이전 포인터에 더 작은 값이 있는지 찾아봐야한다. (왼쪽 탐색)
        if dp[middle] == value:
            right = middle - 1
        # dp보다 작으면 포인터를 왼쪽으로 옮겨서 왼쪽을 탐색하고
        elif dp[middle] > value:
            right = middle - 1
        # dp보다 크면 포인터를 오른쪽으로 옮겨서 오른쪽을 탐색하고
        else:
            left = middle + 1
    # 포인터가 배열을 다 뒤져도 값이 더 커서 넘치면 추가시킨다.
    if left >= len(dp):
        dp.append(value)
    # 포인터가 배열에 맞게 위치해서 값을 변환시킨다.
    else:
        dp[left] = value

print(len(dp) - 1)