"""
    사칙연산을 처리해주는 계산기 클래스
"""


class FourCal:
    def __init__(self):
        self.v1 = 0
        self.v2 = 0

    def set_data(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def add(self):
        return self.v1 + self.v2

    def mul(self):
        return self.v1 * self.v2

    def sub(self):
        return self.v1 - self.v2

    def div(self):
        return self.v1 / self.v2


a = FourCal()
a.set_data(4, 2)
print("v1 : " + str(a.v1))
print("v2 : " + str(a.v2))
print(a.add())  # 객체.메소드() 형태의 경우 self에는 자동으로 객체 a가 들어가게 된다.
print(a.mul())
print(FourCal.sub(a))  # 이런 형태로도 호출할 수 있다. (클래스명.메소드() 형태, 이 경우는 self에 들어갈 인자를 넣어야 함.)
print(FourCal.div(a))
