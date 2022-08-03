#https://www.acmicpc.net/problem/1316
#연속하지 않는 alpabet를 찾는 것이 핵심
#시간 68 ms 30840 kb

#1. 입력받기
N = int(input()) #N은 반복의 개수
count = 0 #결과를 담을 count
case_li = [None for _ in range(N)]#입력 받을 문자열 리스트

for i in range(N):
    case_li[i] = list(input())
#print(case_li)


#2. 검증하기
#case를 하나씩 빼면서,
#dict에 알파벳:인덱스를 넣는다.
#알파벳:인덱스가 2이상 차이나면 break
for case in case_li:
    #값을 넣을 dict소환 dict에 key:알파벳 value:index를 넣어 value가 2이상 차이나면 break
    #ex. dic == {h:1, p:3}
    dic = dict()

    for i in range(len(case) - 1, -1, -1): # ==i[::-1] pop을 할거라, 문자열 뒤쪽부터 
        alpa = case.pop()
        if dic.get(alpa) == None: #알파벳이 처음 들어온 경우
            dic[alpa] = i
        else:
            #있는데, 붙어있는 경우
            if dic.get(alpa) - i == 1: # 8 6
                dic[alpa] = i
            #있는데, 떨어져 있는 경우
            else:
                break
    else:
        count += 1   
print(count)