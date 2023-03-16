START = -1
END = 10000000
DELETED = 10000001

class Grid:
    def __init__(self, n, k):
        self.data = ["O" for _ in range(n)]     # 존재하면 O 삭제되면 X
        self.lastDeleted = []                   # 마지막으로 삭제된 곳 스텍형식으로 저장
        self.now = k                            # 현재위치
        self.linkedList = []                    # [이전위치, 이후위치]
        for idx in range(n):
            if idx == 0:
                self.linkedList.append([START, idx + 1])
            elif idx == n - 1:
                self.linkedList.append([idx - 1, END])
            else:
                self.linkedList.append([idx - 1, idx + 1])
    
    def up(self, x):    # 링크드 리스트에 있는대로 위로 이동
        while x:
            x -= 1
            if self.linkedList[self.now][0] == START:
                return
            self.now = self.linkedList[self.now][0]
        
    def down(self, x):    # 링크드 리스트에 있는대로 아래로 이동
        while x:
            x -= 1
            if self.linkedList[self.now][1] == END:
                return
            self.now = self.linkedList[self.now][1]
                
    def delete(self):
        self.data[self.now] = "X"
        self.lastDeleted.append((self.now))

        # 링크드리스트에 연관되어 있는 애들을 서로 바꿔줌
        before, nxt = self.linkedList[self.now]
        if before != START:
            self.linkedList[before][1] = nxt
        if nxt != END:
            self.linkedList[nxt][0] = before
        
        # 마지막에 있거나 맨처음에 있거나 하면 위치를 이동시킴
        save = self.now
        self.down(1)
        if save == self.now:
            self.up(1)
        
    def back(self):
        # 삭제된 곳을 꺼내서 O로 만듦
        idx = self.lastDeleted.pop()
        self.data[idx] = "O"

        # 다시 이어줌, 기존 idx위치에 연결됐던 곳이 적혀져있음
        before, nxt = self.linkedList[idx]
        if before != START:
            self.linkedList[before][1] = idx
        if nxt != END:
            self.linkedList[nxt][0] = idx


def solution(n, k, cmd):
    grid = Grid(n, k)
    for c in cmd:
        c = c.split()
        if c[0] == "U":
            grid.up(int(c[1]))
        if c[0] == "D":
            grid.down(int(c[1]))
        if c[0] == "C":
            grid.delete()
        if c[0] == "Z":
            grid.back()
    return ''.join(grid.data)

print(solution(8,	2,	["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8,	2,	["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))

# 정확성  테스트
# 테스트 1 〉	통과 (0.02ms, 10.5MB)
# 테스트 2 〉	통과 (0.03ms, 10.5MB)
# 테스트 3 〉	통과 (0.02ms, 10.4MB)
# 테스트 4 〉	통과 (0.03ms, 10.4MB)
# 테스트 5 〉	통과 (0.15ms, 10.4MB)
# 테스트 6 〉	통과 (0.19ms, 10.4MB)
# 테스트 7 〉	통과 (0.16ms, 10.3MB)
# 테스트 8 〉	통과 (0.14ms, 10.4MB)
# 테스트 9 〉	통과 (0.16ms, 10.4MB)
# 테스트 10 〉	통과 (0.13ms, 10.5MB)
# 테스트 11 〉	통과 (1.17ms, 10.4MB)
# 테스트 12 〉	통과 (1.36ms, 10.5MB)
# 테스트 13 〉	통과 (2.42ms, 10.4MB)
# 테스트 14 〉	통과 (3.61ms, 10.4MB)
# 테스트 15 〉	통과 (3.97ms, 10.5MB)
# 테스트 16 〉	통과 (3.99ms, 10.4MB)
# 테스트 17 〉	통과 (16.43ms, 10.3MB)
# 테스트 18 〉	통과 (15.65ms, 10.5MB)
# 테스트 19 〉	통과 (14.20ms, 10.4MB)
# 테스트 20 〉	통과 (8.23ms, 10.4MB)
# 테스트 21 〉	통과 (6.99ms, 10.5MB)
# 테스트 22 〉	통과 (11.67ms, 10.4MB)
# 테스트 23 〉	통과 (0.03ms, 10.4MB)
# 테스트 24 〉	통과 (0.03ms, 10.4MB)
# 테스트 25 〉	통과 (0.01ms, 10.4MB)
# 테스트 26 〉	통과 (0.02ms, 10.5MB)
# 테스트 27 〉	통과 (0.03ms, 10.5MB)
# 테스트 28 〉	통과 (0.07ms, 10.4MB)
# 테스트 29 〉	통과 (0.05ms, 10.4MB)
# 테스트 30 〉	통과 (0.04ms, 10.4MB)
# 효율성  테스트
# 테스트 1 〉	통과 (1042.80ms, 167MB)
# 테스트 2 〉	통과 (1051.16ms, 167MB)
# 테스트 3 〉	통과 (1072.05ms, 168MB)
# 테스트 4 〉	통과 (923.79ms, 174MB)
# 테스트 5 〉	통과 (838.60ms, 174MB)
# 테스트 6 〉	통과 (871.11ms, 173MB)
# 테스트 7 〉	통과 (286.42ms, 47.3MB)
# 테스트 8 〉	통과 (291.78ms, 58.7MB)
# 테스트 9 〉	통과 (875.07ms, 175MB)
# 테스트 10 〉	통과 (874.65ms, 175MB)