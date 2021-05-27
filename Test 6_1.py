import time


class TrafficLight:
    color = 'red'

    def running(self):
        print('Светофор работает')

        self.color = 'red'
        print(f'Установлен цвет: {self.color}')
        time.sleep(7)

        self.color = 'yellow'
        print(f'Установлен цвет: {self.color}')
        time.sleep(2)

        self.color = 'green'
        print(f'Установлен цвет: {self.color}')
        time.sleep(5)

        while True:
            self.running()


traff_light = TrafficLight()
print(traff_light.running())