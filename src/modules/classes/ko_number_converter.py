"""
    숫자를 한글로 변환해주는 클래스
"""


class KoNumberConverter:
    KO_DIGIT = {0: "영", 1: "일", 2: "이", 3: "삼", 4: "사", 5: "오", 6: "육", 7: "칠", 8: "팔", 9: "구"}
    ORIG_DIGIT = {"영": 0, "일": 1, "이": 2, "삼": 3, "사": 4, "오": 5, "육": 6, "칠": 7, "팔": 8, "구": 9}

    def convert_num_to_kr(self, value: int):
        ko_value = ""
        number_str = str(value)

        for i in range(0, len(number_str)):
            ko_value += KoNumberConverter.KO_DIGIT[int(number_str[i])]

        return ko_value

    def convert_kr_to_num(self, ko_value: str):
        value = ""

        for i in range(0, len(ko_value)):
            value += str(KoNumberConverter.ORIG_DIGIT[ko_value[i]])

        return int(value)


