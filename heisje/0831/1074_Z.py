#아이디어: 재귀로 찾는다. 좌상 우상 좌하 우하 이렇게 4방향으로 나누면서 안으로 안으로 들어가는 방법
# 68ms
    #깊이   , 개수  , 변화하는 r행 c열 값
def z(depth, count, r, c):
    if N-depth == -1: #종료조건 = 완전히 재귀를 다 끝냈을 때
        print(count)
        return
    quarter = 2 ** (N - depth) * 2 ** (N - depth) # 개수를 세기위해 4등분으로 나누어서 패턴마다 더해줌
    half = 2 ** (N - depth)                          # 패턴마다 r, c값이 변화해야 하므로
    if r < half and c < half:  # 좌상단 둘다 중앙보다 작아야한다.
        z(depth + 1, count + quarter * 0, r, c)
    elif r < half and c >= half:  # 우상단
        z(depth + 1, count + quarter * 1, r, c - half) #우상단의 경우에는 16부터 시작해야하므로 quarter을 더해준다.
    elif r >= half and c < half:  # 좌하단              #좌하단의 경우에는 4등분으로 나누고 다음 뎁스로 들어가야하기 때문에
        z(depth + 1, count + quarter * 2, r - half, c) #half를 빼준다.
    elif r >= half and c >= half:  # 우하단
        z(depth + 1, count + quarter * 3, r - half, c - half)

N, R, C = map(int,input().split())
z(1, 0, R, C)



