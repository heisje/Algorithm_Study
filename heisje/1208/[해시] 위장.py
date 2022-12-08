# https://school.programmers.co.kr/learn/courses/30/lessons/42578
from collections import defaultdict

def solution(clothes):
    # 옷 구하기
    clothes_dict = defaultdict(list)
    for clothe in clothes:
        clothes_dict[clothe[1]].append(clothe[0])

    # 개수 구하기
    clothes_number = list()
    for key, value in clothes_dict.items():
        clothes_number.append(len(value)+1)

    # 누적곱
    answer = clothes_number[0]
    for idx in range(1, len(clothes_number)):
        answer = answer * clothes_number[idx]
    return answer - 1

a = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(a)
a = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
solution(a)

# 테스트 1 〉	통과 (0.03ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.02ms, 10.2MB)
# 테스트 4 〉	통과 (0.02ms, 10.2MB)
# 테스트 5 〉	통과 (0.02ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.03ms, 10.2MB)
# 테스트 8 〉	통과 (0.02ms, 10.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.3MB)
# 테스트 10 〉	통과 (0.01ms, 10.3MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (0.02ms, 10.3MB)
# 테스트 13 〉	통과 (0.02ms, 10.3MB)
# 테스트 14 〉	통과 (0.01ms, 10.2MB)
# 테스트 15 〉	통과 (0.01ms, 10.3MB)
# 테스트 16 〉	통과 (0.01ms, 10.1MB)
# 테스트 17 〉	통과 (0.01ms, 10.3MB)
# 테스트 18 〉	통과 (0.01ms, 10.2MB)
# 테스트 19 〉	통과 (0.01ms, 10.3MB)
# 테스트 20 〉	통과 (0.01ms, 10.3MB)
# 테스트 21 〉	통과 (0.01ms, 10.3MB)
# 테스트 22 〉	통과 (0.01ms, 10.3MB)
# 테스트 23 〉	통과 (0.01ms, 10.3MB)
# 테스트 24 〉	통과 (0.01ms, 10.3MB)
# 테스트 25 〉	통과 (0.02ms, 10.2MB)
# 테스트 26 〉	통과 (0.03ms, 10.3MB)
# 테스트 27 〉	통과 (0.01ms, 10.2MB)
# 테스트 28 〉	통과 (0.01ms, 10.2MB)