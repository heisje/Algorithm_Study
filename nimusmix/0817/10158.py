W, H = map(int, input().split())
p, q = map(int, input().split())
T = int(input())

p_li = list(range(W+1)) + list(range(W-1, 0, -1))            # 개미가 이동하는 좌표대로 리스트 생성
q_li = list(range(H+1)) + list(range(H-1, 0, -1))            # ex) [0, 1, 2, 3, 4, 3, 2, 1, 0, 1, ...]

print(p_li[(p+T)%(len(p_li))], q_li[(q+T)%(len(q_li))])      # '(좌표+시간) % 리스트의 길이'를 인덱스로 하여 좌표 추출