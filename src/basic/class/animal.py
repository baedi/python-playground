class Animal:
    def __init__(self, name, age=None, weight=None):
        self.name = name
        self.age = age
        self.weight = weight

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_weight(self):
        return self.weight


pet1 = Animal('Kang', 2, 12)
print(f"Hello? My pet's name is {pet1.get_name()}!")
