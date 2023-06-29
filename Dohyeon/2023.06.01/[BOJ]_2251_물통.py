from collections import deque

A, B, C = map(int, input().split())
A_in, B_in = 0, 0
C_in = C

result = []


def QtoK(Q, K, Qin, Kin):
    if Qin >= K - Kin:
        new_Kin = K
        new_Qin = Qin - (K - Kin)

    else:
        new_Qin = 0
        new_Kin = Kin + Qin

    return new_Qin, new_Kin


check_dick = {}

dq = deque()
dq.append([A_in, B_in, C_in])

while (dq):

    now = dq.popleft()

    # print(now)
    if now[0] == 0:  # 조건에 해당
        if now[2] not in result:
            result.append(now[2])

    try:
        key = check_dick[now[0] * 1000000 + now[1] * 1000 + now[2]]  # 이미 했던 것일 경우

        continue

    except KeyError:
        check_dick[now[0] * 1000000 + now[1] * 1000 + now[2]] = 1
        # A to B
        if now[0] != 0:
            new_A, new_B = QtoK(A, B, now[0], now[1])
            dq.append([new_A, new_B, now[2]])
            # A to C
            new_A, new_C = QtoK(A, C, now[0], now[2])
            dq.append([new_A, now[1], new_C])

        # B to A
        if now[1] != 0:
            new_B, new_A = QtoK(B, A, now[1], now[0])
            dq.append([new_A, new_B, now[2]])
            # B to C
            new_B, new_C = QtoK(B, C, now[1], now[2])
            dq.append([now[0], new_B, new_C])

        # C to A
        if now[2] != 0:
            new_C, new_A = QtoK(C, A, now[2], now[0])
            dq.append([new_A, now[1], new_C])
            # C to B
            new_C, new_B = QtoK(C, B, now[2], now[1])
            dq.append([now[0], new_B, new_C])

result.sort()
for i in range(len(result)):
    print(result[i], end=" ")

# 1000으로 곱하자
# BFS


