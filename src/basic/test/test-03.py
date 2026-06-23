def q1_true_and_false():
    print("{0:=^64}".format(" Q1 "))
    a = "Life is too short, you need python"
    if "wife" in a:
        print("wife")
    elif "python" in a and "you" not in a:
        print("python")
    elif "shirt" not in a:
        print("shirt")  # 출력됨
    elif "need" in a:
        print("need")
    else: print("none")


def q2_sum_three_multiples():
    result = 0
    i = 1
    while i <= 1000:
        if i % 3 == 0:
            result += i
        i += 1

    print("{0:=^64}".format(" Q2 "))
    print(result)


def q3_make_star():
    i = 0
    print("{0:=^64}".format(" Q3 "))
    while True:
        i += 1
        if i > 5:
            break
        print(("{0:*^" + str(i) + "}").format("*"))


def q4_print_one_to_hundred():

    print("{0:=^64}".format(" Q4" ))
    for i in range(1, 100 + 1):
        print(i)


def q5_score_avg():
    a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
    total = 0
    for score in a:
        total += score
    average = total / len(a)

    print("{0:=^64}".format(" Q5 "))
    print(average)


def q6_list_comprehension():
    numbers = [1, 2, 3, 4, 5]
    result = [v * 2 for v in numbers if v % 2 != 0]
    print("{0:=^64}".format(" Q6 "))
    print(result)


q1_true_and_false()
q2_sum_three_multiples()
q3_make_star()
q4_print_one_to_hundred()
q5_score_avg()
q6_list_comprehension()
