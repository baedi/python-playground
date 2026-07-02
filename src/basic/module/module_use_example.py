"""
    모듈 사용 예제
     - 모듈을 선언하여 해당 모듈의 함수, 클래스, 변수들을 가져올 수 있다.
"""

# 모듈 import 방법
import src.modules.algorithm.prime_number as prime_number

# 모듈 import 방법 (모듈 이름 없이)
from src.modules.classes.ko_number_converter import KoNumberConverter, DIGIT_HUNDRED
from src.modules.algorithm.prime_number import *


value1 = 15
print(f"{value1} is", f"{'Prime Number!' if prime_number.check_prime_number(value1) else 'Not Prime Number.'}")

value2 = 93
print(f"{value2}'s original prime is {find_original_prime(value2)}.")


conv = KoNumberConverter()
ko_result = conv.convert_num_to_kr(54321032)
orig_result = conv.convert_kr_to_num(ko_result)
print(ko_result, orig_result)
print(DIGIT_HUNDRED)
