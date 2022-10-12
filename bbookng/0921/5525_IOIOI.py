import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()

answer = 0                                                  # 몇 번 포함되는지
count = 0                                                   # 패턴 count
i = 1                                                       # 앞 뒤로 count 하므로 1부터 시작

while i < M - 1:                                            # i+1 이 M이 되어야 하니까 M-1까지
    if S[i-1] == "I" and S[i] == "O" and S[i+1] == "I":     # IOI 면
        count += 1                                          # count +1
        if count == N:                                      # 한 패턴이 나왔으면
            count -= 1                                      # count 를 -1 해주고 (뒤에 다시 겹칠수도 있으니까)
            answer += 1                                     # 횟수 +1
        i += 1
    else:                                                   # 패턴 끊기면
        count = 0                                           # count 초기화
    i += 1                                                  # 다음 idx 로

print(answer)