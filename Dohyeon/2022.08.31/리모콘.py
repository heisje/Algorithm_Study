target = input()
out_of_order = int(input())
if out_of_order != 0:
    broken_list = list(input().split())


def how_many_times(target_ch, out_num, broken):
    if target_ch == "100":
        return 0

    for i in range(len(target_ch)):
        if target_ch[i] in broken:
            break
    else:
        return len(target_ch)

    num_ch = [0]*len(target_ch)
    for i in range(len(target_ch)):
        num_ch[i] = int(target_ch[i])


    we_can = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(len(broken)):
        we_can.remove(int(broken[i]))

    stack_down = []
    stack_up = []

    need_to_up = False
    need_to_down = False
                                                         # 바로 아래숫자를 찾자
    for i in range(len(num_ch) - 1, -1, - 1):            # 1의 자리수 부터 확인한다.
        for j in range(len(we_can)):
            if need_to_down:
                if we_can[j] > num_ch[i]:
                    stack_down.append(we_can[j - 1])
                    if j == 0:
                        break
                    need_to_down = False
                    break
                elif we_can[j] == num_ch[i]:
                    stack_down.append(we_can[j])
                    if i == 0:
                        stack_down.pop()
                    break
            else:
                if we_can[j] > num_ch[i]:
                    stack_down.append(we_can[j - 1])
                    if j == 0:
                        need_to_down = True
                    break
                elif we_can[j] == num_ch[i]:
                    stack_down.append(we_can[j])
                    if i == len(num_ch) - 1:
                        need_to_down = True
                    break

        else:
            stack_down.append(we_can[-1])                   # 앞 자리에서 내려주겠지
            need_to_down = True
            if i == 0:
                stack_down.pop()

    for i in range(len(num_ch) - 1, - 1, - 1):              # 바로 윗숫자를 찾자
        for j in range(len(we_can)):
            if need_to_up:
                if we_can[j] > num_ch[i]:
                    stack_up.append(we_can[j])
                    need_to_up = False
                    break
                elif we_can[j] == num_ch[i]:
                    stack_up.append(we_can[j])
                    if i == 0:
                        stack_up.append(1)
                    break

            else:
                if we_can[j] > num_ch[i]:
                    stack_up.append(we_can[j])
                    break
                elif we_can[j] == num_ch[i]:
                    stack_up.append(we_can[j])
                    if i == len(num_ch) - 1:
                        need_to_up = True
                    break

        else:
            stack_up.append(we_can[0])  # 앞 자리에서 올려주겠지
            need_to_up = True
            if i == 0:
                stack_up.append(1)                        # 제일 앞자리라 더 올릴 수가 없을 경우

    stack_down.reverse()
    stack_up.reverse()

    down_num = 0
    up_num = 0
    for i in range(len(stack_down)):
        down_num += stack_down[i]
        down_num = down_num * 10
    down_num = down_num // 10

    for i in range(len(stack_up)):
        up_num += stack_up[i]
        up_num = up_num * 10
    up_num = up_num // 10

    print(down_num)
    print(up_num)

    return min((up_num - int(target_ch) + len(target_ch)), (int(target_ch) - down_num + len(target_ch)), abs(int(target_ch) - 100))



    


if out_of_order == 0:
    result = 0
else:
    result = how_many_times(target, out_of_order, broken_list)

print(result)




