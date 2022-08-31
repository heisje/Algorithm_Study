import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    command_list = input()
    len_of_list = int(input())
    new_list = []
    temp = ""
    if len_of_list == 0:
        a = input()                  # 런타임에러방지
    else:
        input_list = input()
        for i in range(len(input_list)):
            if input_list[i].isdigit():
                temp = temp + input_list[i]
            elif input_list[i] == "," or input_list[i] == "]":
                new_list.append(int(temp))
                temp = ""
    Error_case = False

    skip = False
    state = True
    for i in range(len(command_list)):
        if skip:
            skip = False
            continue
        if command_list[i] == "R":
            if i + 1 < len(command_list) and command_list[i + 1] == "R":
                skip = True
                continue
            else:
                if state:
                    state = False
                else:
                    state = True
        elif command_list[i] == "D":
            try:
                if state:
                    new_list.pop(0)
                else:
                    new_list.pop(-1)
            except IndexError:
                Error_case = True
                break

    if state == False:
        new_list.reverse()

    if Error_case:
        print("error")
        continue

    print("[", end="")
    if len(new_list) == 0:
        print("]")
    for i in range(len(new_list)):
        print(f"{new_list[i]}", end="")
        if i != (len(new_list) - 1):
            print(",", end="")
        else:
            print("]")




