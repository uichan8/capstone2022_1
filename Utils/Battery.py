import os
import time

class Battery:
    def __init__(self, level = 50):
        self.level = level
        self.charge_speed = 2
        self.discharge_speed = 1

    def charge(self, multiple = 1):
        self.level += self.charge_speed * multiple
        if self.level > 100:
            self.level = 100
        return self.level

    def discharge(self, multiple = 1):
        self.level -= self.discharge_speed * multiple
        if self.level < 0:
            self.level = 0
        return self.level
    
    def display_level(self):
        os.system("clear")
        print("0        10        20        30        40        50        60        70        80        90        100")
        print("[", end="")
        for i in range(self.level):
            print("#", end="")
        for i in range(100-self.level):
            print(" ", end="")
        print("]")
        print("Battery level : ", self.level)
        return self.level

    def return_level(self):
        return self.level

if __name__ == "__main__":
    a = Battery()
    a.print_level()
    for i in range(30):
        a.charge()
        a.print_level()
        time.sleep(1)

    for i in range(10):
        a.discharge()
        a.print_level()
        time.sleep(1)

