# 실버1 / 292ms
import sys
input = lambda:sys.stdin.readline().strip()

N = int(input())
M = int(input())
S = input()
P = 'I' + 'OI'*N

cnt = 0

# 문자열 내에서 해당 문자열의 조각조각이 있는지 탐색하고 그 조각들이 다 모이면 카운트
i = 0
tmp = 0
while i < M-2:
    if S[i:i+3] == 'IOI':
        tmp += 1
        if tmp == N:
            cnt += 1
            tmp -= 1
        i += 2
    else:
        tmp = 0
        i += 1
print(cnt)


# 문자열 하나씩 없애면서 카운트
# while len(S) >= 2*N+1:
#     if S[0] == 'I':
#         if S[:2*N+1] == P:
#             cnt += 1
#             S = S[2:]
#         else:
#             S = S[1:]
#     else:
#         S = S.strip('O')
# print(cnt)


# 문자열 내에서 해당 문자열이 통째로 있는지 탐색하며 카운트
# cnt = 0
# for i in range(M-2*N):
#     if S[i:i+2*N+1] == P:
#         cnt += 1
# print(cnt)
