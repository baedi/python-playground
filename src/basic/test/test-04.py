import sys


def q1_is_odd(number):
    print("{0:=^64}".format(" Q1 "))
    if number % 2 != 0:
        return True
    else:
        return False


def q2_avg_numbers(*args):
    print("{0:=^64}".format(" Q2 "))
    result = 0
    for i in args:
        result += i
    return result / len(args)


def q3_input_and_plus():
    print("{0:=^64}".format(" Q3 "))
    input1 = input("Please input first number : ")
    input2 = input("Please input second number : ")

    total = int(input1) + int(input2)
    print("result sum : %d" % total)


def q4_find_different_print():
    print("{0:=^64}".format(" Q4 "))
    print("You" "Need" "More" "Practice")
    print("You" + "Need" + "More" + "Practice")
    print("You", "Need", "More", "Practice")  # 콤마로 하나씩 쓰면 띄어쓰기됨 (이것만 다름)
    print("".join(["You", "Need", "More", "Practice"]))


def q5_fix_file_input():
    print("{0:=^64}".format(" Q5 "))
    f1 = open("../../../temp/test-04_example05.txt", "w")
    f1.write("Hello python world!!")
    f1.close()  # 파일을 불러오고 나서 반드시 close 해줘야 됨. (안 그러면 다시 읽어올 때 예상치 못한 문제 발생)

    f2 = open("../../../temp/test-04_example05.txt", "r")
    print(f2.read())


def q6_write_file():
    print("{0:=^64}".format(" Q6 "))
    user_input = input("Please enter the content you want to save : ")
    f = open("../../../temp/test-04_example06.txt", "a")
    f.write(user_input)
    f.write("\n\n\n")
    f.close()


def q7_replace_word():
    # 우선 파일을 미리 만든다.
    make_obj = open("../../../temp/test-04_example07.txt", "w")
    make_obj.write("Life is too short\nyou need java")
    make_obj.close()

    f = open("../../../temp/test-04_example07.txt", "r")
    body = f.read()
    f.close()
    body = body.replace("java", "python")
    f = open("../../../temp/test-04_example07.txt", "w")
    f.write(body)
    f.close()


def q8_sum_all_values():
    # 해당 기능이 제대로 동작하려면 console 창에서 인자를 줘야 됨. (모두 숫자로)
    # 예: python src/basic/test/test-04.py 1 2 3 4
    args = sys.argv[1:]
    v_sum = 0
    for n in args:
        v_sum += int(n)

    return v_sum


print(q1_is_odd(3))
print(q1_is_odd(4))
print(q2_avg_numbers(1, 2))
print(q2_avg_numbers(1, 2, 3, 4, 5))
# q3_input_and_plus()
q4_find_different_print()
# q5_fix_file_input()
# q6_write_file()
# q7_replace_word()
print(q8_sum_all_values())
