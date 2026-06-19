"""
    문자열(String) 기초 예시 코드
"""


def print_hello_world():
    """
    "Hello world!"를 출력한다.
    :return: 없음
    """
    print("Hello world!")


def print_textarea_normal():
    """
    개행 문자가 포함된 고정 문자열을 출력한다. (일반적인 개행 방식)
    :return: 없음
    """
    res = "Hello? How's it going?" + "\n"
    res += "Could you repeat your name?" + "\n"
    res += "No problem, Have a good day." + "\n"
    res += "Were you pretending to be poor? "
    print(res)


def print_textarea_sql():
    """
    개행 문자가 들어간 고정 문자열을 출력한다. (가독성을 위한 방식)
    :return: 없음
    """

    res = """
        SELECT *
          FROM TABLE_SAMPLE
         WHERE SEQ = 1
        ;
    """
    print(res)


def print_direction(s: str, is_reverse: bool):
    """
    문자열을 그대로 출력하거나 거꾸로 출력한다. (문자열 인덱싱 예시)
    :param s: 입력 문자열
    :param is_reverse: 거꾸로 출력 여부
    :return: 없음
    """
    i, s_len = 0, len(s)
    res = ""
    while i < s_len:
        if not is_reverse:
            res += s[i]
        else:
            res += s[(s_len - 1) - i]
        i += 1
    print(res)


def print_range(s: str, i_start: int, i_end: int):
    """
    범위에 속한 문자열만 출력한다. (문자열 슬라이싱 예시)
    :param s: 입력 문자열
    :param i_start: 시작 인덱스
    :param i_end: 종료 인덱스
    :return: 없음
    """
    print(s[i_start:i_end])


def print_self_introduction(name: str, age: int, hobby: str):
    """
    인적사항을 입력받아 자기소개하는 문장을 출력한다. (문자열 포매팅 예시)
    :param name: 이름
    :param age: 나이
    :param hobby: 취미
    :return: 없음
    """
    res = "Hello? my name is {0}\n".format(name)
    res += "I'm {s_age} years old and my favorite hobby is {s_hobby}. ".format(s_age=age, s_hobby=hobby)
    res += "I love it!"
    print(res)


def print_your_grade(name: str, chance: float):
    """
    이름과 확률을 입력받아 출력한다. (소수 및 '%' 출력법)
    (참고) 소숫점 포맷팅의 경우 반올림 처리된다.
    :param name: 이름
    :param chance: 확률
    :return: 없음
    """
    print("%s, your chance of getting a job is %0.2f%%." % (name, chance))
    print("{0}, your chance of getting a job is {1:0.2f}%.".format(name, chance))


def print_sort_price(name: str, price: int):
    """
    금액을 입력받아 왼쪽/오른쪽 정렬된 상태로 출력한다.
    :param name: 이름
    :param price: 금액
    :return: 없음
    """
    res = "Welcome back, %-10s!!!" % name + "\n"
    res += "Those costs total %10d won." % price
    print(res)


def print_word():
    """
    여러 가지 정렬 방식을 이용하여 문장을 문서 형식으로 출력한다.
    :return: 없음
    """
    res = "{0:=^64}\n".format("")
    res += "{0:^64}\n".format(" Find my hat at the cafe. ")
    res += "{0:=^64}\n".format("")
    res += "{0:>64}\n".format("Author: Louis")
    res += "{0:>64}\n".format("Date: 2026-06-19")
    res += "{0:<64}\n".format("Louis stayed at a cafe thirty minutes ago.")
    res += "{0:<64}\n".format("Louis lost his hat. he was so upset.")
    res += "{0:<64}\n".format("Louis walked around the street for a few minutes, thinking.")
    res += "{0:<64}\n".format("Louis visited the cafe again, and finally he found his hat.")
    print(res)


def print_word_with_f(name: str, price: int, discount: float):
    """
    f 문자열 포맷팅을 이용하여 출력한다.
    :param name: 이름
    :param price: 가격
    :param discount: 할인
    :return: 없음
    """
    res = f"Welcome back! {name}. How can I help you?\n"
    res += f"These oranges are {discount:.2f}% off, so they cost {(price - (price / discount)):8.0f} Won.\n"
    print(res)


def print_multi(sentence: str, multi: int):
    """
    문장을 multi 수만큼 반복 출력한다.
    :param sentence: 문장
    :param multi: 반복 수
    :return: 없음
    """
    print(sentence * multi)


# 출력 테스트 (라이브러리화 시에는 제거할 것)
str_sample = "Hello world hahaha!!"
print_hello_world()
print_textarea_normal()
print_textarea_sql()
print_direction(str_sample, False)
print_direction(str_sample, True)
print_self_introduction("Anna", 21, "Camping")
print_your_grade("Eric", 85.727)
print_sort_price("Brian", 50000)
print_word()
print_word_with_f("Jack", 50000, 12.575)
print_multi("Good evening!\n", 3)
