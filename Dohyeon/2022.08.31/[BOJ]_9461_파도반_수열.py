import sys
input = lambda : sys.stdin.readline().strip()

testcase = int(input())

p_dict = {1 : 1, 2 : 1, 3 : 1}                                  # 데이터들을 저장해 둘 딕셔너리

def wave_class(N):

    if N == 1 or N == 2 or N == 3:                              # 1, 2, 3 의 값을 원하면 1을 바로 반환
        return 1
    try:
        return p_dict[N]                                        # 이미 저장된 데이터가 있는지 확인
    except KeyError:
        p_dict[N] =  wave_class(N - 3) + wave_class(N - 2)      # 저장된 값이 없으면 재귀를 통해 값을 만든다
        return p_dict[N]

for tc in range(1, testcase + 1):
    n = int(input())
    print(wave_class(n))



