# 락의 그래프에서 맨 위 왼쪽부터 첫 번째로 기준을 잡는다.
# 네가지 방향으로 미리 돌려놓고, 기준점에 대입해본다.
def solution(key, lock):
    LOCK_LEN = len(lock)
    KEY_LEN = len(key)
    
    # Key 속성
    keyRotates = [[[0 for _ in range(0, len(key[0]))] for _ in range(0, len(key))] for _ in range(0,4)]
    keyDols = [[] for _ in range(0,4)]

    # 90도 돌리기
    for y in range(0, len(key)):
        for x in range(0, len(key[y])):
            keyRotates[0][x][KEY_LEN - 1 - y] = key[y][x]
            if key[y][x] == 1:
                keyDols[0].append((KEY_LEN - 1 - y,x))
                
    for i in range(1,4):
        for y in range(0, len(key)):
            for x in range(0, len(key[y])):
                keyRotates[i][x][KEY_LEN - 1 - y] = keyRotates[i-1][y][x]
                if keyRotates[i-1][y][x] == 1:
                    keyDols[i].append((KEY_LEN - 1 - y,x))
    
    # lock 구멍 찾기, trg로 전부 1일 경우 배제
    lockHoles = []
    trg = True
    for y in range(0, len(lock)):
        for x in range(0, len(lock[y])):
            if lock[y][x] == 0:
                lockHoles.append((x, y))
                trg = False
    if trg:
        return True

    # 락의 첫번째를 기준으로 모든 키의 값에 대입해본다.
    for i in range(0,4):                # 4방향 테스트
        for lockHole in lockHoles:      # 락 구멍을 전부 탐색
            holeX, holeY = lockHole
            for value in keyDols[i]:    # 키 돌기를 전부 탐색
                dolX, dolY = value

                # 돌기의 위치를 홀에 맞춘다.
                dX = holeX - dolX
                dY = holeY - dolY

                # lock x,y를 전부 돌면서, key와 맞는지 확인해본다.
                def check():
                    for y in range(0, len(lock)):
                        for x in range(0, len(lock[y])):
                            if 0 <= y-dY < len(keyRotates[i]) and 0 <= x-dX < len(keyRotates[i][0]):
                                # 홈과 돌기가 맞지 않다면
                                if lock[y][x] == keyRotates[i][y-dY][x-dX] :
                                    return False
                            else:
                                # 홈이 있는데 돌기가 없으면
                                if lock[y][x] == 0:
                                    return False
                    return True

                if check():
                    return True
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

# 테스트 1 〉	통과 (0.06ms, 10.2MB)
# 테스트 2 〉	통과 (0.10ms, 10.3MB)
# 테스트 3 〉	통과 (0.32ms, 10.4MB)
# 테스트 4 〉	통과 (0.05ms, 10.5MB)
# 테스트 5 〉	통과 (1.67ms, 10.3MB)
# 테스트 6 〉	통과 (0.87ms, 10.3MB)
# 테스트 7 〉	통과 (67.53ms, 10.3MB)
# 테스트 8 〉	통과 (2.39ms, 10.3MB)
# 테스트 9 〉	통과 (3.25ms, 10.3MB)
# 테스트 10 〉	통과 (13.73ms, 10.3MB)
# 테스트 11 〉	통과 (133.17ms, 10.3MB)
# 테스트 12 〉	통과 (0.04ms, 10.3MB)
# 테스트 13 〉	통과 (0.23ms, 10.3MB)
# 테스트 14 〉	통과 (0.09ms, 10.5MB)
# 테스트 15 〉	통과 (0.28ms, 10.3MB)
# 테스트 16 〉	통과 (7.15ms, 10.4MB)
# 테스트 17 〉	통과 (6.40ms, 10.3MB)
# 테스트 18 〉	통과 (0.71ms, 10.4MB)
# 테스트 19 〉	통과 (0.07ms, 10.3MB)
# 테스트 20 〉	통과 (20.42ms, 10.3MB)
# 테스트 21 〉	통과 (21.67ms, 10.4MB)
# 테스트 22 〉	통과 (10.89ms, 10.4MB)
# 테스트 23 〉	통과 (0.37ms, 10.3MB)
# 테스트 24 〉	통과 (0.23ms, 10.5MB)
# 테스트 25 〉	통과 (31.83ms, 10.3MB)
# 테스트 26 〉	통과 (10.08ms, 10.2MB)
# 테스트 27 〉	통과 (204.46ms, 10.3MB)
# 테스트 28 〉	통과 (3.96ms, 10.3MB)
# 테스트 29 〉	통과 (0.58ms, 10.4MB)
# 테스트 30 〉	통과 (7.67ms, 10.3MB)
# 테스트 31 〉	통과 (61.14ms, 10.3MB)
# 테스트 32 〉	통과 (31.46ms, 10.3MB)
# 테스트 33 〉	통과 (10.62ms, 10.4MB)
# 테스트 34 〉	통과 (0.50ms, 10.3MB)
# 테스트 35 〉	통과 (0.95ms, 10.5MB)
# 테스트 36 〉	통과 (1.11ms, 10.5MB)
# 테스트 37 〉	통과 (0.38ms, 10.2MB)
# 테스트 38 〉	통과 (0.10ms, 10.4MB)