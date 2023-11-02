from collections import deque
import sys

def solution(begin, target, words):
    
    def check(word1, word2):
        cnt = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                cnt += 1
            if cnt >= 2:
                return False
        return True
    
    def loop(pre, visited, cnt):
        if cnt > answer[0]:
            return 
        
        if target == words[pre]:
            answer[0] = cnt
            return
        
        for go in nodes[pre]:
            if go not in visited:
                visited.add(go)
                loop(go, visited, cnt + 1)
                visited.remove(go)
        
    nodes = [[] for _ in range(len(words))]
    
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and check(words[i], words[j]):
                nodes[i].append(j)
    
    answer = [10000000]
    for i in range(len(words)):
        if check(begin, words[i]):
            visited1 = set()
            visited1.add(i)
            loop(i, visited1, 0)
            
    if answer[0] == 10000000:
        return 0
    else:
        return answer[0] + 1
    
# 테스트 1 〉	통과 (0.03ms, 10.4MB)
# 테스트 2 〉	통과 (1.28ms, 10.3MB)
# 테스트 3 〉	통과 (2.35ms, 10.2MB)
# 테스트 4 〉	통과 (0.04ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.5MB)