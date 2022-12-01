def solution(m, n, board):
    answer = 0
    four = [(0, 0), (0, 1), (1, 0), (1, 1)]
    board = list(map(list, board))

    while True:
        temp = []
        for r in range(m - 1):  # (m - 1) * (n - 1)를 순회
            for c in range(n - 1):
                if board[r][c] != '-':
                    for d in four:
                        nr, nc = r + d[0], c + d[1]
                        if board[r][c] != board[nr][nc]:  # 같은 모양 2 x 2 4개가 아니면 중단
                            break
                    else:  # 중단되지 않았으면 temp에 사라질 블록 저장
                        for d in four:
                            nr, nc = r + d[0], c + d[1]
                            temp.append((nr, nc))

        if temp:
            temp = set(temp)  # set으로 중복 제거
            answer += len(temp)  # 없어지는 블록 개수 세기
            for r, c in temp:
                board[r][c] = '-'  # 같은 모양의 블록 4개가 붙어있으면 없애기
        else:
            return answer  # 없어질 블록이 없으면 중단

        for c in range(n):  # 각 열을 행 내림차순으로 순회하면서
            for r in range(m, 0, -1):
                if board[r - 1][c] == '-':
                    tr = r - 1
                    while True:
                        if board[tr][c] != '-':
                            board[r - 1][c] = board[tr][c]
                            board[tr][c] = '-'
                            break
                        elif tr == 0:
                            break
                        tr -= 1

# 테스트 1 〉	통과 (0.07ms, 10.5MB)
# 테스트 2 〉	통과 (0.10ms, 10.1MB)
# 테스트 3 〉	통과 (0.02ms, 10.1MB)
# 테스트 4 〉	통과 (4.58ms, 10.3MB)
# 테스트 5 〉	통과 (264.58ms, 10.2MB)
# 테스트 6 〉	통과 (20.90ms, 10.2MB)
# 테스트 7 〉	통과 (2.17ms, 10.2MB)
# 테스트 8 〉	통과 (4.06ms, 10.2MB)
# 테스트 9 〉	통과 (0.04ms, 10.1MB)
# 테스트 10 〉 통과 (1.01ms, 10.3MB)
# 테스트 11 〉 통과 (8.78ms, 10.4MB)
