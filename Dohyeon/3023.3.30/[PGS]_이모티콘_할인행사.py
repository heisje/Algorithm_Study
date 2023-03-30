from itertools import product

def solution(users, emoticons):

    len_emoti = len(emoticons)

    max_sign_in = 0
    max_money = 0
    for sale_list in product([10, 20, 30, 40], repeat=len_emoti):
        temp_sign_in = 0
        temp_money = 0
        for j in range(len(users)):
            temp = 0
            for k in range(len_emoti):
                if users[j][0] <= sale_list[k]:
                    temp += emoticons[k] * (100 - sale_list[k]) * 0.01  # 할인율이 좋으면 할인해서 산다고 생각
            if temp >= users[j][1]:
                temp_sign_in += 1
            else:
                temp_money += temp
        if temp_sign_in > max_sign_in:
            max_sign_in = temp_sign_in
            max_money = temp_money

        elif temp_sign_in == max_sign_in:
            if temp_money > max_money:
                max_money = temp_money

    answer = [max_sign_in, int(max_money)]

    return answer