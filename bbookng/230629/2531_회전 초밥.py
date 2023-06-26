from collections import defaultdict

N, d, k, c = map(int, input().split())

arr = [int(input()) for _ in range(N)]

check = defaultdict(int)

left, right = 0, k

for i in range(k):
    check[str(arr[i])] += 1

check[str(c)] += 1

answer = len(check.keys())

while left < N-1:
     check[str(arr[left])] -= 1
     if not check[str(arr[left])]:
          check.pop(str(arr[left]))
     check[str(arr[right])] += 1
     if answer <= len(check.keys()):
          answer = len(check.keys())

     left += 1
     right += 1
     right %= N

print(answer)

