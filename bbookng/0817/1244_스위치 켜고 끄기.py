import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

S = int(input())
for i in range(S):
    sex, num = map(int, input().split())
            if sex == 1:                                                # 남학생일 때
                for j in range(N):                                      # 전구 전범위
            if (j+1) % num == 0:                                        # 자기가 받은 수의 배수일 때
                if arr[j] == 0:                                         # 0이면
                    arr[j] = 1                                          # 1로 바꾸기
                else:                                                   # 1이면
                    arr[j] = 0                                          # 0으로 바꾸기
    else:                                                               # 여학생일 때
        num -= 1                                                        # idx 계산 편하게 하기 위해 num -1 해줌
        for j in range(N):                                              # 전구 전범위
            if num-j >= 0 and num+j < N and arr[num-j] == arr[num+j]:   # 받은 수를 기준으로 num-j 와 num+j가 전구 개수의 범위를 벗어나지 않고 같으면
                if arr[num-j] == 1:                                     # 1이면
                    arr[num-j] = arr[num+j] = 0                         # 둘 다 0으로 바꿔줌
                else:                                                   # 0이면
                    arr[num-j] = arr[num+j] = 1                         # 둘 다 1로 바꿔줌
            else:
                break

for i in range(N):
    print(arr[i], end = ' ')
    if (i+1) % 20 == 0:
        print()
