import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    for i in range(4, 0, -1):
        if A[1:].count(i) > B[1:].count(i):
            print('A')
            break
        elif A[1:].count(i) < B[1:].count(i):
            print('B')
            break
        else:
            if i == 1:
                print('D')
                break