import sys
input = sys.stdin.readline

testcase = int(input())
for tc in range(testcase):
    N = int(input())

    max_num = 0
    min_num = 0
    que = []

    for i in range(N):
        order, a = input().split()
        num = int(a)

        if order == "I":
            que.append(num)
            if len(que) == 1:
                max_num = num
                min_num = num
            else:
                if num > max_num:
                    max_num = num
                if num < min_num:
                    min_num = num
        else:
            if num == -1:
                try:
                    que.remove(min_num)
                    min_num = min(que)
                except:
                    pass
            else:
                try:
                    que.remove(max_num)
                    max_num = max(que)
                except:
                    pass
    if len(que) == 0:
        print("EMPTY")
    else:
        print(max_num, min_num)

