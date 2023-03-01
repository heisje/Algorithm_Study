def rotate(key):
    n = len(key)
    m = len(key[0])
    new_key = [[0] * n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            new_key[j][n-1-i] = key[i][j]
            
    return new_key


def check(lock):
    n = len(lock) // 3
    for i in range(n, n*2):
        for j in range(n, n*2):
            if lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    
    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] = lock[i][j]
            
    for _ in range(4):
        key = rotate(key)
        
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                        
                if check(new_lock):
                    return True
                
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False


# 테스트 1 〉	통과 (1.24ms, 10.4MB)
# 테스트 2 〉	통과 (0.04ms, 10.3MB)
# 테스트 3 〉	통과 (9.65ms, 10.3MB)
# 테스트 4 〉	통과 (0.03ms, 10.3MB)
# 테스트 5 〉	통과 (32.48ms, 10.3MB)
# 테스트 6 〉	통과 (32.88ms, 10.2MB)
# 테스트 7 〉	통과 (282.93ms, 10.2MB)
# 테스트 8 〉	통과 (64.22ms, 10.3MB)
# 테스트 9 〉	통과 (81.85ms, 10.2MB)
# 테스트 10 〉	통과 (199.55ms, 10.3MB)
# 테스트 11 〉	통과 (376.33ms, 10.3MB)
# 테스트 12 〉	통과 (0.04ms, 10.2MB)
# 테스트 13 〉	통과 (4.26ms, 10.3MB)
# 테스트 14 〉	통과 (1.73ms, 10.2MB)
# 테스트 15 〉	통과 (7.79ms, 10.3MB)
# 테스트 16 〉	통과 (58.04ms, 10.3MB)
# 테스트 17 〉	통과 (102.63ms, 10.3MB)
# 테스트 18 〉	통과 (33.48ms, 10.2MB)
# 테스트 19 〉	통과 (1.02ms, 10.4MB)
# 테스트 20 〉	통과 (178.36ms, 10.3MB)
# 테스트 21 〉	통과 (239.77ms, 10.2MB)
# 테스트 22 〉	통과 (48.97ms, 10.3MB)
# 테스트 23 〉	통과 (5.23ms, 10.3MB)
# 테스트 24 〉	통과 (6.47ms, 10.1MB)
# 테스트 25 〉	통과 (334.67ms, 10.3MB)
# 테스트 26 〉	통과 (484.50ms, 10.3MB)
# 테스트 27 〉	통과 (561.68ms, 10.2MB)
# 테스트 28 〉	통과 (55.53ms, 10.2MB)
# 테스트 29 〉	통과 (11.71ms, 10.3MB)
# 테스트 30 〉	통과 (52.87ms, 10.2MB)
# 테스트 31 〉	통과 (159.08ms, 10.3MB)
# 테스트 32 〉	통과 (303.42ms, 10.4MB)
# 테스트 33 〉	통과 (46.39ms, 10.2MB)
# 테스트 34 〉	통과 (3.00ms, 10.3MB)
# 테스트 35 〉	통과 (3.90ms, 10.4MB)
# 테스트 36 〉	통과 (4.52ms, 10.3MB)
# 테스트 37 〉	통과 (4.51ms, 10.2MB)
# 테스트 38 〉	통과 (1.80ms, 10.4MB)