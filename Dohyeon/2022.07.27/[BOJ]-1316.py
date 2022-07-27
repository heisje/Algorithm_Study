n = int(input()) # 단어 수 입력
result = 0
word_list =[]
for i in range(n):
    a = input()
    word_list.append(a) # 입력 받은 단어 하나씩 list에 넣음
for i in range(n): # 단어 수만큼 반복
    
    is_group = True # 그룹단어 표시를 위함, 그대로 True로 나온다면 그룹단어
    check_list = [] # 나온 알파벳을 저장하기 위함
    idx = -1 # check_list의 체크 중인 index를 나타냄, 하나가 들어가면 0이되므로 -1
    word = word_list[i] #확인할 단어 word
    for j in word: #순서대로 한글자씩 확인
        if j not in check_list: #체크한 적이 있는지를 확인
            check_list.append(j)
            idx += 1
        else:
            if check_list[idx] == j: # 계속 반복중인 글자임
                continue
            else:
                is_group = False # 확인한적 있는 글자이지만 반복중인 것이 아님
                break
    if is_group:
        result += 1

print(result)

# 시간복잡도 nm?
        
