class Stationery:
    title=None
    def draw (self):
        print('Запуск отрисовки')

class pen(Stationery):
    def draw (self):
        print('Рисуем ручкой')

class pencil(Stationery):
    def draw (self):
        print('Рисуем карандашем')

class handle(Stationery):
    def draw (self):
        print('Рисуем маркером')

a=Stationery()
a.draw()

p=pen()
p.draw()

penc=pencil()
penc.draw()

h=handle()
h.draw()


