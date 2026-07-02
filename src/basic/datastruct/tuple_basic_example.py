"""
    튜플(Tuple) 기초 예시 코드

    (참고)
     - 튜플 내부 값은 리스트와 달리 변경, 삭제할 수 없다.
"""


def print_how_to_declare_tuple():
    """
    튜플의 다양한 선언 예시
    :return: 없음
    """
    tuple1 = ()
    tuple2 = (100,)  # 요소가 하나일 경우 ',' 안 붙으면 튜플로 인식 안 됨.
    tuple3 = (100, 200, 300)
    tuple4 = 400, 500
    print("%s %s %s %s" % (tuple1, tuple2, tuple3, tuple4))


def print_tuple_example():
    """
    튜플의 다양한 예시
    :return: 없음
    """
    t = (1, 2, 3)
    t2 = t + (4, 5, 6, 7)
    t3 = t2 * 2
    print("%s (cnt : %d)" % (t3, len(t3)))
    print("t3[-8:] -> %s" % str(t3[-8:]))


# 테스트용 (직접 실행 시 호출)
if __name__ == "__main__":
    print_how_to_declare_tuple()
    print_tuple_example()
