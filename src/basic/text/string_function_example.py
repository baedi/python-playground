"""
    문자열(String) 함수 사용 예시 코드
"""


def print_alphabet_count(sentence: str):
    """
    입력한 문장의 각 알파벳 개수를 출력한다. (문자열 내장 함수 사용)
    :param sentence: 문장
    :return: 없음
    """
    i = 0
    check = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while i < len(check):
        cnt = sentence.upper().count(check[i])
        if cnt > 0:
            res = "{0:s} : {1:3d}".format(check[i], sentence.upper().count(check[i]))
            print(res)
        i = i + 1


def print_find_word(sentence: str, find_word: str):
    """
    입력한 문장에서 특정 단어를 찾는다. 찾았다면 최초 등장한 위치를 출력한다.
    find랑 비슷한 함수로 index가 있는데 차이점은 문자열을 못 찾았을 때 에러가 발생되느냐 차이.
    :param sentence: 문장
    :param find_word: 찾을 단어
    :return: 없음
    """
    print("find idx : %d" % sentence.find(find_word))


def print_trim(sentence: str):
    """
    입력한 문자열로 왼쪽/오른쪽/전체 공백을 지운 상태의 결과를 각각 출력한다.
    :param sentence: 문장
    :return: 없음
    """
    print(f"Left Trim : {sentence.lstrip()}")
    print(f"Right Trim : {sentence.rstrip()}")
    print(f"All Trim : {sentence.strip()}")


def print_split(sentence: str):
    """
    입력한 문자열을 공백으로 나누어 출력한다.
    :param sentence: 문장
    :return: 없음
    """
    for word in sentence.split(" "):
        print(word)


def print_replace(sentence: str, before: str, after: str):
    """
    입력한 문장에서 특정 문자열을 다른 걸로 바꿔준다.
    :param sentence: 문장
    :param before: 변경 전 문자열
    :param after: 변경 후 문자열
    :return:
    """
    print(sentence.replace(before, after))


def print_self_introduce2(name: str, age: int):
    """
    자기소개 멘트를 출력한다. (str 함수 활용)
    :param name: 이름
    :param age: 나이
    :return: 없음
    """
    print("Hello! my name is " + name + ", I'm " + str(age) + " years old.")


# 테스트용 (직접 실행 시 호출)
if __name__ == "__main__":
    # 출력 테스트 (라이브러리화 시에는 제거할 것)
    print_alphabet_count("Hello world hahahahaha!")
    print_find_word("Good morning sir!", "morning")
    print_trim("   o_O   ")
    print_split("What about you?")
    print_replace("What should I eat? I eat hamburgers", "eat", "bring")
    print_self_introduce2("Lisa", 17)
