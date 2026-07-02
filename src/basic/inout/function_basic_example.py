"""
    함수(inout) 기초 에시 코드
"""


def print_time(hour: int, minute: int, second: int):
    """
    시, 분, 초를 입력받아 출력하는 함수

    :param hour: 시간
    :param minute: 분
    :param second: 초
    :return: 없음
    """
    print("{0:=^64}".format(" print_time() "))
    print(f"{hour}시간 {minute}분 {second}초 입니다.")


def get_sum(is_minus: bool, *value: int):
    """
    입력받은 수를 모두 합하여 총합을 리턴하는 함수
     - 인자 개수 상관없이 원하는 만큼 넣을 수 있다. (매개변수 앞에 '*'를 붙이면 입력받은 인자를 모아 튜플로 만들어준다.)

    :param is_minus: 음수 게산 여부
    :param value: 숫자 (인자)
    :return: 총합
    """
    print("{0:=^64}".format(" print_sum() "))
    res = 0
    for v in list(value):
        if not is_minus:
            res = res + v
        else:
            res = res - v

    return res


def print_introduce(**info: str):
    """
    키워드 매개변수를 이용하여 인적정보를 출력하는 함수.
     - 인자 개수 상관없이 원하는 만큼 Key=Value 형태로 넣을 수 있다.
       (매개변수 앞에 '**'를 붙이면 입력받은 인자를 모아 딕셔너리로 만들어준다.)
    :param info: 인적정보
    :return: 없음
    """
    print("{0:=^64}".format(" print_introduce() "))
    print(f"Hi! I'm {info['name']}, it's nice to see you.")
    print(f"My favorite hobby is {info['hobby']}!!")


def get_operations(v1: int, v2: int):
    """
    두 개의 수를 입력받아 사칙연산 결과를 반환하는 함수 (다중 리턴 함수)
    :param v1: 첫번째 수
    :param v2: 두번째 수
    :return: 결과값 (튜플)
    """
    print("{0:=^64}".format(" get_operations() "))
    return v1 + v2, v1 - v2, v1 * v2, v1 / v2


def print_kiosk(coffee: str, is_ice: bool = True, is_cream: bool = False):
    """
    커피 주문을 받아서 결과를 출력하는 함수 (매개변수에 디폴트 값 사용 에제)
    :param coffee: 커피 이름
    :param is_ice: 아이스 여부
    :param is_cream: 크림 추가 여부
    :return:
    """
    print("{0:=^64}".format(" print_kiosk() "))
    if is_ice and is_cream:
        print(f"주문하신 아이스 {coffee} (크림 추가) 나왔습니다.")
    elif is_ice and not is_cream:
        print(f"주문하신 아이스 {coffee} 나왔습니다.")
    elif not is_ice and is_cream:
        print(f"주문하신 핫 {coffee} (크림 추가) 나왔습니다.")
    else:
        print(f"주문하신 핫 {coffee} 나왔습니다.")


# 테스트용 (직접 실행 시 호출)
if __name__ == "__main__":
    print_time(hour=13, minute=29, second=55)
    print_time(second=15, minute=33, hour=21)  # 매개변수를 지정해서 넣는 것도 가능하다.
    print(get_sum(False, 1, 2, 3, 4, 5))
    print_introduce(name="Kevin", hobby="Chess")
    a = get_operations(33, 6)
    print(f"{a}")
    a, b, c, d = get_operations(37, 2)
    print(f"{a}, {b}, {c}, {d}")
    print_kiosk("아메리카노")
    print_kiosk("카페라떼", False, True)
    print_kiosk("콜드브루", None, None)

    # def 대신 lambda를 사용하여 함수를 호출하는 방식 (한 줄로 구성된 함수를 정의할 때 사용함)
    print_greeting = lambda name1, name2: print(f"Hello {name1}, I'm {name2}!")
    print_greeting("Anna", "John")
