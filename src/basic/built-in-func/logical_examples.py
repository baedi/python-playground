"""
    논리 연산 (Logical Operation) 관련 내장 함수
"""

# all()
print(f"{' 리스트의 값이 모두 참인지 체크 ':=^64}")

v_check1_1 = [1, 2, 3, 4, "5"]
print(f"{all(v_check1_1)} : {v_check1_1}")

v_check1_2 = [0] * 10
print(f"{all(v_check1_2)} : {v_check1_2}")

v_check1_3 = [1, 2, 5, 0, 4]
print(f"{all(v_check1_3)} : {v_check1_3}")

v_check1_4 = []
print(f"{all(v_check1_4)} : {v_check1_4}")


# any()
print(f"{' 리스트의 값이 하나라도 참인지 체크 ':=^64}")

v_check2_1 = [1, 2, 3, 4]
print(f"{any(v_check2_1)} : {v_check2_1}")

v_check2_2 = ["", "", 0, 100]
print(f"{any(v_check2_2)} : {v_check2_2}")

v_check2_3 = ["", "", 0, ""]
print(f"{any(v_check2_3)} : {v_check2_3}")

v_check2_4 = []
print(f"{any(v_check2_4)} : {v_check2_4}")