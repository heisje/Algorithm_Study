import math
import sys
from itertools import combinations_with_replacement

input = lambda : sys.stdin.readline().strip()

# 우리는 어차피 4개로 이루어 진다는 사실을 안다.
# 코드 참조 https://www.acmicpc.net/source/48349027

target = int(input())

square_num_li = [i*i for i in range(1, int(math.floor(math.sqrt(target)))+1)]
square_num_li_2 = [sum(k) for k in combinations_with_replacement(square_num_li, 2)]


def find_answer(tg):
    if tg in square_num_li:
        print(1)
        return

    elif tg in square_num_li_2:
        print(2)
        return

    else:
        for i in square_num_li_2:
            temp = tg - i
            if temp in square_num_li:
                print(3)
                return
    print(4)
    return


find_answer(target)