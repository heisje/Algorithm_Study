from copy import deepcopy


def solution(key, lock):
    N = len(lock)
    M = len(key)
    
    add_in = [1] * (M - 1)                                      # 자물쇠 확장
    add_out = [1] * (2 * M + N - 2)
    exp_lock = [add_out] * (M - 1) + [add_in + l + add_in for l in lock] + [add_out] * (M - 1)
    L = len(exp_lock)
    
    
    def rotate(pre_key):                                        # 시계방향으로 90도 회전하는 함수
        L = len(pre_key)
        rot_key = [[] for _ in range(L)]
        for i in range(L):
            for j in range(L):
                rot_key[i].append(pre_key[L - j - 1][i])
        return rot_key

    
    def check(row, col, now_key, lock_copy):                    # params: 현재 시작 위치, 현재 열쇠의 모양, 확장된 자물쇠의 복사본
        for i in range(M):                                      # return: boolean 자물쇠가 열리는지 여부                   
            for j in range(M):
                lock_copy[i + row][j + col] += now_key[i][j]

        cnt = 0
        for i in range(N):
            for j in range(N):
                now = lock_copy[M - 1 + i][M - 1 + j]
                if now != 1:                                    # 모두 1인 경우만 True
                    return False
        return True
    

    for _ in range(4):                                          # 360도 돌면서 확인
        key = rotate(key)
        for i in range(N + M - 1):
            for j in range(N + M - 1):
                lcopy = deepcopy(exp_lock)
                if check(i, j, key, lcopy):
                    return True           
    return False

"""
테스트 1 〉	통과 (1.83ms, 10.3MB)
테스트 2 〉	통과 (0.14ms, 10.3MB)
테스트 3 〉	통과 (84.70ms, 10.2MB)
테스트 4 〉	통과 (0.53ms, 10.5MB)
테스트 5 〉	통과 (141.89ms, 10.3MB)
테스트 6 〉	통과 (212.49ms, 10.3MB)
테스트 7 〉	통과 (1474.77ms, 10.4MB)
테스트 8 〉	통과 (371.43ms, 10.3MB)
테스트 9 〉	통과 (522.21ms, 10.3MB)
테스트 10 〉 통과 (1026.86ms, 10.4MB)
테스트 11 〉 통과 (2049.34ms, 10.3MB)
테스트 12 〉 통과 (0.06ms, 10.4MB)
테스트 13 〉 통과 (25.09ms, 10.3MB)
테스트 14 〉 통과 (3.71ms, 10.3MB)
테스트 15 〉 통과 (34.04ms, 10.3MB)
테스트 16 〉 통과 (164.81ms, 10.3MB)
테스트 17 〉 통과 (497.00ms, 10.3MB)
테스트 18 〉 통과 (172.58ms, 10.3MB)
테스트 19 〉 통과 (2.68ms, 10.4MB)
테스트 20 〉 통과 (574.69ms, 10.4MB)
테스트 21 〉 통과 (1209.54ms, 10.5MB)
테스트 22 〉 통과 (188.48ms, 10.4MB)
테스트 23 〉 통과 (30.86ms, 10.3MB)
테스트 24 〉 통과 (35.16ms, 10.3MB)
테스트 25 〉 통과 (1200.63ms, 10.4MB)
테스트 26 〉 통과 (1345.04ms, 10.4MB)
테스트 27 〉 통과 (2400.44ms, 10.4MB)
테스트 28 〉 통과 (127.78ms, 10.3MB)
테스트 29 〉 통과 (38.06ms, 10.4MB)
테스트 30 〉 통과 (195.93ms, 10.3MB)
테스트 31 〉 통과 (745.17ms, 10.3MB)
테스트 32 〉 통과 (1368.63ms, 10.3MB)
테스트 33 〉 통과 (240.73ms, 10.3MB)
테스트 34 〉 통과 (13.09ms, 10.3MB)
테스트 35 〉 통과 (13.41ms, 10.5MB)
테스트 36 〉 통과 (18.71ms, 10.5MB)
테스트 37 〉 통과 (10.09ms, 10.3MB)
테스트 38 〉 통과 (5.26ms, 10.2MB)
"""