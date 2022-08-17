import sys

input = sys.stdin.readline

my_board = []                                           # 나의 빙고판
call_number = []                                        # 사회자가 부른 숫자 1차원 배열
my_board_for_search = []                                # 사회자가 부른 숫자 검색용 1차원 배열

for i in range(5):
    my_board.append(list(map(int, input().split())))
    for j in range(5):
        my_board_for_search.append(my_board[i][j])
for i in range(5):
    a = list(map(int, input().split()))
    for j in range(5):
        call_number.append(a[j])


call_count = 0                                          # 나중에 print할 사회자가 몇 번째 숫자를 불렀는지 카운트
for i in range(len(call_number)):
    bingo = 0
    for j in range(len(my_board_for_search)):
        if my_board_for_search[j] == call_number[i]:    # 사회자가 부르는 숫자가 나의 빙고판에서는 몇번째 인덱스인지 확인하는 과정
            idx = j
            break

    call_count += 1

    pos_i = idx // 5                                    # 행 좌표를 알 수 있다.
    pos_j = idx % 5                                     # 열 좌표를 알 수 있다.

    my_board[pos_i][pos_j] = 'a'                    # 불려진 숫자는 'a'로 바꾸어 체크한다.

    if i >= 11:                                     # 3빙고가 나는 최소 조건이다. 이 이상은 되야 3빙고가 난다.
        for row in range(5):                          # 가로 빙고가 있는지 확인
            if my_board[row].count('a') == 5:
                bingo += 1

        for col in range(5):                          # 세로 빙고가 있는지 확인
            count = 0
            for row in range(5):
                if my_board[row][col] == 'a':
                    count += 1
            if count == 5:
                bingo += 1

        count = 0
        for cross in range(5):                        # 왼쪽 위, 오른쪽 아래 대각선 빙고가 있는지 확인
            if my_board[cross][cross] == 'a':
                count += 1
        if count == 5:
            bingo += 1
        count = 0
        for cross in range(5):                        # 오른쪽 위, 왼쪽 아래 대각선 빙고가 있는지 확인
            if my_board[cross][4 - cross] == 'a':
                count += 1
        if count == 5:
            bingo += 1
        count = 0

    if bingo >= 3:                                    # 갑자기 3개가 넘는 빙고가 날 수도 있으니 3개 이상으로 표현
        break
print(call_count)



