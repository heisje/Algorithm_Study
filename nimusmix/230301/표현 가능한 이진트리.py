def check(binary, parent):
    if parent == '0':
        if not all(child == '0' for child in binary):
            return False
    if len(binary) == 1:
        return True
    
    m = len(binary) // 2
    return check(binary[:m], binary[m]) and check(binary[m+1:], binary[m])


def solution(numbers):
    answer = []
    
    for number in numbers:
        binary = bin(number)[2:]
        digit = 0
        
        for i in range(51):
            digit = 2 ** i - 1
            if digit >= len(binary):
                break
            
        binary = '0' * (digit - len(binary)) + binary
        answer.append(1 if check(binary, binary[len(binary) // 2]) else 0)
    
    return answer


# 테스트 1 〉	통과 (0.02ms, 10.1MB)
# 테스트 2 〉	통과 (0.05ms, 10.2MB)
# 테스트 3 〉	통과 (0.05ms, 10.4MB)
# 테스트 4 〉	통과 (0.33ms, 9.99MB)
# 테스트 5 〉	통과 (0.69ms, 10.3MB)
# 테스트 6 〉	통과 (0.88ms, 10.2MB)
# 테스트 7 〉	통과 (1.01ms, 10.3MB)
# 테스트 8 〉	통과 (0.52ms, 10.4MB)
# 테스트 9 〉	통과 (4.86ms, 10.3MB)
# 테스트 10 〉	통과 (42.52ms, 11MB)
# 테스트 11 〉	통과 (46.81ms, 11.4MB)
# 테스트 12 〉	통과 (62.09ms, 11MB)
# 테스트 13 〉	통과 (51.03ms, 10.8MB)
# 테스트 14 〉	통과 (61.84ms, 11MB)
# 테스트 15 〉	통과 (31.99ms, 10.6MB)
# 테스트 16 〉	통과 (106.20ms, 11.4MB)
# 테스트 17 〉	통과 (134.43ms, 11.1MB)
# 테스트 18 〉	통과 (87.63ms, 11MB)
# 테스트 19 〉	통과 (157.97ms, 10.9MB)
# 테스트 20 〉	통과 (72.28ms, 10.6MB)