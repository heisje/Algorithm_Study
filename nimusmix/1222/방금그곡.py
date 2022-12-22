def melody_split(arr):
    MELODY = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    rst = ''
    for idx, i in enumerate(arr):
        if not i.isalpha():
            continue
        # '#' 붙으면 소문자로 문자열에 저장
        rst += i.lower() if idx != (len(arr) - 1) and arr[idx:idx+2] in MELODY else i
    return rst


def solution(m, musicinfos):
    neo = melody_split(m)
    ans = []

    for idx, musicinfo in enumerate(musicinfos):
        s, e, title, mel = musicinfo.split(',')
        
        t, m = map(int, s.split(':'))
        start = t * 60 + m
        
        t, m = map(int, e.split(':'))
        end = t * 60 + m
        
        playing = end - start
        
        melody = melody_split(mel)
        # melody의 길이가 playing보다 길어질 때까지 연장한 다음 자르기
        while len(melody) < playing:
            melody += melody
        melody = melody[:playing]

        if neo in melody:
            # 아래에서 playing의 길이대로 내림차순 정렬해야 하므로 idx도 -를 붙여서 먼저 입력된 것들이 가장 큰 값을 갖도록 하기
            ans.append((playing, -idx, title))

    if not ans:
        return "(None)"
    elif len(ans) == 1:
        return ans[0][2]
    
    ans.sort(reverse=True)
    return ans[0][2]


# 테스트 1 〉	통과 (0.03ms, 10.3MB)
# 테스트 2 〉	통과 (0.03ms, 10.4MB)
# 테스트 3 〉	통과 (0.04ms, 10.3MB)
# 테스트 4 〉	통과 (0.04ms, 10.4MB)
# 테스트 5 〉	통과 (0.03ms, 10.5MB)
# 테스트 6 〉	통과 (0.04ms, 10.4MB)
# 테스트 7 〉	통과 (0.15ms, 10.5MB)
# 테스트 8 〉	통과 (0.17ms, 10.4MB)
# 테스트 9 〉	통과 (0.15ms, 10.4MB)
# 테스트 10 〉	통과 (0.37ms, 10.4MB)
# 테스트 11 〉	통과 (0.15ms, 10.4MB)
# 테스트 12 〉	통과 (0.14ms, 10.4MB)
# 테스트 13 〉	통과 (0.14ms, 10.5MB)
# 테스트 14 〉	통과 (0.15ms, 10.4MB)
# 테스트 15 〉	통과 (0.25ms, 10.4MB)
# 테스트 16 〉	통과 (0.15ms, 10.3MB)
# 테스트 17 〉	통과 (0.14ms, 10.4MB)
# 테스트 18 〉	통과 (0.14ms, 10.4MB)
# 테스트 19 〉	통과 (0.76ms, 10.5MB)
# 테스트 20 〉	통과 (0.14ms, 10.5MB)
# 테스트 21 〉	통과 (0.14ms, 10.3MB)
# 테스트 22 〉	통과 (0.15ms, 10.4MB)
# 테스트 23 〉	통과 (0.15ms, 10.4MB)
# 테스트 24 〉	통과 (0.14ms, 10.4MB)
# 테스트 25 〉	통과 (0.04ms, 10.3MB)
# 테스트 26 〉	통과 (0.04ms, 10.4MB)
# 테스트 27 〉	통과 (0.05ms, 10.4MB)
# 테스트 28 〉	통과 (0.05ms, 10.3MB)
# 테스트 29 〉	통과 (11.34ms, 10.5MB)
# 테스트 30 〉	통과 (11.07ms, 10.4MB)