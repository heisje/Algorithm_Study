# 가장 긴 증가하는 부분 수열 문제라고 한다.
N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]


def main():
    li.sort()
    dp = [1000]        # 가장 큰 값을 누적시킬 dp

    for _, value in li:
        if dp[-1] < value:    # 증가하는 부분수열일 경우
            dp.append(value)
        else:                 # 증가가 멈췄을 경우
            for i in range(len(dp)):
                if dp[i] > value:
                    dp[i] = value
                    break
    return N-len(dp)


print(main())
