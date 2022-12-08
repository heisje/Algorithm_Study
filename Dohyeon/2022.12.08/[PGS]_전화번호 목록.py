def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        check = False
        case = phone_book[i]
        for j in range(i, len(phone_book)):
            if i == j:
                continue
            else:
                if case == phone_book[j][:len(case)]:
                    check = True
                    break

                if case[:len(phone_book[j])] == phone_book[j]:
                    check = True
                    break
        if check:
            answer = False
            break

    return answer


result = solution(["12","123","1235","567","88"])
print(result)

# 답안코드
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

# https://velog.io/@chaegil15/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%95%B4%EC%8B%9C-%EC%A0%84%ED%99%94%EB%B2%88%ED%98%B8-%EB%AA%A9%EB%A1%9D

