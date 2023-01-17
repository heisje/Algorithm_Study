def solution(triangle):
    for arr_idx, arr in enumerate(triangle):
        if arr_idx == 0:
            continue
        for idx, i in enumerate(arr):
            prev = triangle[arr_idx-1]
            left = prev[idx-1] if idx - 1 >= 0 else 0
            right = prev[idx] if idx < len(prev) else 0
            triangle[arr_idx][idx] = i + max(left, right)
    return max(triangle[-1])


# 정확성 테스트
# 테스트 1 〉	통과 (0.02ms, 10.1MB)
# 테스트 2 〉	통과 (0.05ms, 10.3MB)
# 테스트 3 〉	통과 (0.11ms, 10.2MB)
# 테스트 4 〉	통과 (0.34ms, 10.3MB)
# 테스트 5 〉	통과 (1.15ms, 10.2MB)
# 테스트 6 〉	통과 (0.35ms, 10.3MB)
# 테스트 7 〉	통과 (1.33ms, 10.4MB)
# 테스트 8 〉	통과 (0.26ms, 10.2MB)
# 테스트 9 〉	통과 (0.02ms, 10.2MB)
# 테스트 10 〉	통과 (0.27ms, 10.3MB)

# 효율성  테스트
# 테스트 1 〉	통과 (40.06ms, 14.1MB)
# 테스트 2 〉	통과 (30.84ms, 13.2MB)
# 테스트 3 〉	통과 (45.20ms, 14.7MB)
# 테스트 4 〉	통과 (40.81ms, 14.1MB)
# 테스트 5 〉	통과 (37.70ms, 13.9MB)
# 테스트 6 〉	통과 (47.49ms, 14.6MB)
# 테스트 7 〉	통과 (43.92ms, 14.4MB)
# 테스트 8 〉	통과 (36.11ms, 13.6MB)
# 테스트 9 〉	통과 (37.46ms, 13.9MB)
# 테스트 10 〉	통과 (43.60ms, 14.4MB)