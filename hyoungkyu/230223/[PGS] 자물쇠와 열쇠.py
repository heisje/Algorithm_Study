# Lv3
# key를 오른쪽으로 돌리기
def rotate_key(key):
    res = []
    for j in range(len(key)):
        tmp = []
        for i in range(len(key)-1, -1, -1):
            tmp.append(key[i][j])
        res.append(tmp[:])
    return res

# 자물쇠 풀기 시도 
# (자물쇠 해당 위치 == key의 오른쪽 밑) => key의 크기만큼 다 돌림
def unlock(i, j, key, lock):
    key_i, cnt = 0, 0
    for ti in range(i-len(key)+1, i+1):
        key_j = 0
        for tj in range(j-len(key)+1, j+1):
            # 홈을 채우면 카운트 +1
            if 0<=ti<len(lock) and 0<=tj<len(lock) and lock[ti][tj] == 0 and key[key_i][key_j] == 1:
                cnt += 1
            # 홈이 아닌데 key의 홈이 닿으면 ㅈㅈ
            elif 0<=ti<len(lock) and 0<=tj<len(lock) and lock[ti][tj] == 1 and key[key_i][key_j] == 1:
                return 0
            key_j += 1
        key_i += 1
    return cnt

def solution(key, lock):
    answer = False
    zeros = 0
    # 자물쇠의 홈 부분 개수 세기
    for i in range(len(lock)):
        for j in range(len(lock)):
            if not lock[i][j]:
                zeros += 1
    
    # key 모양 4번 * 자물쇠 전체 크기
    for _ in range(4):
        for i in range(len(lock)+len(key)-1):
            for j in range(len(lock)+len(key)-1):
                if zeros == unlock(i, j, key, lock):
                    return True
                
        key = rotate_key(key)
    
    return answer

'''
0 0 0       0 1 0       1 1 0       0 0 1
1 0 0   >   1 0 0   >   0 0 1   >   0 0 1
0 1 1       1 0 0       0 0 0       0 1 0
'''

'''
테스트 1 〉	통과 (0.67ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.1MB)
테스트 3 〉	통과 (3.38ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (6.38ms, 10.2MB)
테스트 6 〉	통과 (2.99ms, 10.1MB)
테스트 7 〉	통과 (2.67ms, 10.3MB)
테스트 8 〉	통과 (13.43ms, 10.1MB)
테스트 9 〉	통과 (17.30ms, 10.4MB)
테스트 10 〉	통과 (38.42ms, 10.2MB)
테스트 11 〉	통과 (45.54ms, 10.3MB)
테스트 12 〉	통과 (0.02ms, 10.4MB)
테스트 13 〉	통과 (2.28ms, 10.2MB)
테스트 14 〉	통과 (1.06ms, 10.2MB)
테스트 15 〉	통과 (0.75ms, 10.3MB)
테스트 16 〉	통과 (7.80ms, 10.2MB)
테스트 17 〉	통과 (0.64ms, 10.2MB)
테스트 18 〉	통과 (3.26ms, 10.4MB)
테스트 19 〉	통과 (0.29ms, 10.2MB)
테스트 20 〉	통과 (14.00ms, 10.1MB)
테스트 21 〉	통과 (7.03ms, 10.1MB)
테스트 22 〉	통과 (9.27ms, 10.2MB)
테스트 23 〉	통과 (1.04ms, 10.3MB)
테스트 24 〉	통과 (2.70ms, 10.2MB)
테스트 25 〉	통과 (22.62ms, 10.1MB)
테스트 26 〉	통과 (31.23ms, 10.4MB)
* 테스트 27 〉	통과 (51.52ms, 10.3MB)
테스트 28 〉	통과 (5.41ms, 10.2MB)
테스트 29 〉	통과 (2.06ms, 10.2MB)
테스트 30 〉	통과 (7.56ms, 10.1MB)
테스트 31 〉	통과 (12.79ms, 10.4MB)
테스트 32 〉	통과 (22.93ms, 10.4MB)
테스트 33 〉	통과 (9.38ms, 10.2MB)
테스트 34 〉	통과 (0.19ms, 10.3MB)
테스트 35 〉	통과 (0.96ms, 10.3MB)
테스트 36 〉	통과 (1.75ms, 10.3MB)
테스트 37 〉	통과 (1.17ms, 10.3MB)
테스트 38 〉	통과 (0.24ms, 10.2MB)
'''