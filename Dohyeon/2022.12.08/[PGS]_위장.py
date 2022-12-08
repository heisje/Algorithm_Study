def solution(clothes):
    answer = 0
    clothes_dict = {}

    for i in range(len(clothes)):
        try:
            clothes_dict[clothes[i][1]] += 1
        except KeyError:
            clothes_dict[clothes[i][1]] = 1
    dict_key_list = list(clothes_dict.keys())
    print(clothes_dict)
    tmp = 1
    for i in range(len(dict_key_list)):
        tmp = tmp * (clothes_dict[dict_key_list[i]] + 1)
    answer += tmp

    answer -= 1
    return answer


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))

"""
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.3MB)
테스트 13 〉	통과 (0.02ms, 10.1MB)
테스트 14 〉	통과 (0.01ms, 10.1MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.3MB)
테스트 17 〉	통과 (0.01ms, 10.1MB)
테스트 18 〉	통과 (0.02ms, 10.3MB)
테스트 19 〉	통과 (0.02ms, 10.3MB)
테스트 20 〉	통과 (0.01ms, 10.2MB)
테스트 21 〉	통과 (0.01ms, 10.1MB)
테스트 22 〉	통과 (0.01ms, 10.3MB)
테스트 23 〉	통과 (0.02ms, 10.3MB)
테스트 24 〉	통과 (0.02ms, 10.2MB)
테스트 25 〉	통과 (0.02ms, 10.1MB)
테스트 26 〉	통과 (0.02ms, 10.2MB)
테스트 27 〉	통과 (0.01ms, 10.3MB)
테스트 28 〉	통과 (0.02ms, 10.2MB)
"""