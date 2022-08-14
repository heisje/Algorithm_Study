#https://www.acmicpc.net/problem/2477

#문제: ㄱ자 모양의 밭에 최대한 심을 수 있는 참외의 개수
#풀이방법: 1. ㄱ자를 체크하기위해 먼저 큰 네모의 넓이를 구한 뒤 작은 네모를 빼준다.

#변수세팅
N = int(input())                #1m**2당 심을 수 있는 참외의 개수
li = []                         #리스트에 전부 넣기 (idx, width)
check_li = [0,0,0,0]            #체크리스트에 갯수세기

#입력
for idx in range(6):
    bearing, width = map(int, input().split())
    li.append([bearing - 1,width])           #리스트에 전부 넣기
    check_li[bearing - 1] += 1               #체크리스트에 개수 세기

#모서리 찾기, 긴변에서부터 3개의 거리만큼에 모서리가 있다.
edge = dict() #모서리를 담을 변수 (set안됨) 
big_edge = [] #긴 변
for idx in range(6):
    if check_li[li[idx][0]] == 1:  #긴 변일때
        if check_li[li[(idx + 3) % 6][0]] == 2: #앞이 짧은 변이면 추가 #li = [(idx, width)]
            edge[li[(idx + 3) % 6][0]] = li[(idx + 3) % 6][1]
        elif check_li[li[(idx - 3 + 6) % 6][0]] == 2: #뒤가 짧은 변이면 추가
            edge[li[(idx - 3 + 6) % 6][0]] = li[(idx - 3 + 6) % 6][1]

        big_edge.append(li[idx][1]) #긴 변 저장

#작은 모서리 넓이 구하기
a = [] 
for c in edge.values():
    a += [c]
small_box = a[0] * a[1]

big_box = big_edge[0] * big_edge[1]
print((big_box-small_box) * N)
