'''
못품 ㅠㅠ
'''

# def distance(a, b, n):
#     # 1 : 반시계, 2 : 시계, 3 : 양방향
#     if abs(a-b) > n-abs(a-b):
#         return (n-abs(a-b), 1)
#     elif abs(a-b) < n-abs(a-b):
#         return (abs(a-b), 2)
#     else:
#         return (abs(a-b), 3)

# # 이동할 수 있는지 확인
# def possible(n, distance, dist, check_person):
#     if max(dist) < distance:
#         return (False, -1)
#     for i in range(len(dist)):
#         if not check_person[i] and dist[i] >= distance:
#             return (True, i)
#     return (False, -1)

# # 이동하면서 지나가는 점들 다 체크
# def check_visited(n, direction, distance, pos, weak, visited):  # di : 방향, distance : 순찰 가능한 거리(사람)
#     if direction == 'dd':
#         'dd'

# def check(n, weak, dist, visited, check_person):
#     for i in range(len(weak)-1):
#         if not visited[i]:
#             for j in range(i+1, len(weak)):
#                 distance_res = distance(weak[i], weak[j], n)
#                 res = possible(n, distance_res[0], dist, check_person)
#                 if res[0]:
#                     check_person[res[1]] = 1
#                     check_visited(n, distance_res[1], distance_res[0], i, weak, visited)

# def solution(n, weak, dist):
#     answer = 0
#     visited = [0] * n
#     check_person = [0] * n
#     check(n, weak, dist, visited, check_person)
            
#     return answer