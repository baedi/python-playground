class Animal:
    # 클래스 변수 (상수)
    type = "animal"

    # 생성자
    def __init__(self, name, age=None, weight=None):
        # 객체 변수
        self.name = name
        self.age = age
        self.weight = weight

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_weight(self):
        return self.weight

    def animal_sound(self):
        print(f"{self.name}({Animal.type}) cried ... ?")


class Dog(Animal):  # 부모 클래스 상속

    def __init__(self, name, age=None, weight=None):
        super().__init__(name, age, weight)

    def animal_sound(self):  # 오버라이딩 이용
        print(f"{self.name}({Animal.type}) cried ... Bark!!")


class Cat(Animal):  # 부모 클래스 상속

    def __init__(self, name, age=None, weight=None):
        super().__init__(name, age, weight)

    def animal_sound(self):  # 오버라이딩 이용
        print(f"{self.name}({Animal.type}) cried ... Meow~")


pet1 = Animal('Kang', 2, 12)
print(f"Hello? My pet's name is {pet1.get_name()}!")
pet1.animal_sound()

pet2 = Dog('Max', 3, 15)
pet2.animal_sound()

pet3 = Cat('Neko', 1, 5)
pet3.animal_sound()

# 클래스변수의 이름을 바꾸게 되면 모든 클래스의 객체에 영향을 준다.
Animal.type = "???"
pet1.animal_sound()
pet2.animal_sound()
pet3.animal_sound()
