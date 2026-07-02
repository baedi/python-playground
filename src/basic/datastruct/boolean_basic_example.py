"""
    부울(boolean) 기초 예시 코드
"""


def print_bool_condition():
    """
    참/거짓의 다양한 조건들을 나타낸다.
    :return: 없음
    """
    bool_list = [
        True, False,
        1, 0,
        "Hello?", "",
        [0], [],
        (0,), (),
        {'a': 0}, {},
        (0 == 0), (1 == 0),
        (3 > 2), (100 < 50),
        None
    ]
    for target in bool_list:
        print("value : {0:12s}, type : {1:24s}, result : {2}".format(str(target), str(type(target)), bool(target)))


def print_list_items_sum(num_list: list):
    """
    리스트에 있는 요소들이 모두 비어있을 때까지 값을 꺼내서 합계를 구한다.
    :param num_list: 숫자 리스트(list)
    :return: 없음
    """
    res_sum = 0
    while num_list:
        res_sum += num_list.pop()
        print("current : %d" % res_sum)

    print("sum : %d" % res_sum)


# 테스트용 (직접 실행 시 호출)
if __name__ == "__main__":
    print_bool_condition()
    print_list_items_sum([10, 55, 32, 1, 7, 0, 9])
