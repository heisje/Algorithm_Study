N = int(input())
numbers = sorted(list(map(int, input().split())))
answer = 0

for i in range(N):
    number = numbers[i]
    left = 0
    right = N - 1

    while left != right:
        tmp = numbers[left] + numbers[right]
        if tmp == number:
            if i != left and i != right:
                answer += 1
                break
            elif i == left:
                left += 1
            else:
                right -= 1

        elif tmp <= number:
            left += 1
        elif tmp > number:
            right -= 1

print(answer)



