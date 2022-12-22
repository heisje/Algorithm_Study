import math

def solution(m, musicinfos):
    answer = ''
    max_time = 0
    # 올림음들은 글자가 2개이기 때문에 바꿔줌
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")

    for music in musicinfos:

        start, end, title, melody = music.split(',')
        melody = melody.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")

        # 총 재생되는 시간 계산
        time = ((int(end[:2]) - int(start[:2])) * 60) + (int(end[3:]) - int(start[3:]))

        # 재생시간동안 재생되는 전체 멜로디
        tmp = (melody * math.ceil(time / len(melody)))[:time]

        # 기억한 멜로디가 재생된 전체 멜로디에 있으면, 그리고 max_time이 갱신이 된다면
        if m in tmp and time > max_time:
            answer = title
            max_time = time

    if not answer:
        return "(None)"
    else:
        return answer

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))

'''
테스트 1 〉	통과 (0.03ms, 10.5MB)
테스트 2 〉	통과 (0.04ms, 10.4MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.04ms, 10.2MB)
테스트 7 〉	통과 (0.05ms, 10.3MB)
테스트 8 〉	통과 (0.06ms, 10.5MB)
테스트 9 〉	통과 (0.06ms, 10.4MB)
테스트 10 〉	통과 (0.09ms, 10.4MB)
테스트 11 〉	통과 (0.05ms, 10.4MB)
테스트 12 〉	통과 (0.06ms, 10.3MB)
테스트 13 〉	통과 (0.06ms, 10.3MB)
테스트 14 〉	통과 (0.08ms, 10.3MB)
테스트 15 〉	통과 (0.06ms, 10.4MB)
테스트 16 〉	통과 (0.06ms, 10.3MB)
테스트 17 〉	통과 (0.06ms, 10.5MB)
테스트 18 〉	통과 (0.07ms, 10.2MB)
테스트 19 〉	통과 (0.06ms, 10.3MB)
테스트 20 〉	통과 (0.08ms, 10.4MB)
테스트 21 〉	통과 (0.09ms, 10.4MB)
테스트 22 〉	통과 (0.05ms, 10.3MB)
테스트 23 〉	통과 (0.06ms, 10.5MB)
테스트 24 〉	통과 (0.06ms, 10.3MB)
테스트 25 〉	통과 (0.03ms, 10.3MB)
테스트 26 〉	통과 (0.03ms, 10.4MB)
테스트 27 〉	통과 (0.03ms, 10.5MB)
테스트 28 〉	통과 (0.03ms, 10.4MB)
테스트 29 〉	통과 (1.29ms, 10.2MB)
테스트 30 〉	통과 (1.18ms, 10.4MB)
'''