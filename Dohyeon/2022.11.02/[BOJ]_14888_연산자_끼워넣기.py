from itertools import combinations


N = int(input())
nums = list(map(int, input().split()))
calc = list(map(int, input().split()))

num_list = list(range(N - 1))
max_val = -100000000
min_val = 100000000

plus = list(combinations(num_list, calc[0]))

for plus_list in plus:
    plus_list = list(plus_list)
    expression = ['/'] * (N - 1)
    for i in plus_list:
        expression[i] = '+'
    new_num_list1 = list(set(num_list) - set(plus_list))

    plus_minus = list(combinations(new_num_list1, calc[1]))

    for minus_list in plus_minus:
        minus_list = list(minus_list)
        for j in minus_list:
            expression[j] = '-'
        new_num_list2 = list(set(new_num_list1) - set(minus_list))

        plus_minus_multiply = list(combinations(new_num_list2, calc[2]))

        for multiply in plus_minus_multiply:
            multiply = list(multiply)
            for k in multiply:
                expression[k] = '*'

            for f in range(N - 1):

                if expression[f] == "*":
                    if f == 0:
                        result = nums[f] * nums[f+1]
                    else:
                        result = result * nums[f+1]
                elif expression[f] == "+":
                    if f == 0:
                        result = nums[f] + nums[f+1]
                    else:
                        result = result + nums[f + 1]
                elif expression[f] == "-":
                    if f == 0:
                        result = nums[f] - nums[f+1]
                    else:
                        result = result - nums[f + 1]
                elif expression[f] == "/":
                    if f == 0:
                        result = int(nums[f] / nums[f+1])
                    else:
                        result = int(result / nums[f + 1])


            if result > max_val:
                max_val = result
                #print("max!")
                #print(expression)
            if result < min_val:
                min_val = result
                #print("min!")
                #print(expression)

            for k in multiply:
                expression[k] = '/'
        for j in minus_list:
            expression[j] = '/'
print(max_val)
print(min_val)
