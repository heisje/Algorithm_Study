import sys

switches = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
number = int(sys.stdin.readline())

for _ in range(number):
    student = list(map(int, sys.stdin.readline().split()))

    if student[0] == 1:
        idx = student[1] * 1
        multi = 2
        while True:
            if idx > switches:
                break
            s[idx - 1] = 0 if s[idx - 1] == 1 else 1
            idx = student[1] * multi
            multi += 1

    else:
        idx = student[1] - 1
        i_arr = [idx]
        n = 0
        while True:
            n += 1
            if idx - n < 0 or idx + n > switches - 1:
                break
            if s[idx - n] != s[idx + n]:
                break
            i_arr += [idx - n, idx + n] 
        for i in i_arr:
            s[i] = 0 if s[i] == 1 else 1

for i in range(0, switches):
    print(s[i], end=' ')
    if (i + 1) % 20 == 0:
        print()
