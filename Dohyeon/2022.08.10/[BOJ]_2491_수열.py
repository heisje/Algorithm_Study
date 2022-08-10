N = int(input())
num_list = list(map(int, input().split()))

length = 1                                      # 얼마나 이어지고 있는가를 확인
max_length = 0                                  # 최장 오름차순, 내림차순 길이
same_length = 0                                 # 같은 것이 연속으로 나온 길이
up_t_down_f = True                              # 오름차순이면 True, 내림차순이면 False를 가지는 변수이다.
if N == 1:
    max_length = 1
for i in range(N - 1):                          # 특정 인덱스와 그 다음 값을 확인해야 하므로 N - 1까지만 체크
    if i == 0:                                  # 수열이 시작할 때를 확인
        if num_list[i] > num_list[i + 1]:       # 내림차순일 때
            up_t_down_f = False
            length += 1
        elif num_list[i] < num_list[i + 1]:     # 오름차순일 때
            up_t_down_f = True
            length += 1
        else:                                   # 같은 값이 연속으로 나올 때
            same_length += 1                    # 갑자기 같은 숫자들 이후에 오름차순, 내림차순이 바뀔 때 이 값을 더 해주어야 한다. ex) 1 4 4 4 2
            length += 1                         # 위와 같이 차순이 바뀌는게 아니라면 그냥 length를 더하면 된다.
    else:
        if up_t_down_f:                         # 오름차순이 유지되고 있을 때
            if num_list[i] < num_list[i + 1]:   # 다시 오름 차순이 나올 때
                length += 1                     # 그냥 길이를 다시 더하면 된다.
                if same_length != 0:            # 앞에서 같은 숫자가 계속 나왔었지만 length 값으로 더해져 왔기 때문에 값이 same_length 필요없어짐
                    same_length = 0             # 그러므로 0으로 다시 초기화
            elif num_list[i] > num_list[i + 1]: # 내림차순으로 변경됐을 때
                length = 2                      # 현재 값과 다음 값을 합쳐서 길이가 2임
                up_t_down_f = False             # 내림차순으로 변경됨을 알림
                if same_length != 0:            # 앞에서 같은 숫자가 계속 나왔었기 때문에 이 값이 있다면
                    length += same_length       # 이 값들도 내림차순에 포함되기 때문에 더해줘야 한다.
                    same_length = 0             # 0으로 초기화
            else:
                length += 1                     # 같은 값이 반복될 경우 length + 1
                same_length += 1                # 다음에 차순이 변경될 경우를 대비해 same_length + 1

        else:                                   # 내림차순이 유지되고 있을 때, 이는 위에서 오름 차순이 유지되고 있었을 때와 같은 방법으로 해결
            if num_list[i] > num_list[i + 1]:   # 내림차순 유지
                length += 1
                if same_length != 0:
                    same_length = 0
            elif num_list[i] < num_list[i + 1]: # 오름차순으로 변경
                length = 2
                up_t_down_f = True
                if same_length != 0:
                    length += same_length
                    same_length = 0
            else:                               # 같은 값일 때
                length += 1
                same_length += 1
                
    if length > max_length:                     # 현재까지의 length가 최대 길이를 넘는지 확인
        max_length = length
        
print(max_length)


