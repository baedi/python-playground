"""
    예외 처리(Exception) 기초 예시 코드
"""


def divide_value(a: str, b: str):
    """
        입력한 문자열을 Int형 숫자로 변환 후 나누기 결과를 출력하는 함수

        :param s_input: 문자열
    """
    res = None
    try:
        i_val1 = int(a)
        i_val2 = int(b)
        res = i_val1 / i_val2

    except ValueError as e:
        print(f"Input value is not number format. :: {e}")

    except ZeroDivisionError:
        print("Divide error! Don't use zero as the denominator")

    finally:
        if res is not None:
            res = format(res, ".1f")

        print(f"{a} / {b} = {res}")


if __name__ == "__main__":
    v1 = input("분자값을 입력하세요 : ")
    v2 = input("분모값을 입력하세요 : ")
    divide_value(v1, v2)
