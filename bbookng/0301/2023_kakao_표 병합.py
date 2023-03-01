from pprint import pprint

def update(r, c, nr, nc, table):
    for i in range(1, 51):
        for j in range(1, 51):
            # 머지 당하는 셀과 부모가 같으면 모두 병합해줘야함
            if table[i][j][1] == table[r][c][1]:
                # 머지 하는 쪽 셀 내용으로 수정
                table[i][j] = [table[nr][nc][0], table[nr][nc][1]]

def solution(commands):
    answer = []
    table = [[['', [r, c]] for c in range(51)] for r in range(51)]

    for command in commands:
        command = command.split()
        command, value = command[0], command[1:]

        # 셀 위치를 선택해 update 할 때
        if command == 'UPDATE' and len(value) == 3:
            r, c, value = int(value[0]), int(value[1]), value[2]
            nr, nc = table[r][c][1]
            for i in range(1, 51):
                for j in range(1, 51):
                    if table[i][j][1] == [nr, nc]:
                        table[i][j][0] = value

        # 셀 value 를 선택해 value2로 바꿀 때
        elif command == 'UPDATE' and len(value) == 2:
            value1, value2 = value[0], value[1]
            for i in range(1, 51):
                for j in range(1, 51):
                    if table[i][j][0] == value1:
                        table[i][j][0] = value2

        # merge 할 때
        elif command == 'MERGE':
            r1, c1, r2, c2 = int(value[0]), int(value[1]), int(value[2]), int(value[3])
            # 같은 위치면 무시
            if r1 == r2 and c1 == c2:
                continue
            if table[r1][c1][0] != '' and table[r2][c2][0] != '':
                update(r2, c2, r1, c1, table)
            elif table[r1][c1][0] == '' and table[r2][c2][0] != '':
                update(r1, c1, r2, c2, table)
            elif table[r1][c1][0] != '' and table[r2][c2][0] == '':
                update(r2, c2, r1, c1, table)
            else:
                update(r2, c2, r1, c1, table)

        elif command == 'UNMERGE':
            r, c = int(value[0]), int(value[1])
            nr, nc = table[r][c][1]
            tmp = []
            for i in range(1, 51):
                for j in range(1, 51):
                    # 선택한 셀일 경우는 값 그대로
                    if i == r and j == c:
                        table[i][j] = [table[i][j][0], [i, j]]
                    # 아니면 수정할거니까 병합되어 있는 셀들의 좌표를 리스트에 추가
                    elif [nr, nc] == table[i][j][1]:
                        tmp.append([i, j])

            # 값 초기화
            for i, j in tmp:
                table[i][j] = ['', [i, j]]

        elif command == 'PRINT':
            r, c = int(value[0]), int(value[1])
            if table[r][c][0] == '':
                answer.append("EMPTY")
            else:
                answer.append(table[r][c][0])

    return answer

print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))
