from collections import deque

N = int(input())

dq = deque()

for n in range(1, 10):
    dq.append(n)

cnt = 0
while dq:
    n = dq.popleft()
    if n // (10 ** (N-1)):
        cnt += 1
        continue
    nn = n % 10
    if nn + 1 <= 9:
        dq.append(n * 10 + nn + 1)
    if 0 <= nn - 1:
        dq.append(n * 10 + nn - 1)

# cnt = 9
# for n in range(N-1):
#     cnt = cnt * 2 - (n + 1)

print(cnt % 1000000000)