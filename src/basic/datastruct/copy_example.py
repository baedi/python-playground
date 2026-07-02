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


# 테스트용 (직접 실행 시 호출)
if __name__ == "__main__":
    example_shallow_copy()
    example_deep_copy()
