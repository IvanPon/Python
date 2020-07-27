
class Road:
    def __init__(self,_length,_width):
        self._length=_length
        self._width=_width

    def weight (self, _length, _width):
        m=(_length*_width*25*5)/1000
        print (f'Требуемая масса aсфальта для укладки дороги длиной {_length} м. и шириной {_width} м. составляет - {m} тонн')

m=Road(5000,20)
m.weight(5000,20)
