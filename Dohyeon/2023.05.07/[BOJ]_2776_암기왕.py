T = int(input())
for test in range(T):
    total = int(input())
    called_numbers = list(map(int, input().split()))
    guess = int(input())
    guessed_numbers = list(map(int, input().split()))

    called_numbers_set = set(called_numbers)
    for num in guessed_numbers:
        if num in called_numbers_set:
            print(1)
        else:
            print(0)