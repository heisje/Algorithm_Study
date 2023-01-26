import sys

N = int(sys.stdin.readline())
for _ in range(N):
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    cntA = []
    cntB = []
    for n in [4, 3, 2, 1]:
        cntA.append(A[1:].count(n))
        cntB.append(B[1:].count(n))
    for idx in range(4):
        if cntA[idx] == cntB[idx]:
            continue
        elif cntA[idx] > cntB[idx]:
            print('A')
            break
        elif cntA[idx] < cntB[idx]:
            print('B')
            break
    else:
        print('D')
