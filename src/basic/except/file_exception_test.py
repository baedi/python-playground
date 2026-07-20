"""
    예외 처리(Exception) 기초 예시 코드 2
"""


def open_and_write_file(path: str):
    """
        경로(Path)를 입력받아 해당 경로의 파일을 읽어서 출력하는 함수

        :param path: 파일 경로
    """
    file_obj = None
    try:
        file_obj = open(path, "r")
        for line in file_obj:
            print(line)

    except(FileNotFoundError, ValueError):
        print("Can't open a file. Try again.")

    else:
        print("File open success!")

    finally:
        if file_obj is not None:
            file_obj.close()


if __name__ == "__main__":
    path_str = input("파일 경로 입력 : ")
    open_and_write_file(path_str)
