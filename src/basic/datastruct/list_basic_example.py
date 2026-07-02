"""
    리스트(List) 기초 예시 코드

    (참고)
     - 리스트 내부 값은 변경 가능하다.
"""


def print_list():
    """
    리스트에 다양한 타입의 값을 담은 요소들을 하나씩 출력한다.
    :return: 없음
    """
    ex_list = [100, "Good", 3.14, True, [1, 2, 3]]
    for ex in ex_list:
        print(ex)


def print_list_range_sum():
    """
    리스트에 슬라이싱 기법을 적용하여 구간 합 구하기
    :return: 없음
    """
    ex_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    s = 0
    for ex in ex_list[3:-2]:
        s += ex
    print(s)


def print_list_merge():
    """
    리스트 합치기 예시
    :return: 없음
    """
    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8]
    print("a : %s" % a)
    print("b : %s" % b)
    print("merge : %s" % (a + b))


def print_list_multi():
    """
    리스트 반복 예시
    :return: 없음
    """
    a = [100, 200, 300]
    print(a * 3)


def print_list_delete():
    """
    리스트 삭제 예시
    :return: 없음
    """
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("before : %s (ea : %d)" % (a, len(a)))
    del a[7:]
    print("after : %s (ea : %d)" % (a, len(a)))


def print_list_function_test():
    """
    다양한 리스트 함수 사용 예시
    :return: 없음
    """
    a = [100, 200, 300, 400, 500, 200, 200]
    a.insert(2, 10)  # 특정 구간에 요소 추가
    a.append(50)  # 뒤에 요소 추가
    a.remove(200)  # 특정 값 삭제 (가장 처음 나오는 것)
    a.extend([-1, -2, -3])  # 리스트 확장
    a.sort()  # 정렬
    a.reverse()  # 뒤집기
    a[2] = 350  # 리스트 값 변경
    print(a)
    print("pop : %d" % a.pop())  # 마지막 값 꺼내기
    print("200 cnt : %d" % a.count(200))  # 특정 값 개수 출력


# 테스트용 (직접 실행 시 호출)
if __name__ == "__main__":
    print_list()
    print_list_range_sum()
    print_list_merge()
    print_list_multi()
    print_list_delete()
    print_list_function_test()
