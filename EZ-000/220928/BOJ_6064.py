import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    while True:
        if M * N < x:
            print(-1)
            break
        if x % N == y % N:
            print(x)
            break
        x += M

'''참고
https://jinho-study.tistory.com/150
'''