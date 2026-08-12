"""
    날짜(Datetime) 라이브러리 사용 예제
"""

import datetime as datetime

print(f"\n{'날짜 차이 계산하기':=^64}")
start_date = datetime.date(2026, 3, 24)
end_date = datetime.date(2026, 3, 29)
print(f"시작일 : {start_date}")
print(f"종료일 : {end_date}")
print(f"일수 차이는 {(end_date - start_date).days}일 입니다.")
