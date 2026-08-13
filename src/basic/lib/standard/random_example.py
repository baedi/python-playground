"""
    난수(Random) 라이브러리 사용 예시
"""

import random


def escape_cnt():
    cnt = 0
    while 1 == 1:
        rand = random.randint(1, 100)
        if rand in (1, 100):
            break
        else:
            cnt = cnt + 1

    return cnt


def random_pick(s_number: int, e_number: int):
    temp_list = list(range(s_number, e_number + 1))
    res_list = []

    while len(temp_list) > 0:
        rand = random.randint(0, len(temp_list) - 1)
        res_list.append(temp_list[rand])
        del temp_list[rand]

    return res_list


print(f"{'난수 생성하기':=^64}")
print("0 ~ 1 난수 생성 :", random.random())
print("1 ~ 100 난수 생성 : ", random.randint(1, 100))
print("1 ~ 100 난수 사이 '1' 혹은 '100'이 %d번만에 나왔습니다." % escape_cnt())
print("숫자 카드를 무작위로 꺼내보다 : %s" % random_pick(11, 20))

choice_test_list = [10, 20, 30, 40, 50]
print("%s 중에서 %d을 뽑았습니다!" % (choice_test_list, random.choice(choice_test_list)))

