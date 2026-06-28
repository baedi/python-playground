"""
    파일 인수(arguments) 예시 코드

    설명:
        프로그램 실행 시 입력한 인수값을 이용하여 처리하는 예시

    사용 방법 :
        콘솔(터미널) 창에서 "python {실행할 py 경로} {인수 1} {인수 2} ... {인수 n}" 을 입력한다.
            ex) python src/basic/inout/args_example.py Kevin 23 Fishing
"""

import sys


arguments = sys.argv[0:]
print("file path : %s" % arguments[0])

args_i = 1
for v in arguments[1:]:
    print(f"args {args_i} : {v}")
    args_i += 1

