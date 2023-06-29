# 1224ms

# 연속된 초밥을 line으로 보고
# D개의 길이를 가지고 0으로 초기화 된 li를 가지고
# 처음에 K개 만큼 뒤로 체크를 하고
# 이후 back을 하나씩 뒤로 옮기면서 완전 탐색한다.
# 탐색중에 C를 만나면 카운트 하지 않는다.
# 0이 되거나 0에서 1로 될 때 카운트를 시작한다.

def main():
    N, D, K, C = map(int, input().split())
    li = [int(input()) for _ in range(N)]
    checkLi = [0 for _ in range(D+1)]
    count = 0
    answer = 0
  
    # 리스트 체크
    for k in range(K):
        checkLi[li[-k-1]] += 1
        if checkLi[li[-k-1]] == 1:
            count += 1

    # back이 맨뒤로 갈 때 까지 완전 탐색
    for back in range(0, N):
        # 앞부분 빼기
        front = back - K
        checkLi[li[front]] -= 1
        if checkLi[li[front]] == 0:
            count -= 1

        # 뒷부분 더하기
        checkLi[li[back]] += 1
        if checkLi[li[back]] == 1:
            count += 1

        # 최대값 체크
        if checkLi[C] == 0:
            if answer < count + 1:
                answer = count + 1
        else:
            if answer < count:
                answer = count
    return answer

print(main())