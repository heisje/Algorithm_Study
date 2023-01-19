# Lv3
def solution(triangle):
    answer = 0
    answer_lst = [triangle[0]]
    # [7], [10, 15], [18, 16, 15], ...
    for i in range(1, len(triangle)):
        tmp = [0] * (i+1)
        for j in range(len(triangle[i-1])):
            tmp[j] = max(tmp[j], answer_lst[i-1][j]+triangle[i][j])
            tmp[j+1] = max(tmp[j+1], answer_lst[i-1][j]+triangle[i][j+1])
        answer_lst.append(tmp)
    # print(answer_lst)
    answer = max(answer_lst[-1])
    return answer

'''
정확성 테스트
테스트 1 〉통과 (0.02ms, 10.2MB)
테스트 2 〉통과 (0.04ms, 10.2MB)
테스트 3 〉통과 (0.12ms, 10.2MB)
테스트 4 〉통과 (0.25ms, 10.3MB)
테스트 5 〉통과 (3.65ms, 10.3MB)    *
테스트 6 〉통과 (0.56ms, 10.2MB)
테스트 7 〉통과 (1.97ms, 10.4MB)
테스트 8 〉통과 (0.49ms, 10.2MB)
테스트 9 〉통과 (0.02ms, 10.1MB)
테스트 10 〉통과 (0.25ms, 10.3MB)
효율성 테스트
테스트 1 〉통과 (62.72ms, 17.9MB)
테스트 2 〉통과 (49.08ms, 16MB)
테스트 3 〉통과 (65.70ms, 18.9MB)
테스트 4 〉통과 (58.02ms, 18MB)
테스트 5 〉통과 (58.90ms, 17.2MB)
테스트 6 〉통과 (67.49ms, 19.2MB)   *
테스트 7 〉통과 (61.96ms, 18.6MB)
테스트 8 〉통과 (56.65ms, 17MB)
테스트 9 〉통과 (59.62ms, 17.5MB)
테스트 10 〉통과 (63.40ms, 18.6MB)
'''