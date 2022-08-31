T = int(input())

for _ in range(T):
    N = int(input())
    P = [1, 1, 1, 2, 2]

    for i in range(4, N):
        P.append(P[i]+P[i-4])
    
    print(P[N-1])
