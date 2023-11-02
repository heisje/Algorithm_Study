# Lv3
from collections import deque

def solution(begin, target, words):
    answer = 0
    # 방문 체크를 위해 begin 추가
    words.append(begin)
    answer = bfs(begin, target, words)
    
    return answer

def bfs(begin, target, words):
    idx = words.index(begin)
    visited = [0] * len(words)
    visited[idx] = 1
    que = deque()
    que.append(begin)
    while que:
        cur_word = que.popleft()
        idx = words.index(cur_word)
        for i in range(len(words)):
            # 이미 방문 했으면 continue
            if visited[i]:
                continue
            # 바꿀 수 있으면 진행
            if check_spell(cur_word, words[i]):
                # 종료 조건: target이랑 같을 경우
                if words[i] == target:
                    return visited[idx]
                # 해당 단어로 바꾼 후 방문 체크
                que.append(words[i])
                visited[i] = visited[idx] + 1
    return 0
                
            
def check_spell(cur_word, word):
    flag = False
    for i in range(len(cur_word)):
        if cur_word[i] != word[i]:
            if flag:
                return False
            flag = True
    return True
    
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.05ms, 10.3MB)
테스트 3 〉	통과 (0.19ms, 10.4MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
'''