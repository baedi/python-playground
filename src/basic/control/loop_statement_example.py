"""
    반복문(loop) 예시 코드
"""


def print_all_items(items: list):
    """
    리스트에 담겨 있는 모든 요소들을 출력하는 함수 (while문 이용)
    :param items: 품목 리스트
    """
    idx = 0
    print("{0:=^64}".format("print_all_items_with_while()"))
    while idx < len(items):
        print("%d : %s" % (idx + 1, items[idx]))
        idx = idx + 1


def print_two_divide(value: int):
    """
    수가 주어지면 3으로 나누어 떨어질 때까지 2로 계속 나누는 함수 (break문 이용)
    :param value: 값
    """
    print("{0:=^64}".format("print_two_divide()"))
    while value > 1:
        if value % 3 == 0:
            break
        value = int(value / 2)
    print("result : %d" % value)


def print_three_multiples(max_value: int):
    """
    1부터 최댓값 범위 내에 3의 배수에 해당하는 값들을 리스트에 담아서 출력한다. (continue 이용)
    :param max_value: 최댓값
    """
    cur = 0
    res = []
    while cur < max_value:
        cur = cur + 1
        if cur % 3 != 0:
            continue
        res.append(cur)
    print("{0:=^64}".format("print_three_multiples()"))
    print(f"1 ~ {max_value} :: {res}")


def print_odd_even_cnt(num_list: list):
    """
    숫자가 들어간 리스트를 반복문으로 확인하여 짝수, 홀수 개수를 출력한다.
    :param num_list: 숫자 리스트
    """
    odd, even = 0, 0
    for num in num_list:
        if num % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    print("{0:=^64}".format("print_odd_even_cnt()"))
    print("odd : %d, even : %d" % (odd, even))


def print_vector3(vector_list: list):
    """
    3차원 좌표로 표현된 튜플을 반복문을 이용하여 출력하기
    :param vector_list: 3차원 튜플이 들어간 리스트
    :return:
    """
    print("{0:=^64}".format("print_vector3()"))
    for (x, y, z) in vector_list:
        print("x: %.1f, y: %.1f, z: %.1f" % (x, y, z))


def print_four_multiples(start: int, end: int):
    """
    시작값 ~ 종료값 사이의 값들 중에서 4배수에 해당하는 값들만 리스트에 담아서 출력한다. (range 함수 이용)
    :param start: 시작값
    :param end: 종료값
    """
    res = []
    for v in range(start, end + 1):
        if v % 4 == 0:
            res.append(v)
    print("{0:=^64}".format("print_four_multiples()"))
    print(f"{start} ~ {end} :: {res}")


def print_change_the_sign(num_list: list):
    """
    입력한 숫자들 중에서 짝수인 것만 부호를 변경하는 로직 (리스트 컴프리헨션 사용 예)
    :param num_list: 숫자 리스트
    """
    result = [
        v * -1 for v in num_list if v % 2 == 0
    ]
    print("{0:=^64}".format("print_change_the_sign()"))
    print(result)


print_all_items(["Apple", "Banana", "Kiwi", "Grape"])
print_two_divide(100)
print_three_multiples(25)
print_odd_even_cnt([1, 55, 23, 50, 14, 22, 19])
print_vector3([(1, 2, 3), (10, 52, 0.9), (-12, -22.5, 13)])
print_four_multiples(25, 99)
print_change_the_sign([5, -10, 12, -103, 55, 678, -119])
