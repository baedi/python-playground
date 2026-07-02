"""
    집합(set) 기초 예시 코드
"""


def print_set():
    """
    집합(set)의 기본 정의
    :return: 없음
    """
    s = {1, 2, 3}
    print(type(s))
    print(s)


def conv_str_to_set(s: str):
    """
    문자열을 set으로 변환해주는 함수
    :param s: 문자열
    :return: 집합(set)
    """
    return set(s)


def conv_set_to_list(d: set):
    """
    set을 리스트로 변환해주는 함수
    :param d: 집합(set)
    :return: 리스트(list)
    """
    return list(d)


def print_set_operation():
    """
    두 개의 set을 이용하여 교집합, 합집합, 차집합을 나타낸다.
    :return: 없음
    """
    s1 = {100, 150, 200, 250, 300}
    s2 = {5, 100, 200, 1000, 5000}

    print(f"s1 : {s1}")
    print(f"s2 : {s2}")
    print("교집합 : %s" % str(s1 & s2))  # s1.intersection(s2)
    print("합집합 : %s" % str(s1 | s2))  # s1.union(s2)
    print("차집합 : %s" % str(s1 - s2))  # s1.difference(s2)


def control_set(d: set, mode: int, target):
    """
    집합(set)에 요소를 추가, 제거하기
    :param d: 집합(set)
    :param mode: 모드 (1:삽입, 5:다중삽입, -1:삭제)
    :param target: 삽입 혹은 삭제할 요소
    :return:
    """
    print("before set : %s" % d)
    if mode == 1:
        print(" - add %s" % target)
        d.add(target)
    elif mode == 5:
        print(" - update(multi add) %s" % target)
        d.update(target)
    elif mode == -1:
        print(" - remove %s" % target)
        d.remove(target)
    print("after set : %s" % d)
    print("{0:=^64}".format(""))


# 테스트용 (직접 실행 시 호출)
if __name__ == "__main__":
    print_set()
    print(conv_str_to_set("Hello world!"))
    print(conv_set_to_list({1, 2, 3}))
    print_set_operation()

    test_set = {1, 2, 3}
    control_set(test_set, 1, 5)
    control_set(test_set, 5, {10, 11, 12})
    control_set(test_set, -1, 11)
