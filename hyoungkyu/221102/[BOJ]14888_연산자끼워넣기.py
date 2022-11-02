# 실버1 / 620ms
import itertools
import sys
input = lambda:sys.stdin.readline().strip()

N = int(input())
numbers = list(map(int, input().split()))
operator = list(map(int, input().split()))      # +, -, *, /
oper = ['+', '-', '*', '//']
operator_ = []

for i in range(4):
    for _ in range(operator[i]):
        operator_.append(oper[i])

maxV = -1000000000
minV = 1000000000
operator_set = list(set(itertools.permutations(operator_)))
for i in operator_set:
    # print(i)
    tot = numbers[0]
    # print(tot)
    for j in range(1, N):
        if i[j-1] == '+':
            tot += numbers[j]
        elif i[j-1] == '-':
            tot -= numbers[j]
        elif i[j-1] == '*':
            tot *= numbers[j]
        elif i[j-1] == '//':
            if tot < 0:
                tot = -((tot)*(-1) // numbers[j]) 
            else:
                tot //= numbers[j]
    # print(tot)

        # s = str(tot) + i[j-1] + str(numbers[j])
        # if i[j-1] == '//' and tot < 0:
        #     s = '-(' + str(-tot) + i[j-1] + str(numbers[j]) + ')'
        # tot = int(eval(s))
    if maxV < tot:
        maxV = tot
    if minV > tot:
        minV = tot
print(maxV)
print(minV)
