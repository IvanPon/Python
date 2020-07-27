class Car:

    def __init__(self,speed,color,name,is_polise):
        self.speed=speed
        self.color=color
        self.name=name
        self.is_polise=is_polise

    def go(self):
        print("Машина поехала")

    def stop(self):
        print('Машина остановилась')

    def turn(self,direction):
        if direction=='right':
            print('Машина повернула направо')
        elif direction=='left':
            print('Машина повернула налево')

    def show_speed(speed):
        print(f'Скорость автомобиля равна: {speed}')

#------------------------------------------TownCar--------------------------------------------------------------------
class TownCar(Car):
    def __init__(self,speed,color,name,is_polise):
        super().__init__(speed,color,name,is_polise)

    def show_speed(self,speed):
        print(speed)
        if speed>60:
            print('Скорость превышена, максимальная скорость 60 км/ч')
        else:
            print(f'Скорость автомобиля равна: {speed}')

#------------------------------------------WorkCar--------------------------------------------------------------------
class WorkCar(Car):
    def __init__(self,speed,color,name,is_polise):
        super().__init__(speed,color,name,is_polise)

    def show_speed(self,speed):
        print(speed)
        if speed>40:
            print('Скорость превышена, максимальная скорость 40 км/ч')
        else:
            print(f'Скорость автомобиля равна: {speed}')

#----------------------------------------SportCar---------------------------------------------------------------------
class SportCar(Car):
    def __init__(self,speed,color,name,is_polise):
        super().__init__(speed,color,name,is_polise)

# ----------------------------------------PoliceCar---------------------------------------------------------------------
class PoliceCar (Car):
    def __init__(self, speed, color, name, is_polise):
        super().__init__(speed, color, name, is_polise)
    is_polise=True
#-----------------------------------------------------------------------------------------------------------------------

Lada=Car(50,'red','Lada',False)
Lada.go()
Lada.stop()
Lada.turn('right')
Lada.turn('left')
Car.show_speed(40)

Bus=TownCar(70,'green','Hynday',False)
Bus.show_speed(70)

Lorry=WorkCar(50,'Orange','Kamaz',False)
Lorry.show_speed(60)

Ferrari=SportCar(80,'red','Ferrari',False)
print(Ferrari.speed,Ferrari.color,Ferrari.name,Ferrari.is_polise)


PolCar=PoliceCar(120,'blue','Reno',True)
print(PolCar.speed,PolCar.color,PolCar.name,PolCar.is_polise)