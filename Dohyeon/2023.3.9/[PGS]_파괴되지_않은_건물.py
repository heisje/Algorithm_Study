def solution(board, skill):

    for i in range(len(skill)):
        type_of_skill = skill[i][0]
        start_i = skill[i][1]
        start_j = skill[i][2]
        end_i = skill[i][3]
        end_j = skill[i][4]
        dmg = skill[i][5]

        for j in range(start_i, end_i + 1):
            for k in range(start_j, end_j + 1):
                if type_of_skill == 1:
                    board[j][k] -= dmg
                else:
                    board[j][k] += dmg
    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                count += 1
    answer = count
    return answer
