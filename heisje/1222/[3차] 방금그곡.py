# https://school.programmers.co.kr/learn/courses/30/lessons/17683
# (문제오류)E#에 대한 조건을 추가해야됨
import re
MATCH_MUSIC = {
    'C' : '1', 
    'C#' : '2', 
    'D' : '3', 
    'D#' : '4',
    'E' : '5', 
    'E#' : 'F',
    'F' : '6', 
    'F#' : '7', 
    'G' : '8', 
    'G#' : '9', 
    'A' : 'A', 
    'A#' : 'B', 
    'B' : 'C',
}
def solution(m, musicinfos):
    
    answers = []
    p = re.compile('[a-zA-Z][#]*')
    m = p.findall(m)
    new_m = ''
    
    for n in m:
        if MATCH_MUSIC.get(n):
            new_m += MATCH_MUSIC.get(n)
        
    for musicinfo in musicinfos:
        start, end, title, music_base = musicinfo.split(',')

        # 음계를 구하는 과정
        # 정규표현식을 사용함
        music_base = p.findall(music_base)
        music_len = len(music_base)
        new_music_base = ''
        for n in music_base:
            new_music_base += MATCH_MUSIC[n]

        # 시간을 구하는 부분
        hour, minute = start.split(':')
        start = int(hour) * 60 + int(minute)
        hour, minute = end.split(':')
        end = int(hour) * 60 + int(minute)
        time = end - start
        
        # 주어진 조건에 맞게 음악을 길게 늘리는 과정
        music = ''
        index = 0
        for _ in range(time):
            music += new_music_base[index % music_len]
            index += 1
        print(new_music_base)
        # 안에 들었는지 확인하는 과정
        if music.find(new_m) >= 0:
            answers.append((time, -start, title))


    # 없을 경우
    if not answers:
        return '(None)'
    
    # 여러개일 경우
    answers.sort(reverse=True)
        
    return answers[0][2]
    

a = ""	
b = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(a,b))
a = "CC#BCC#BCC#BCC#B"	
b = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
print(solution(a,b))
a = "ABC"	
b = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(a,b))
a = "ABCDEFG"
b = ["11:50,12:04,HELLO,CDEFGAB", "12:57,13:11,BYE,CDEFGAB"]
print(solution(a,b))