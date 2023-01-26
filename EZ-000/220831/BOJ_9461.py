T = int(input())
for _ in range(T):
    padovan = [1, 1, 1, 2, 2]
    N = int(input())
    if N > 5:
        for _ in range(N - 5):
            padovan.append(padovan[-1] + padovan[-5])
        print(padovan[-1])
    else:
        print(padovan[N - 1])
