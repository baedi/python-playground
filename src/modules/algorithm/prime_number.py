"""
    소수(prime number) 처리를 위한 모듈
"""
import math


def check_prime_number(number: int):
    """
        입력한 값이 소수인지 판별하는 함수 (소수라면 True, 그렇지 않다면 False를 반환한다.)

        :param number: 입력값(숫자)
        :return: 소수 결과(부울)
    """
    result = True

    if number <= 1:
        return False

    for v in range(2, int(math.sqrt(number)) + 1):
        if number % v == 0:
            result = False
            break

    return result


def check_prime_number_bundle(*number: int):
    """
        입력한 값들이 소수인지 판별하여 딕셔너리로 결과를 반환

        :param number: 입력값(숫자, 튜플)
        :return: 소수 결과 (딕셔너리 - 숫자:부울)
    """
    res_dict = {}
    temp_set = set(number)

    for target in temp_set:
        res_dict[target] = check_prime_number(target)

    return res_dict


def make_sieve_of_eratos(max_number: int):
    """
        입력한 숫자 범위 내에서 에라토스테네스의 체를 만들어주는 함수
        (0부터 입력값까지의 모든 소수 여부를 리턴해준다.)

        :param max_number: 최대값(숫자)
        :return: 소수 결과 (리스트 - 부울)
    """
    prime_list = [True] * (max_number + 1)
    prime_list[0], prime_list[1] = False, False

    for i in range(2, max_number + 1):
        if not prime_list[i]:
            continue

        prime_list[i] = True
        j = i + i
        while j < max_number + 1:
            prime_list[j] = False
            j = j + i

    return prime_list


def find_original_prime(number: int):
    """
        입력한 숫자가 소수가 아니면 어떤 소수에서 걸리는지 출력하는 함수
        (소수라면 1을 출력하고 그렇지 않다면 최솟값 소수를 반환한다.)

        :param number: 입력값(숫자)
        :return: 소수 최솟값
    """
    if number <= 0:  # 0 이하이면 -1 반환
        return -1
    if number % 2 == 0:  # 짝수는 2 반환
        return 2

    i = 3
    while i < int(math.sqrt(number)) + 1:
        if number % i == 0:
            return i
        i = i + 2

    return 1
