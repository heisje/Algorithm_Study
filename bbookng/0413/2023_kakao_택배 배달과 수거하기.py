def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver = 0
    pick = 0

    for i in range(n):
        deliver += deliveries[n - i - 1]
        pick += pickups[n - i - 1]
        while deliver > 0 or pick > 0:
            deliver -= cap
            pick -= cap
            answer += (n - i) * 2

    return answer

'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.00ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.4MB)
테스트 7 〉	통과 (0.26ms, 10.2MB)
테스트 8 〉	통과 (0.87ms, 10.1MB)
테스트 9 〉	통과 (2.39ms, 10.2MB)
테스트 10 〉	통과 (3.43ms, 10.2MB)
테스트 11 〉	통과 (1.89ms, 10.3MB)
테스트 12 〉	통과 (1.65ms, 10.3MB)
테스트 13 〉	통과 (0.98ms, 10.1MB)
테스트 14 〉	통과 (1.29ms, 10.4MB)
테스트 15 〉	통과 (37.02ms, 11.5MB)
테스트 16 〉	통과 (581.23ms, 11.6MB)
테스트 17 〉	통과 (54.39ms, 11.6MB)
테스트 18 〉	통과 (35.44ms, 11.6MB)
테스트 19 〉	통과 (47.51ms, 11.7MB)
테스트 20 〉	통과 (33.16ms, 11.7MB)
'''