"""
    조건문(if) 예시 코드
"""


def print_can_buy_check(money: int, amount: int):
    """
    물건 구매 가능 여부 출력 (조건문 기본 사용)
    :param money: 소유 금액
    :param amount: 구매할 물건 수
    """
    price = 3000

    print("{0:=^64}".format("print_can_buy_check()"))
    if price * amount <= money:
        print('You successfully purchased the item. balance : %d' % (money - (price * amount)))
    else:
        print('Not enough money.')


def print_can_enter(age: int, is_friendly: bool):
    """
    나이와 부모 동반 여부를 입력받아 입장 가능 여부 출력 (조건문 활용, 다중 조건문)
    """
    print("{0:=^64}".format("print_can_enter()"))
    if age >= 14:
        print("You can go there!")
    elif not age >= 14 and is_friendly:
        print("You can go there with your family")
    else:
        print("You can't go there.")


def print_find_items(find_item: str, item_list: list):
    """
    찾고자 하는 물건이 있는지 체크 (리스트를 이용한 조건문)
    :param find_item: 찾고자 하는 물건
    :param item_list: 물건 목록
    """
    print("{0:=^64}".format("print_find_items()"))
    if find_item in item_list:
        print("You found some %s!" % find_item)
    else:
        print("You could not find any %s." % find_item)


def print_error_message(err_code: int):
    """
    에러 코드에 대한 메시지 출력 (다중 조건물 활용)
    :param err_code: 에러 코드
    """
    print("{0:=^64}".format("print_error_message()"))
    if err_code == 0:
        pass
    elif err_code == -50001:
        print("%s, Type definition error!" % err_code)
    elif err_code == -50002:
        print("%s, Duplicate error!" % err_code)
    else:
        print("Unknown error!")


def print_score_grade(score: int):
    """
    점수를 입력받아 등급을 출력하는 함수 (조건부 표현식 이용)
    :param score: 점수
    """
    print("{0:=^64}".format("print_if_expression()"))
    grade = "A" if score > 80 else (
        "B" if score > 70 else (
            "C" if score > 60 else (
                "D" if score > 50 else "F"
            )
        )
    )
    print(grade)


# 테스트용 (직접 실행 시 호출)
if __name__ == "__main__":
    print_can_buy_check(50000, 11)
    print_can_buy_check(50000, 20)
    print_can_enter(11, True)
    print_can_enter(11, False)
    print_can_enter(16, False)
    print_find_items('Grape', ['Apple', 'Banana', 'Grape'])
    print_find_items('Napkin', ['Fork', 'Sushi', 'Dish'])
    print_error_message(0)
    print_error_message(-50002)
    print_error_message(-50005)
    print_score_grade(99)
    print_score_grade(75)
    print_score_grade(49)
