def solution(triangle):
    answer = 0

    for row in range(len(triangle)):
        if row == 0:
            continue
        for col in range(len(triangle[row])):
            if col == 0:
                triangle[row][col] += triangle[row - 1][col]
            elif col == len(triangle[row]) - 1:
                triangle[row][col] += triangle[row - 1][col - 1]
            else:
                if triangle[row - 1][col - 1] >= triangle[row - 1][col]:
                    triangle[row][col] += triangle[row - 1][col - 1]
                else:
                    triangle[row][col] += triangle[row - 1][col]

    answer = max(triangle[len(triangle)-1])
    return answer


print(solution([[7],
                [3, 8],
                [8, 1, 0],
                [2, 7, 4, 4],
                [4, 5, 2, 6, 5]]))

"""
테스트 1 〉	통과 (0.02ms, 10.4MB)
테스트 2 〉	통과 (0.02ms, 10.1MB)
테스트 3 〉	통과 (0.06ms, 10.2MB)
테스트 4 〉	통과 (0.16ms, 10.3MB)
테스트 5 〉	통과 (1.56ms, 10.4MB)
테스트 6 〉	통과 (0.31ms, 10.1MB)
테스트 7 〉	통과 (1.56ms, 10.3MB)
테스트 8 〉	통과 (0.56ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.15ms, 10MB)
효율성  테스트
테스트 1 〉	통과 (39.71ms, 14MB)
테스트 2 〉	통과 (30.62ms, 13.1MB)
테스트 3 〉	통과 (41.36ms, 14.7MB)
테스트 4 〉	통과 (41.62ms, 13.9MB)
테스트 5 〉	통과 (37.28ms, 14MB)
테스트 6 〉	통과 (46.68ms, 14.7MB)
테스트 7 〉	통과 (43.31ms, 14.5MB)
테스트 8 〉	통과 (35.04ms, 13.7MB)
테스트 9 〉	통과 (37.70ms, 13.7MB)
테스트 10 〉	통과 (40.24ms, 14.4MB)
"""