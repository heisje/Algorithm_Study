import re 
num = re.compile('[0-9]+')

def solution(files):
    # 1차 분류 (해더/넘버/모든이름)
    match_list = []
    for file in files:
        number = num.findall(file)[0]
        head, *tail = file.split(number)
        match_list.append((head.upper(),number.zfill(5),file))
    # 2차 헤더와 넘버로 sort
    match_list.sort(key=lambda x:(x[0],x[1]))
    
    answer = []
    for match in match_list:
        answer.append(match[2])
    return answer


a = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(a))
a = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
print(solution(a))


# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.02ms, 10.2MB)
# 테스트 3 〉	통과 (2.16ms, 10.7MB)
# 테스트 4 〉	통과 (1.79ms, 10.5MB)
# 테스트 5 〉	통과 (1.80ms, 10.4MB)
# 테스트 6 〉	통과 (1.74ms, 10.6MB)
# 테스트 7 〉	통과 (1.74ms, 10.3MB)
# 테스트 8 〉	통과 (1.55ms, 10.4MB)
# 테스트 9 〉	통과 (1.61ms, 10.4MB)
# 테스트 10 〉	통과 (1.63ms, 10.5MB)
# 테스트 11 〉	통과 (1.75ms, 10.3MB)
# 테스트 12 〉	통과 (1.75ms, 10.3MB)
# 테스트 13 〉	통과 (1.34ms, 10.4MB)
# 테스트 14 〉	통과 (1.79ms, 10.4MB)
# 테스트 15 〉	통과 (1.83ms, 10.5MB)
# 테스트 16 〉	통과 (1.68ms, 10.4MB)
# 테스트 17 〉	통과 (1.25ms, 10.3MB)
# 테스트 18 〉	통과 (1.44ms, 10.6MB)
# 테스트 19 〉	통과 (1.57ms, 10.7MB)
# 테스트 20 〉	통과 (1.63ms, 10.5MB)