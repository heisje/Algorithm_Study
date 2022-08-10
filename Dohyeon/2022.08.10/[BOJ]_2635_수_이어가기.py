import copy

N = int(input())

def make_line(a, b):                                # 주어진 두 수를 이용해 수를 이어나가는 함수
    result = [a, b]
    while(True):
        if a - b >= 0:                              # 음의 정수가 아닐 때
            result.append(a - b)                    # 이어간다.
            temp = a - b                            # b 와 새로 만들어진 수를 계산할 준비
            a = b
            b = temp
        else:
            break
    return result

max_len = 0
for i in range(0, N + 1):

    new_val = len(make_line(N, i))
    if new_val > max_len:                           # 최고 길이를 갱신할 경우
        max_len = new_val                           # 최고 길이 저장
        result_list = copy.deepcopy(make_line(N, i))  # 깊은 복사로 이어진 수의 리스트를 복사

print(max_len)
print(*result_list)                             # 리스트 일렬로 출력

