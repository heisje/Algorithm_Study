def solution(rows, columns, queries):
    answer = []
    board = [[i + j * columns for i in range(1, columns+1)] for j in range(rows)]

    for r1, c1, r2, c2 in queries:
        r, c = r1 - 1, c1 - 1

        numbers = [board[r][c]]
        change = board[r][c]

        # 윗 변
        for i in range(c2-c1):
            c += 1
            tmp = board[r][c]
            numbers.append(tmp)
            board[r][c] = change
            change = tmp

        # 오른쪽 변
        for i in range(r2-r1):
            r += 1
            tmp = board[r][c]
            numbers.append(tmp)
            board[r][c] = change
            change = tmp

        # 아래 변
        for i in range(c2-c1):
            c -= 1
            tmp = board[r][c]
            numbers.append(tmp)
            board[r][c] = change
            change = tmp

        # 왼쪽 변
        for i in range(r2-r1):
            r -= 1
            tmp = board[r][c]
            numbers.append(tmp)
            board[r][c] = change
            change = tmp

        answer.append(min(numbers))

    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))


'''
테스트 1 〉	통과 (0.04ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (165.31ms, 11.7MB)
테스트 4 〉	통과 (98.82ms, 11.1MB)
테스트 5 〉	통과 (212.08ms, 11.4MB)
테스트 6 〉	통과 (162.29ms, 11.9MB)
테스트 7 〉	통과 (169.20ms, 12.1MB)
테스트 8 〉	통과 (128.72ms, 11.2MB)
테스트 9 〉	통과 (184.87ms, 11.6MB)
테스트 10 〉	통과 (151.46ms, 11.5MB)
테스트 11 〉	통과 (117.01ms, 11.3MB)
'''