"""
    시간(Time) 라이브러리 사용 예제
"""

import time as time

today_time = time.time()
today_localtime = time.localtime(today_time)
today_asctime = time.asctime(today_localtime)

print(f"{'time 라이브러리로 현재시간 표현하기':=^64}")
print(f"실수값 : {today_time}")
print(f"날짜 표현 : {today_localtime}")
print(f"간결한 날짜 표현 1 : {today_asctime}")
print(f"간결한 날짜 표현 2 : {time.ctime()}")

today_format = time.strftime('%Y-%m-%d %H:%M:%S', today_localtime)
print(f"yyyy-MM-dd hh:mm:ss 형태로 날짜 표현 : {today_format}")

# 1초동안 딜레이
time.sleep(1)
print("Done!")
