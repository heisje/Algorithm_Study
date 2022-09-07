import math
import sys

input = lambda : sys.stdin.readline().strip()

min_count = 5

def find_lagran(tg,count):
    if count == 5:
        return False

    global min_count
    if count >= min_count:
        return False
    if tg == 0:
        if count < min_count:
            min_count = count
        else:
            return False

    a = math.floor(math.sqrt(tg))
    for i in range(a, a//2, -1):
        result = find_lagran(tg - i**2, count + 1)
        if result == False:
            continue
    else:
        return False

target = int(input())

find_lagran(target, 0)
print(min_count)



