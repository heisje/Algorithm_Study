# 실버1 / 2996ms -> list 사용, 100ms -> dictionary 사용
import sys
input = sys.stdin.readline

# N : 접시의 수, d : 초밥의 가짓수, k : 연속해서 먹는 접시의 수, c : 쿠폰 번호
N, d, k, c = map(int, input().split())
sushies = []
for _ in range(N):
    sushies.append(int(input()))
sushies *= 2

s, e = 0, 0
max_length = 0
length = 1
dic = {sushies[s]: 1}
while s<N or e<N:
    # 더하는 경우
    if e-s+1 < k:
        e += 1
        if sushies[e] in dic:
            dic[sushies[e]] += 1
            if dic[sushies[e]] == 1:
                length += 1
        else:
            dic[sushies[e]] = 1
            length += 1

    # 빼는 경우
    elif e-s+1 == k:
        dic[sushies[s]] -= 1
        if dic[sushies[s]] == 0:
            length -= 1
            del dic[sushies[s]]
        s += 1

    # 최대값 갱신
    if max_length <= length:
        if c not in dic:
            max_length = length+1
        else:
            max_length = length
    # print(s, e, dic, length)
print(max_length)