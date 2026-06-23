def q1_get_avg(d: dict):
    avg = 0
    score_list = d.items()
    for score in score_list:
        avg += score[1]
    print("{0:=^64}".format(" Q1 "))
    print(avg / len(score_list))


def q2_odd_even(v: int):
    print("{0:=^64}".format(" Q2 "))
    if v % 2 == 0:
        print("{0}은(는) 짝수 입니다.".format(v))
    else:
        print("{0}은(는) 홀수 입니다.".format(v))


def q3_pin_split(pin: str):
    print("{0:=^64}".format(" Q3 "))
    print(pin.split("-")[0])
    print(pin.split("-")[1])


def q4_get_gender(pin: str):
    print("{0:=^64}".format(" Q4 "))
    print("Gender : %s" % pin.split("-")[1][0])


def q5_replace_str(sentence: str):
    print("{0:=^64}".format(" Q5 "))
    print(sentence.replace(":", "#"))


def q6_reverse_list(v_list: list):
    v_list.sort()
    v_list.reverse()
    print("{0:=^64}".format(" Q6 "))
    print(v_list)


def q7_convert_list_to_str(v_list: list):
    v_str = ""
    for v in v_list:
        v_str += v + " "
    print("{0:=^64}".format(" Q7 "))
    print(v_str.strip())


def q8_add_tuple(t: tuple):
    t = t + (4,)
    print("{0:=^64}".format(" Q8 "))
    print(t)


def q9_dict_error_reason():
    print("{0:=^64}".format(" Q9 "))
    a = dict()
    a['name'] = 'python'
    a[('a',)] = 'python'
    #a[[1]] = 'python'  # 리스트 형태는 Key로 사용 불가능함. (리스트는 변경 가능한 요소이기 때문)
    a[250] = 'python'
    print(a)


def q10_print_dict_item():
    a = {'A': 90, 'B': 80, 'C': 70}
    result = a.pop('B')
    print(a)
    print(result)


def q11_remove_list_duplicate():
    a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
    a_set = set(a)
    b = list(a_set)
    print(b)


def q12_multiple_variable():
    a = b = [1, 2, 3]   # a, b는 모두 같은 리스트를 참조한다. (따라서 어떤 변수를 사용하든 결과는 동일하게 나타남.)
    a[1] = 4
    print(b)


q1_get_avg({'국어': 80, '영어': 75, '수학': 55})
q2_odd_even(13)
q3_pin_split('881120-1068234')
q4_get_gender('881120-1068234')
q5_replace_str("a:b:c:d")
q6_reverse_list([1, 3, 5, 4, 2])
q7_convert_list_to_str(['Life', 'is', 'too', 'short'])
q8_add_tuple((1, 2, 3))
q9_dict_error_reason()
q10_print_dict_item()
q11_remove_list_duplicate()
q12_multiple_variable()
