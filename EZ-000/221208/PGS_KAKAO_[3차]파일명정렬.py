import re


def solution(files):
    p = re.compile(r'(?P<HEAD>\D+)(?P<NUMBER>\d+)')
    print(p.match('img01.png').group("HEAD"))
    files.sort(key=lambda x: (p.match(x).group("HEAD").upper(), int(p.match(x).group("NUMBER"))))
    return files


# 테스트 1 〉	통과 (0.15ms, 10.2MB)
# 테스트 2 〉	통과 (0.13ms, 10.1MB)
# 테스트 3 〉	통과 (1.94ms, 10.6MB)
# 테스트 4 〉	통과 (1.70ms, 10.5MB)
# 테스트 5 〉	통과 (1.57ms, 10.5MB)
# 테스트 6 〉	통과 (1.53ms, 10.5MB)
# 테스트 7 〉	통과 (1.81ms, 10.5MB)
# 테스트 8 〉	통과 (1.48ms, 10.5MB)
# 테스트 9 〉	통과 (1.54ms, 10.4MB)
# 테스트 10 〉 통과 (2.71ms, 10.4MB)
# 테스트 11 〉 통과 (2.54ms, 10.6MB)
# 테스트 12 〉 통과 (1.58ms, 10.5MB)
# 테스트 13 〉 통과 (1.48ms, 10.6MB)
# 테스트 14 〉 통과 (1.36ms, 10.7MB)
# 테스트 15 〉 통과 (1.17ms, 10.8MB)
# 테스트 16 〉 통과 (2.45ms, 10.5MB)
# 테스트 17 〉 통과 (1.15ms, 10.5MB)
# 테스트 18 〉 통과 (1.44ms, 10.3MB)
# 테스트 19 〉 통과 (2.37ms, 10.5MB)
# 테스트 20 〉 통과 (2.45ms, 10.5MB)
