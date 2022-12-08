def solution(files):
    answer = []
    for file in files:
        head, number = '', ''

        for word in file:
            if word.isdigit():          # 숫자면
                number += word          # number 에 추가
            elif not number:            # number 가 비어있고 숫자가 아니면
                head += word.lower()    # head 에 추가
            else:                       # number가 비어있지 않고 그 외
                break                   # 멈춰!

        # 리스트에 head, number와 해당 file의 index를 추가
        answer.append((head, int(number), files.index(file)))

    # head, number 순으로 정렬
    answer.sort(key=lambda x: (x[0], x[1]))

    result = []
    # 정렬된 answer 에서 files의 해당 인덱스를 찾아 result에 추가
    for i in answer:
        result.append(files[i[2]])

    return result

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))

'''
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (8.45ms, 10.7MB)
테스트 4 〉	통과 (8.28ms, 10.4MB)
테스트 5 〉	통과 (8.09ms, 10.4MB)
테스트 6 〉	통과 (8.10ms, 10.6MB)
테스트 7 〉	통과 (8.04ms, 10.4MB)
테스트 8 〉	통과 (6.70ms, 10.5MB)
테스트 9 〉	통과 (6.93ms, 10.6MB)
테스트 10 〉	통과 (7.08ms, 10.4MB)
테스트 11 〉	통과 (7.03ms, 10.5MB)
테스트 12 〉	통과 (7.65ms, 10.6MB)
테스트 13 〉	통과 (7.27ms, 10.3MB)
테스트 14 〉	통과 (12.31ms, 10.7MB)
테스트 15 〉	통과 (12.31ms, 10.7MB)
테스트 16 〉	통과 (7.92ms, 10.3MB)
테스트 17 〉	통과 (7.88ms, 10.6MB)
테스트 18 〉	통과 (7.78ms, 10.5MB)
테스트 19 〉	통과 (7.59ms, 10.6MB)
테스트 20 〉	통과 (7.59ms, 10.6MB)
'''