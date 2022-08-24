N, K = map(int, input().split())

line = list(map(int, input().split()))

max_val = 0
for i in range(K):                      # 음수가 섞여 있으므로 초기값을 이렇게 설정해줄 필요가 있다.
    max_val += line[i]

for i in range(N - K + 1):
    if i == 0:
        before = max_val                                # 초기값 그대로 사용
    else:
        now = before - line[i - 1] + line[i + K - 1]    # K 범위중 가장 앞의 값을 지우고 가장 뒤에 원소 하나를 추가해주면 된다.
        before = now                                    # 다음 인덱스를 위해 before값 넣어주기
        if now >= max_val:
            max_val = now

print(max_val)