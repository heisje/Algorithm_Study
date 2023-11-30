def solution(a):
    answer = 0
    min_idx = a.index(min(a))
    
    min_value = float('inf')
    for i in a[:min_idx]:
        if min_value > i:
            answer += 1
            min_value = i
        
    min_value = float('inf')
    for i in reversed(a[min_idx+1:]):
        if min_value > i:
            answer += 1
            min_value = i
        
    return answer + 1

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.05ms, 10.4MB)
# 테스트 4 〉	통과 (6.26ms, 14.2MB)
# 테스트 5 〉	통과 (36.02ms, 32.9MB)
# 테스트 6 〉	통과 (72.43ms, 42.6MB)
# 테스트 7 〉	통과 (106.69ms, 55.5MB)
# 테스트 8 〉	통과 (64.64ms, 53.3MB)
# 테스트 9 〉	통과 (63.78ms, 53.3MB)
# 테스트 10 〉	통과 (64.40ms, 53.4MB)
# 테스트 11 〉	통과 (84.88ms, 53.4MB)
# 테스트 12 〉	통과 (83.60ms, 53.5MB)
# 테스트 13 〉	통과 (76.48ms, 53.5MB)
# 테스트 14 〉	통과 (84.12ms, 53.2MB)
# 테스트 15 〉	통과 (85.25ms, 53.2MB)