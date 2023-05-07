import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    memo_1 = set(map(int, input().split()))
    M = int(input())
    memo_2 = list(map(int, input().split()))

    for n in memo_2:
        answer = 1 if n in memo_1 else 0
        print(answer)
