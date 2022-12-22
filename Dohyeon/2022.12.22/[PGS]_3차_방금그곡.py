def solution(m, musicinfos):
    answer = '(None)'
    m = m.replace('A#', 'H')
    m = m.replace('C#', 'I')
    m = m.replace('D#', 'J')
    m = m.replace('F#', 'K')
    m = m.replace('G#', 'L')
    longest_time = 0
    for i in range(len(musicinfos)):
        infos = list(musicinfos[i].split(','))
        infos[3] = infos[3].replace('A#', 'H')
        infos[3] = infos[3].replace('C#', 'I')
        infos[3] = infos[3].replace('D#', 'J')
        infos[3] = infos[3].replace('F#', 'K')
        infos[3] = infos[3].replace('G#', 'L')
        start_time = int(infos[0][:2]) * 60 + int(infos[0][3:])
        end_time = int(infos[1][:2]) * 60 + int(infos[1][3:])
        song_length = len(infos[3])
        total_time = end_time - start_time
        t = total_time // song_length
        l = total_time % song_length

        melody = ''
        for j in range(t):
            melody = melody + infos[3]
        melody = melody + infos[3][:l]

        if m in melody:
            if longest_time < total_time:
                longest_time = total_time
                answer = infos[2]

    return answer

print(solution("ABC",	["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))

"""
테스트 1 〉	통과 (0.04ms, 10.5MB)
테스트 2 〉	통과 (0.04ms, 10.5MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (0.04ms, 10.4MB)
테스트 5 〉	통과 (0.04ms, 10.4MB)
테스트 6 〉	통과 (0.06ms, 10.4MB)
테스트 7 〉	통과 (0.11ms, 10.6MB)
테스트 8 〉	통과 (0.17ms, 10.6MB)
테스트 9 〉	통과 (0.10ms, 10.4MB)
테스트 10 〉	통과 (0.17ms, 10.6MB)
테스트 11 〉	통과 (0.10ms, 10.4MB)
테스트 12 〉	통과 (0.11ms, 10.4MB)
테스트 13 〉	통과 (0.11ms, 10.4MB)
테스트 14 〉	통과 (0.17ms, 10.4MB)
테스트 15 〉	통과 (0.16ms, 10.5MB)
테스트 16 〉	통과 (0.10ms, 10.4MB)
테스트 17 〉	통과 (0.10ms, 10.4MB)
테스트 18 〉	통과 (0.11ms, 10.4MB)
테스트 19 〉	통과 (0.11ms, 10.5MB)
테스트 20 〉	통과 (0.10ms, 10.4MB)
테스트 21 〉	통과 (0.10ms, 10.5MB)
테스트 22 〉	통과 (0.11ms, 10.4MB)
테스트 23 〉	통과 (0.11ms, 10.4MB)
테스트 24 〉	통과 (0.11ms, 10.4MB)
테스트 25 〉	통과 (0.03ms, 10.4MB)
테스트 26 〉	통과 (0.05ms, 10.5MB)
테스트 27 〉	통과 (0.04ms, 10.4MB)
테스트 28 〉	통과 (0.03ms, 10.5MB)
테스트 29 〉	통과 (1.57ms, 10.5MB)
테스트 30 〉	통과 (1.13ms, 10.5MB)
"""