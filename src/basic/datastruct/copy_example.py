"""
    얕은 복사(Shallow copy)와 깊은 복사(Deep copy) 예시 코드
"""


def example_shallow_copy():
    """
    얕은 복사(Shallow copy) 예시
    :return: 없음
    """
    a = [1, 2, 3]
    b = a
    b.append(100)
    print("a : %s (id : %d)" % (a, id(a)))
    print("b : %s (id : %d)" % (b, id(b)))


def example_deep_copy():
    """
    깊은 복사(Deep copy) 예시
    """
    a = [1, 2, 3]
    b = a[:]
    b.append(100)
    print("a : %s (id : %d)" % (a, id(a)))
    print("b : %s (id : %d)" % (b, id(b)))


example_shallow_copy()
example_deep_copy()
