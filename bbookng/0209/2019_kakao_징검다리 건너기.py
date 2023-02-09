def solution(stones, k):
    answer = 0
    start = 1
    end = 200000000

    def check(N, stones):
        cnt = 0
        for stone in stones:
            if stone < N:
                cnt += 1
                if cnt == k:
                    return False
            else:
                cnt = 0
        return True

    while start <= end:
        mid = (start + end) // 2
        print(mid)
        if check(mid, stones):
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.05ms, 10.3MB)
테스트 6 〉	통과 (0.18ms, 10.2MB)
테스트 7 〉	통과 (0.32ms, 10.1MB)
테스트 8 〉	통과 (0.43ms, 10.1MB)
테스트 9 〉	통과 (0.76ms, 10.4MB)
테스트 10 〉	통과 (0.02ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.1MB)
테스트 13 〉	통과 (0.04ms, 10.1MB)
테스트 14 〉	통과 (0.14ms, 10.1MB)
테스트 15 〉	통과 (0.43ms, 10.2MB)
테스트 16 〉	통과 (0.74ms, 10.2MB)
테스트 17 〉	통과 (0.71ms, 10.1MB)
테스트 18 〉	통과 (0.03ms, 10.2MB)
테스트 19 〉	통과 (0.02ms, 10.2MB)
테스트 20 〉	통과 (0.10ms, 10.3MB)
테스트 21 〉	통과 (0.14ms, 10.2MB)
테스트 22 〉	통과 (0.75ms, 10.3MB)
테스트 23 〉	통과 (0.61ms, 10.2MB)
테스트 24 〉	통과 (0.50ms, 10.3MB)
테스트 25 〉	통과 (0.03ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (176.07ms, 18.6MB)
테스트 2 〉	통과 (237.70ms, 18.5MB)
테스트 3 〉	통과 (232.89ms, 18.6MB)
테스트 4 〉	통과 (99.46ms, 18.5MB)
테스트 5 〉	통과 (112.62ms, 18.6MB)
테스트 6 〉	통과 (116.38ms, 18.6MB)
테스트 7 〉	통과 (283.44ms, 18.6MB)
테스트 8 〉	통과 (316.05ms, 18.5MB)
테스트 9 〉	통과 (294.38ms, 18.5MB)
테스트 10 〉	통과 (283.24ms, 18.5MB)
테스트 11 〉	통과 (256.07ms, 18.5MB)
테스트 12 〉	통과 (279.52ms, 18.6MB)
테스트 13 〉	통과 (154.14ms, 18.5MB)
테스트 14 〉	통과 (120.65ms, 18.5MB)
'''