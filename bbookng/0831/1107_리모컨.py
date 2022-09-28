import sys
input = lambda : sys.stdin.readline().strip()

N = int(input())
M = int(input())
arr = set(input().split())
result = abs(N-100)                                     # 그냥 +, - 로 이동하는 경우를 최솟값으로 설정


for i in range(10000001):                               # 작은 숫자부터, 큰 숫자부터 합한 경우의 수
    i = str(i)                                          # index 사용하기 위해서 string으로 변경
    for j in range(len(i)):                             # i의 길이 만큼
        if i[j] in arr:                                 # i 안에 고장난 버튼이 있으면
            break                                       # break 하고 다음 숫자로
    else:                                               # 위에서 break 안했다면
        result = min(result, len(i) + abs(N - int(i)))  # 숫자 버튼으로 누른 i 에서 +, - 버튼 눌러야 하는 횟수
                                                        # 비교해서 최솟값 갱신

print(result)
