import sys
input = sys.stdin.readline

def solution(M, N, x, y):
    result = x                                               # result 는 x를 기준으로 해도, y를 기준으로 해도 상관 없음
    while result <= N*M:                                     # 최댓값 까지
        if (result-x) % M == 0 and (result-y) % N == 0:      # tc 1의 결과값인 33을 예로 들면 33은 3+3x10, 9+2x10 이므로
                                                             # 결과값은 이런 규칙을 지닌다는 것을 알 수 있음
            return result                                    # 값이 나온다면 결과 반환
        result += M                                          # 값을 찾기 위해 x면 M, y면 N 단위로 증가시켜줌
    return -1                                                # while 문 다 돌고도 안나오면 -1 return


T = int(input())

for tc in range(T):
    M, N, x, y = map(int, input().split())

    print(solution(M, N, x, y))

