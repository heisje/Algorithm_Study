from itertools import combinations

def solution(orders, course):

    answer = []
    for num_of_menu in course:
        maximum = 0
        counting_dict = {}
        mini_result = []
        for i in range(len(orders)):
            if len(orders[i]) >= num_of_menu:
                orders_list = list(orders[i])
                orders_list.sort()
                temp = list(combinations(orders_list, num_of_menu))

                for comb in temp:
                    tmp_str = ''.join(comb)

                    try:
                        check = counting_dict[tmp_str]

                    except KeyError:
                        counting_dict[tmp_str] = 0
                        temp_count = 0
                        for j in range(len(orders)):
                            for k in range(len(tmp_str)):
                                if tmp_str[k] not in orders[j]:
                                    break
                            else:
                                temp_count += 1

                            if temp_count + len(orders) - j - 1 < maximum:
                                break

                        else:
                            if temp_count < 2:
                                continue
                            if temp_count > maximum:
                                maximum = temp_count
                                mini_result.clear()
                                mini_result.append(tmp_str)

                            elif temp_count == maximum:
                                mini_result.append(tmp_str)
                            else:
                                print("오류")
        answer.extend(mini_result)
    answer.sort()
    return answer


result = solution(["XYZ", "XWY", "WXA"], [2,3,4])
print(result)

"""
테스트 1 〉	통과 (0.33ms, 10.3MB)
테스트 2 〉	통과 (0.19ms, 10.4MB)
테스트 3 〉	통과 (0.23ms, 10.2MB)
테스트 4 〉	통과 (0.48ms, 10.3MB)
테스트 5 〉	통과 (0.56ms, 10.3MB)
테스트 6 〉	통과 (1.44ms, 10.2MB)
테스트 7 〉	통과 (1.45ms, 10.3MB)
테스트 8 〉	통과 (8.04ms, 10.4MB)
테스트 9 〉	통과 (10.91ms, 10.2MB)
테스트 10 〉	통과 (26.82ms, 10.6MB)
테스트 11 〉	통과 (13.75ms, 10.3MB)
테스트 12 〉	통과 (18.64ms, 10.3MB)
테스트 13 〉	통과 (23.53ms, 10.4MB)
테스트 14 〉	통과 (18.27ms, 10.4MB)
테스트 15 〉	통과 (25.41ms, 10.4MB)
테스트 16 〉	통과 (6.22ms, 10.4MB)
테스트 17 〉	통과 (3.46ms, 10.4MB)
테스트 18 〉	통과 (1.27ms, 10.3MB)
테스트 19 〉	통과 (0.17ms, 10.2MB)
테스트 20 〉	통과 (3.28ms, 10.2MB)
"""