"""
    딕셔너리(Dictionary) 기초 예시 코드
"""


def print_self_introduce():
    """
    딕셔너리 데이터를 참조하여 자기소개 출력
    :return: 없음
    """
    obj = {
        "name": "Anna",
        "age": 21,
        "gender": "Woman",
        "hobby": "cooking"
    }
    res = f"Hello? My name is {obj['name']} and I'm {obj['age']} years old.\n"
    res += f"My favorite hobby is {obj['hobby']}. Thank you."
    print(res)


def print_dictionary_manage():
    """
    딕셔너리 요소 추가/수정/삭제 테스트 (Before/After 출력)
    :return: 없음
    """
    info = {
        "name": "Chris",
        "email": None
    }
    print("Before : " + str(info))

    # Add & Modify & Remove
    info["email"] = "chris@test.com"
    info["nickname"] = "chris_official"
    del info["name"]
    print("After : " + str(info))


def find_key_with_tuple(key: tuple):
    """
    튜플을 Key로 삼아서 딕셔너리를 관리하는 예시
    (튜플은 한 번 정의하면 값을 변경할 수 없으므로 key로 사용 가능함.)
    :return: 없음
    """
    obj = {
        (0, 1): "Zero-One",
        (0, 2): "Zero-Two",
        (0, 3): "Zero-Three",
        (1, 1): "One-One",
        (1, 2): "One-Two"
    }
    if obj.get(key):
        print(str(key) + " -> " + str(obj[key]))
    else:
        print(str(key) + " -> Not found.")


def print_key_value(obj: dict):
    """
    key를 List로 변환하여 for 문으로 key : value 출력
    :param obj: 딕셔너리 입력
    :return: 없음
    """
    for key in list(obj.keys()):
        print(key + " : " + str(obj[key]))
    obj.clear()


def print_key_value2(obj: dict):
    """
    딕셔너리를 튜플 리스트로 가져온 뒤 for 문으로 key : value 출력
    :param obj: 딕셔너리 입력
    :return: 없음
    """
    for t in obj.items():
        print(t[0] + " : " + str(t[1]))
    obj.clear()


def print_key_exist_check(obj: dict, key: str):
    """
    딕셔너리에 특정 키가 유효한지 여부를 출력한다.
    :param obj: 딕셔너리 입력
    :param key: 딕셔너레에서 찾을 키 값
    :return: 없음
    """
    print("찾고자 하는 키 : " + str(key))
    if key in obj:
        print("Tier : " + str(obj[key]))
    else:
        print("No data.")


# 테스트용 (직접 실행 시 호출)
if __name__ == "__main__":
    print_self_introduce()
    print_dictionary_manage()
    find_key_with_tuple((0, 3))
    find_key_with_tuple((1, 5))
    print_key_value({"name": "Alex", "age": 24, "hobby": "music"})
    print_key_value2({"name": "Lux", "age": 32, "job": "insurance manager"})

    user_tier = {
        "Grace": "Bronze",
        "Alen": "Diamond",
        "Lua": "Unranked",
        "Hana": "Master"
    }
    print_key_exist_check(user_tier, "Alen")
    print_key_exist_check(user_tier, "Kyle")
