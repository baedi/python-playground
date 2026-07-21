"""
    사용자 정의 예외 처리(User Exception) 예시 코드
"""


class NoFuelException(Exception):
    pass


class NoBatteryException(Exception):
    def __str__(self):
        return "Your car is not work. please charge your car."


class Car:
    def __init__(self):
        self.fuel = 0
        self.battery = 0

    def fill_up_fuel(self, amount: int):
        self.fuel = min(self.fuel + amount, 100)

    def charge_battery(self, amount: int):
        self.battery = min(self.battery + amount, 100)

    def drive(self, use_fuel: int = 10, use_battery: int = 10):
        try:
            if self.fuel - use_fuel < 0:
                raise NoFuelException()
            if self.battery - use_battery < 0:
                raise NoBatteryException()

        except NoFuelException:
            print("Your car is not work. please fill up your car.")
        except NoBatteryException as e:
            print(e)

        else:
            self.fuel = self.fuel - use_fuel
            self.battery = self.battery - use_battery
            print("driving... (fuel : %d, battery : %d)" % (self.fuel, self.battery))


if __name__ == '__main__':
    elantra = Car()
    elantra.drive()
    elantra.fill_up_fuel(40)
    elantra.drive()
    elantra.charge_battery(30)
    elantra.drive()
    elantra.drive(30, 20)
    elantra.drive(1, 1)
