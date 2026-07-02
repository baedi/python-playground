"""
    파일 입출력(File Input/Output) 예시 코드
"""


def file_write_content(path: str, file_name: str):
    """
    파일을 불러와서 새로운 내용을 파일에 쓰기(저장)하는 함수
    :param path: 파일 위치(경로)
    :param file_name: 파일명(확장자 포함)
    """
    print("{0:=^64}".format(" file_write_content() "))
    file_object = open(f"{path}/{file_name}", "w")

    for v in range(1, 4):
        file_object.write(f"Number {v}.\n")

    file_object.close()


def file_add_content(path: str, file_name: str):
    """
    파일을 불러와서 내용을 추가하는 함수
    :param path: 파일 위치(경로)
    :param file_name: 파일명(확장자 포함)
    """
    print("{0:=^64}".format(" file_add_content() "))
    file_object = open(f"{path}/{file_name}", "a")

    for v in range(4, 6):
        file_object.write(f"New Number {v}!\n")

    file_object.close()


def file_read_and_print(path: str, file_name: str):
    """
    특정 파일을 읽어서 콘솔에 출력해주는 함수 (readline() 함수 예제)
    :param path: 파일 위치(경로)
    :param file_name: 파일명(확장자 포함)
    """
    print("{0:=^64}".format(" file_read_and_print() "))
    file_object = open(f"{path}/{file_name}", "r")

    while True:
        line = file_object.readline()
        if not line:
            break

        print(line, end="")  # 읽어온 문자열에 줄바꿈(\n)이 포함되어 있어 이렇게 처리함.

    file_object.close()


def file_read_and_print2(path: str, file_name: str):
    """
    특정 파일을 읽어서 콘솔에 출력해주는 함수 (readlines() 함수 예제)
    :param path: 파일 위치(경로)
    :param file_name: 파일명(확장자 포함)
    """
    print("{0:=^64}".format(" file_read_and_print2() "))
    file_object = open(f"{path}/{file_name}", "r")

    for v in file_object.readlines():
        print(v.strip())  # 줄바꿈 문자열 제거

    file_object.close()


def file_read_and_print3(path: str, file_name: str):
    """
    특정 파일을 읽어서 콘솔에 출력해주는 함수 (read() 함수 예제)
    :param path: 파일 위치(경로)
    :param file_name: 파일명(확장자 포함)
    """
    print("{0:=^64}".format(" file_read_and_print3() "))
    file_object = open(f"{path}/{file_name}", "r")
    print(file_object.read())

    file_object.close()


def file_read_and_print4(path: str, file_name: str):
    """
    특정 파일을 읽어서 콘솔에 출력해주는 함수 (파일 객체를 이용하여 출력하는 예제)
     + with open ... as obj 를 이용하면 해당 블록 내에서만 파일 객체를 사용할 수 있다. (파일 닫아줄 필요 없음)
    :param path: 파일 위치(경로)
    :param file_name: 파일명(확장자 포함)
    """
    print("{0:=^64}".format(" file_read_and_print4() "))
    with open(f"{path}/{file_name}", "r") as file_object:
        for v in file_object:
            print(v.strip())


# 테스트용 (직접 실행 시 호출)
if __name__ == "__main__":
    input_path = "../../../temp"  # (중요) 이 프로젝트에 temp 디렉토리 생성 필요
    input_file_name = "hello.txt"
    file_write_content(input_path, input_file_name)
    file_read_and_print(input_path, input_file_name)
    file_read_and_print2(input_path, input_file_name)
    file_add_content(input_path, input_file_name)
    file_read_and_print3(input_path, input_file_name)
    file_read_and_print4(input_path, input_file_name)
