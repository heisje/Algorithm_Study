# 실버3 / 128ms
import sys
input = lambda : sys.stdin.readline().strip()

# 내 코드 -> 시간초과떠서 pypy로 품
N = int(input())
DP = [0] * (N+1)
DP[0] = 0
for i in range(1, N+1):
    tmp = 100
    for j in range(1, i+1):
        if j*j > i:
            break
        if DP[i - j*j] + 1 < tmp:
            tmp = DP[i - j*j] + 1
    DP[i] = tmp
print(DP[N])

# python으로 푼 사람꺼 보고 따라 만든거
# N = int(input())
# lst1 = [i*i for i in range(1, int(N**0.5)+1)] # 제곱수만 담음
# lst2 = []
# for i in range(len(lst1)):
#     for j in range(i, len(lst1)):
#         lst2.append(lst1[i]+lst1[j])          # 제곱수 리스트 중 2개를 뽑아서 합한 값 리스트 (len(lst1) C 2)
# lst2_set = set(lst2)                          # 중복 없앰
# def answer(N):
#     if N in lst1:  # 제곱수면
#         return 1
#     elif N in lst2:  # 제곱수 두개를 더해서 만들 수 있는 수면
#         return 2
#     else:
#         for square in lst1:  # 제곱 수 중
#             if N - square in lst2:  # n에서 제곱수를 뺀 수가 제곱수 두개를 더해서 만들수 있는 수면
#                 return 3
#     return 4
# print(answer(N))

# DP[1] = 1   # 1
# DP[2] = 2   # 1 1
# DP[3] = 3   # 1 1 1
# DP[4] = 1   # 2
# DP[5] = 2   # 2 1
# DP[6] = 3   # 2 1 1
# DP[7] = 4   # 2 1 1 1
# DP[8] = 2   # 2 2
# DP[9] = 1   # 3
# DP[10] = 2  # 3 1
# DP[11] = 3  # 3 1 1
# DP[12] = 3  # 2 2 2
# DP[13] = 2  # 3 2
# DP[14] = 3  # 3 2 1
# DP[15] = 4  # 3 2 1 1
# DP[16] = 1  # 4
# DP[17] = 2  # 4 1
# DP[18] = 2  # 3 3
# DP[19] = 3  # 3 3 1
# DP[20] = 2  # 4 2
# DP[21] = 3  # 4 2 1
# DP[22] = 3  # 3 3 2