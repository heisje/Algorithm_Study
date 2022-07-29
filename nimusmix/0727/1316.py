n = int(input())
count = 0

for i in range(n):
    word = list(input())
    check_list = []
    for j in range(len(word)):                                 # 입력된 단어의 알파벳이 체크리스트에 없거나, 직전 글자와 같다면 리스트에 추가
        if word[j] not in check_list or word[j] == word[j-1]:
            check_list.append(word[j])                         # 입력된 단어와 리스트에 추가된 단어가 같다면 그룹 단어이므로 카운트
    if word == check_list:
        count += 1
print(count)