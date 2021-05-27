class Car:

    speed: float
    color: str
    name: str
    is_police: bool

    def go(self):
        return print('GO')

    def stop(self):
        return print('STOP')

    def turn(self, direction):
        return print(f'MOVE {direction}')

    def show_speed(self):
        return self.speed


class PoliceCar(Car):
    is_police = True
    name = 'SKODA'
    color = 'Белая'
    speed = 120.0

class TownCar(Car):
    is_police = False
    name = "Ваз"
    color = "Зеленый"
    speed = 90.0

    def show_speed(self):
        if self.speed > 60:
            return 'Превышена скорость!! ' + str(self.speed)
        return str(self.speed)

class WorkCar(Car):
    is_police = False
    name = 'МАЗ'
    color = 'Красный'
    speed = 90.0

    def show_speed(self):
        if self.speed > 40:
            return 'Превышена скорость!! ' + str(self.speed)
        return str(self.speed)

class SporCar(Car):
    is_police = False
    name = 'FERRARI'
    color = 'Красный'
    speed = 200.0



tc = TownCar()
pc = PoliceCar()
sc = SporCar()
wc = WorkCar()

print(tc.__dict__)
print(pc.__dict__)
print(wc.__dict__)
print(sc.__dict__)

pc.go()
print(wc.turn(direction='Домой'))
sc.speed = 230

print(tc.__dict__)
print(pc.__dict__)
print(wc.__dict__)
print(sc.__dict__)