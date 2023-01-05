# 반복되는지 확인하는 함수. 반복되는 횟수에 따라 재귀로 들어가 총 반복되는 횟수를 최종으로 return
def Alzip(string, start, size):
    if string[start:start+size] == string[start+size:start+size*2]:
        return Alzip(string, start+size, size) + 1
    else:
        return 1

def solution(s):
    answer = len(s)                         # 아무것도 안한게 일단 최소값
    for size in range(1, len(s)//2+2):      # 절반 이상의 size가 되면 아무것도 안한 값이 최솟값.
        idx = 0
        length = 0
        while idx + size < len(s):          # 현재 index + size가 s의 총 길이보다 작을 때까지
            n = Alzip(s, idx, size)         # 반복되는 횟수 계산
            if n > 1:                       # 반복되는게 있다면
                idx += size * n             # idx 는 반복된 size * n 만큼 뒤로
                length += size + len(str(n))# 현재 길이는 반복된 횟수 숫자의 길이 + size
            else:                           # 반복이 되지 않는다면
                idx += size * n             # idx는 size 만큼만 뒤로
                length += size * n          # 길이또한 size 그대로
        length += len(s) - idx              # 현재 단위 길이에 전체 길이에서 남은 index 만큼을 빼주어 뒤에 남은 부분을 더해 총 길이 계산
        if length < answer:                 # 최솟값 갱신
            answer = length

    return answer

'''
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.44ms, 10.2MB)
테스트 3 〉	통과 (0.35ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.04ms, 10.1MB)
테스트 7 〉	통과 (0.45ms, 10.2MB)
테스트 8 〉	통과 (0.86ms, 10.2MB)
테스트 9 〉	통과 (0.70ms, 10.2MB)
테스트 10 〉	통과 (4.05ms, 10.2MB)
테스트 11 〉	통과 (0.09ms, 10.2MB)
테스트 12 〉	통과 (0.09ms, 10MB)
테스트 13 〉	통과 (0.11ms, 10.4MB)
테스트 14 〉	통과 (1.33ms, 10.3MB)
테스트 15 〉	통과 (0.11ms, 10.1MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
테스트 17 〉	통과 (2.32ms, 10.4MB)
테스트 18 〉	통과 (1.24ms, 10.2MB)
테스트 19 〉	통과 (1.28ms, 9.99MB)
테스트 20 〉	통과 (3.72ms, 10.2MB)
테스트 21 〉	통과 (4.25ms, 10.2MB)
테스트 22 〉	통과 (2.92ms, 10.2MB)
테스트 23 〉	통과 (3.08ms, 10.1MB)
테스트 24 〉	통과 (3.12ms, 10.1MB)
테스트 25 〉	통과 (2.92ms, 10.2MB)
테스트 26 〉	통과 (2.97ms, 10.2MB)
테스트 27 〉	통과 (3.02ms, 10.3MB)
테스트 28 〉	통과 (0.02ms, 10.3MB)
'''