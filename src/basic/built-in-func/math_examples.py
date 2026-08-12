"""
    수식 관련 내장 함수
"""

# abs()
print(f"\n{' 절댓값 구하기 ':=^64}")
v1_target = [5, 33, -17]
for v in v1_target:
    print(f"{v}의 절댓값은 {abs(v)} 입니다.")


# divmod()
print(f"\n{' 몫과 나머지 한번에 구하기 ':=^64}")
v2_high = 100
v2_low = 7
print(f"{v2_high}을 {v2_low}로 나눴을 때 몫과 나머지는 ... {divmod(v2_high, v2_low)}")


# eval()
print(f"\n{' 문자열로 된 수식을 계산하기 ':=^64}")
v3_str = "(3 + 2) * 5"
print(f"{v3_str} = {eval(v3_str)}")


# pow()
print(f"\n{' 제곱수 계산하기 ':=^64}")
v4_val = 12
print(f"{v4_val}^2 = {pow(v4_val, 2)}")


# round()
print("f\n{' 반올림 ':=^64}")
v5_list = [(12.55, 1), (33.44445, 2), (500.657, 0)]
for val, digit in v5_list:
    print(f"{val}을 {digit}번째 자리수까지 반올림하면? -> {round(val, digit)}")


# sum()
print(f"\n{' 모든 수 합치기 ':=^64}")
v6_list = [1, 2, 3, 4, 5]
print(f"{v6_list}를 모두 합하면 {sum(v6_list)}")
