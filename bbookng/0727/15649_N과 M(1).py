N, M = map(int,input().split())

def solution(i, arr):
    if i == M:                          # 순열의 길이가 채워질 때 마다 print 하고 함수를 탈출
        print(" ".join(map(str, arr)))
        return

    # 빈 list에 1이 들어있지 않으므로 i = 1만들고 arr에 1을 추가하며 재귀 > 1로 시작하는 순열 재귀
    # N+1 까지 재귀 후 i = 0일때 j = 2의 for 문으로 다시 돌아옴 > 2로 시작하는 순열 재귀
    # solution(1, arr+[1]) > solution(2, arr+[2]_

    for j in range(1, N+1):
        if j not in arr:
            solution(i+1, arr+[j])

solution(0, []) # 0과 빈 리스트로 시작

