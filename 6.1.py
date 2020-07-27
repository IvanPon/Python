import time

class TrafficLight:
    # Атрибуты:
    colour1='red'
    colour2='yellow'
    colour3='green'

    # методы:
    def running (self, colour1,colour2,colour3):
        TrafficLight.colour1 = colour1
        TrafficLight.colour2 = colour2
        TrafficLight.colour3 = colour3
        for i in range(2):
            print(colour1)
            time.sleep(7)
            print(colour2)
            time.sleep(2)
            print(colour3)
            time.sleep(7)

a = TrafficLight()
print (a.running('red','yellow','green'))
