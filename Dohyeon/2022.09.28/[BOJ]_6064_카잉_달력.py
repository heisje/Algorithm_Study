import sys

input = lambda: sys.stdin.readline().strip()

testcase = int(input())

for tc in range(1, testcase + 1):
    M, N, x, y = map(int, input().split())

    # M, N의 최소공배수가 지구 최후의 날!
    """
    gcm = M*N
    for i in range(max(M,N), M*N + 1):
        if i % M == 0 and i % N == 0:
            gcm = i

    num = gcm // M              # M은 num개 존재 가능
    """
    check = False               # 최소공배수 도달로 나온건지만 확인
    for i in range(N):
        maybe_year = i*M + x    # 년도 수 (우리버전)
        temp = maybe_year % N   # 오른쪽 값을 찾아주자
        if temp == 0:           # 나누어 떨어지는 경우에는 N이된다.
            temp = N
        if temp == y:
            print(maybe_year)
            check = True
            break
        if i != 0 and i*M % N == 0:
            break
    if not check:
        print(-1)


