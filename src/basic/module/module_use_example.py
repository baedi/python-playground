# 모듈 import 방법
import src.modules.algorithm.prime_number as prime_number

# 모듈 import 방법 (모듈 이름 없이)
# 모든 함수를 쓰고 싶다면 '*'를 쓴다.
from src.modules.classes.ko_number_converter import KoNumberConverter
from src.modules.algorithm.prime_number import find_original_prime


value1 = 15
print(f"{value1} is", f"{'Prime Number!' if prime_number.check_prime_number(value1) else 'Not Prime Number.'}")

value2 = 93
print(f"{value2}'s original prime is {find_original_prime(value2)}.")


conv = KoNumberConverter()
ko_result = conv.convert_num_to_kr(54321032)
orig_result = conv.convert_kr_to_num(ko_result)
print(ko_result, orig_result)
