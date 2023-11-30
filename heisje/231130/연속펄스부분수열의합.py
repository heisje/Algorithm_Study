#  0 1  2 3  4 5
# -1 1 -1 1 -1 1
#  1-1  1-1  1-1

def solution(sequence):
    save = []
    parse = -1
    
    save.append(sequence[0])
    
    for idx, s in enumerate(sequence[1:]):
        save.append(save[idx] + s * parse)
        parse *= -1
    
    mini = min(save)
    maxi = max(save)
    
    if mini >= 0 and maxi >= 0:
        return maxi
    if mini < 0 and maxi < 0:
        return -mini
    return abs(maxi) + abs(mini)
    
#     테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.00ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10MB)
# 테스트 6 〉	통과 (0.01ms, 10.1MB)
# 테스트 7 〉	통과 (0.01ms, 10.3MB)
# 테스트 8 〉	통과 (0.17ms, 10.1MB)
# 테스트 9 〉	통과 (0.19ms, 10.2MB)
# 테스트 10 〉	통과 (1.05ms, 10.5MB)
# 테스트 11 〉	통과 (2.14ms, 10.8MB)
# 테스트 12 〉	통과 (25.86ms, 18.7MB)
# 테스트 13 〉	통과 (30.70ms, 18.7MB)
# 테스트 14 〉	통과 (21.84ms, 18.9MB)
# 테스트 15 〉	통과 (22.20ms, 18.6MB)
# 테스트 16 〉	통과 (23.04ms, 19.8MB)
# 테스트 17 〉	통과 (111.54ms, 54.1MB)
# 테스트 18 〉	통과 (110.67ms, 55.9MB)
# 테스트 19 〉	통과 (127.98ms, 62.6MB)
# 테스트 20 〉	통과 (113.63ms, 62.4MB)