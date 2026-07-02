"""
    콘솔 입력(input) 기초 예시 코드
"""

def check_your_weight(weight: int):
    """
    몸무게를 입력받아 상태를 출력하는 함수
    :param weight: 몸무게
    :return: 없음
    """
    if weight >= 100:
        print("You are too fat. you need to diet hard!!")
    elif weight >= 80:
        print("You are fat. you need to diet more!")
    elif weight >= 60:
        print("You are normal. very nice!")
    elif weight >= 50:
        print("You are thin. it's okay.")
    else:
        print("You are too thin. are you okay?")


# 테스트용 (직접 실행 시 호출)
if __name__ == "__main__":
    weight = input("Input your weight : ")  # 콘솔 입력
    check_your_weight(int(weight))  # 콘솔로 입력받은 값은 문자열이므로 주의
