"""
    자료 구조 (Data Structure) 관련 내장 함수
"""


# enumerate()
def print_index_and_value(input_list: list):
    """
        입력받은 리스트를 열거하여 (인덱스, 값) 형태로 출력하기

        :param input_list: 리스트
    """
    print(f"\n{' 리스트를 열거형(enumerate)으로 만들고 출력하기 ':=^64}")
    temp = enumerate(input_list)
    for idx, value in temp:
        print(f"temp[{idx}] = {value}")


# filter()
def print_even_only(input_list: list):
    """
        입력받은 리스트의 값 중 짝수인 것만 출력하기 (filter 내장 함수 이용)

        :param input_list: 리스트
    """

    def even_check(val: int):
        return val % 2 == 0

    print(f"\n{' 입력받은 리스트 중 짝수만 출력하기 (filter 이용) ':=^64}")
    print(f"before : {input_list}")
    print(f"after : {list(filter(even_check, input_list))}")


# range()
def print_three_multiple():
    """
        반복문을 이용하여 3의 배수를 출력하는 로직
    """
    print(f"\n{' 반복문으로 3의 배수 출력하기 ':=^64}")
    for v in range(3, 101, 3):
        print(v, end=", ")
    print("")

# sorted()
def print_sort_data(input_list: list):
    """
        입력받은 리스트의 데이터를 정렬하여 출력

        :param input_list: 리스트
    """
    print(f"\n{' 데이터 정렬 ':=^64}")
    print(f"before : {input_list}")
    print(f"after : {sorted(input_list)}")


# zip()
def merge_each_data(a_list: list, b_list: list):
    """
        동일한 개수의 리스트 2개를 인덱스별로 각각 합치는 로직 (행렬 연산 처럼)

        :param a_list: A 리스트
        :param b_list: B 리스트
    """
    print(f"\n{' 리스트 각각 합치기 ':=^64}")
    print(f"A : {a_list}")
    print(f"B : {b_list}")
    print(f"result : {list(zip(a_list, b_list))}")


if __name__ == "__main__":
    print_index_and_value([100, 101, 200, 300])
    print_even_only([5, 6, 7, 8, 9, 10, 11, 12, 19, 20])
    print_three_multiple()
    print_sort_data([26, 3, 55, 102, 599, 1024, -87])
    merge_each_data([10, 20, 30], [5, 7, 9])
