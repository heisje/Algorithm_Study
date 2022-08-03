suspects = []
spy = []
for i in range(9):
    height = int(input())
    suspects.append(height) # 키를 용의자 리스트에 저장

found = False 
for j in range(len(suspects)):
    for k in range(len(suspects)):
        if j == k:
            continue
        else:
            spy.append(suspects[j]) # 스파이로 추정된 둘을 스파이 리스트에 저장해둠
            spy.append(suspects[k])
            suspects[j] = 0 # 스파이 둘의 값을 빼고 합이 100이 되는지 확인
            suspects[k] = 0
            if sum(suspects) == 100:
                found = True # 스파이 둘을 찾아냈으니 참으로 바뀜
                break
            else:
                suspects[j] = spy[0] # 스파이가 아니므로 용의자 리스트의 값을 원래대로 돌려둠
                suspects[k] = spy[1]
                spy.clear() # 다시 사용하기 위해 비워둠
    if found:
        break

suspects.sort() # 오름차순 정렬
for i in range(2, len(suspects)): # 제일 앞에 0이 두개 오므로 빼준다
    print(suspects[i])