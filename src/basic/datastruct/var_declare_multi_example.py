"""
    변수 다중 선언 에시
"""


def example_multi_declare1():
    """
    여러 변수에 한 번에 값 할당하기 1
    :return: 없음
    """
    item1, item2, item3 = ("Hamburger", "Pizza", "Coke")
    print("{0} -> {1} -> {2}".format(item1, item2, item3))


def example_multi_declare2():
    """
    여러 변수에 한 번에 값 할당하기 2
    :return: 없음
    """
    [item1, item2, item3] = ["Hamburger", "Pizza", "Coke"]
    print("{0} -> {1} -> {2}".format(item1, item2, item3))


def value_change(a: int, b: int):
    """
    두 변수값을 서로 교환하는 예시
    :param a: 값 1
    :param b: 값 2
    :return: 없음
    """
    a, b = b, a
    print("a : %d, b : %d" % (a, b))


example_multi_declare1()
example_multi_declare2()
value_change(5, 10)
