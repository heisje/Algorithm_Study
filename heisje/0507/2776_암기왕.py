T = input()
for _ in range(int(T)):
    N = input()
    note1 = set(input().split())
    M = input()
    note2 = input().split()
    for i in note2:
        if i in note1:
            print(1)
        else:
            print(0)