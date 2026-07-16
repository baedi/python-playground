"""
    파이썬 라이브러리 경로 확인하기
    - 파이썬 라이브러리가 설치되어 있는 디렉토리를 확인할 수 있다.
"""

import sys

path_list = sys.path
for path in path_list:
    print(path)