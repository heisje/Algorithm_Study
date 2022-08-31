import sys
input = lambda : sys.stdin.readline().strip()

def find_point(A, start_num, start_i, start_j, wanted_i, wanted_j):
    # N은 전체 크기, start_num은 가장왼쪽위의 값이 탐색된 순서, start_i, start_j는 이 공간의 행,열 시작 인덱스, wanted는 찾고자 하는 좌표
    if A == 4:
        if start_i == wanted_i:
            if start_j == wanted_j:
                return start_num
            else:
                return start_num + 1
        else:
            if start_j == wanted_j:
                return start_num + 2
            else:
                return start_num + 3

    else:
        quarter = A // 4              # 사분면을 나눈다
        length = int(A ** (1/2))    # 공간의 한 변의 길이

        if start_i + length // 2 > wanted_i:
            if start_j + length // 2 > wanted_j:            # 2사분면
                return find_point(quarter, start_num, start_i, start_j, wanted_i, wanted_j)
            else:                                           # 1사분면
                return find_point(quarter, start_num + 1 * quarter, start_i, start_j + length // 2, wanted_i, wanted_j)
        else:
            if start_j + length // 2 > wanted_j:            # 3사분면
                return find_point(quarter, start_num + 2 * quarter, start_i + length // 2, start_j, wanted_i, wanted_j)
            else:                                           # 4사분면
                return find_point(quarter, start_num + 3 * quarter, start_i + length // 2, start_j + length // 2, wanted_i, wanted_j)


N, i, j = map(int, input().split())
if N == 0:
    print(0)
else:
    print(find_point((2**N) * (2**N), 0, 0, 0, i, j))


