def solution(key, lock):
    # 90도 회전
    def rotate(array):
        return list(zip(*array))[::-1]

    # 체크하기
    def check(x, y, start, end):
        arr = [[0] * size for _ in range(size)]

        for i in range(M):
            for j in range(M):
                arr[x + i][y + j] += key[i][j]

        for i in range(start, end + 1):
            for j in range(start, end + 1):
                arr[i][j] += lock[i - start][j - start]
                if arr[i][j] != 1:
                    return False

        return True

    M = len(key)
    N = len(lock)

    start = M - 1
    end = M + N - 2

    size = N + 2 * M - 2

    for _ in range(4):
        for i in range(end + 1):
            for j in range(end + 1):
                if check(i, j, start, end):
                    return True
        key = rotate(key)

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

'''
테스트 1 〉	통과 (0.82ms, 10.2MB)
테스트 2 〉	통과 (0.07ms, 10.3MB)
테스트 3 〉	통과 (55.28ms, 10.1MB)
테스트 4 〉	통과 (0.03ms, 10.2MB)
테스트 5 〉	통과 (7.60ms, 10.2MB)
테스트 6 〉	통과 (10.60ms, 10.3MB)
테스트 7 〉	통과 (24.66ms, 10.2MB)
테스트 8 〉	통과 (236.27ms, 10.2MB)
테스트 9 〉	통과 (120.87ms, 10.3MB)
테스트 10 〉	통과 (239.44ms, 10.4MB)
테스트 11 〉	통과 (129.85ms, 10.2MB)
테스트 12 〉	통과 (0.03ms, 10.2MB)
테스트 13 〉	통과 (16.38ms, 10.3MB)
테스트 14 〉	통과 (4.54ms, 10.4MB)
테스트 15 〉	통과 (7.66ms, 10.4MB)
테스트 16 〉	통과 (16.43ms, 10.2MB)
테스트 17 〉	통과 (0.93ms, 10.4MB)
테스트 18 〉	통과 (85.00ms, 10.3MB)
테스트 19 〉	통과 (1.12ms, 10.2MB)
테스트 20 〉	통과 (108.72ms, 10.2MB)
테스트 21 〉	통과 (10.34ms, 10.3MB)
테스트 22 〉	통과 (11.22ms, 10.2MB)
테스트 23 〉	통과 (2.98ms, 10.4MB)
테스트 24 〉	통과 (3.25ms, 10.3MB)
테스트 25 〉	통과 (140.77ms, 10.2MB)
테스트 26 〉	통과 (166.33ms, 10.2MB)
테스트 27 〉	통과 (309.28ms, 10.2MB)
테스트 28 〉	통과 (19.06ms, 10.3MB)
테스트 29 〉	통과 (5.80ms, 10.2MB)
테스트 30 〉	통과 (48.18ms, 10.4MB)
테스트 31 〉	통과 (71.22ms, 10.3MB)
테스트 32 〉	통과 (134.84ms, 10.4MB)
테스트 33 〉	통과 (35.70ms, 10.4MB)
테스트 34 〉	통과 (0.31ms, 10.2MB)
테스트 35 〉	통과 (1.93ms, 10.2MB)
테스트 36 〉	통과 (2.81ms, 10.4MB)
테스트 37 〉	통과 (4.82ms, 10.4MB)
테스트 38 〉	통과 (0.35ms, 10.3MB)
'''