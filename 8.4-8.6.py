class Storage:
    def __init__(self, type, price, quantity):
        self.type=type
        self.price=price
        self.quantity=quantity

    def __str__(self):
        return f'Вид - {self.type} Стоимость - {self.price} Количество - {self.quantity} '

class office_equipment(Storage):
    def __init__(self, type, price, quantity, name):
        super().__init__(type, price, quantity)
        self.name=name

    def __str__(self):
        return f'Вид - {self.type} Стоимость - {self.price} Количество - {self.quantity} Марка {self.name}'

class printer (office_equipment):
    def __init__(self, type, price, quantity, name, model):
        super().__init__(type, price, quantity, name)
        self.model = model

    def __str__(self):
        return f'Вид - {self.type} Стоимость - {self.price} Количество - {self.quantity} Марка {self.name} Модель {self.model}'

class scan (office_equipment):
    def __init__(self, type, price, quantity, name, model):
        super().__init__(type, price, quantity, name)
        self.model = model
    def __str__(self):
        return f'Вид - {self.type} Стоимость - {self.price} Количество - {self.quantity} Марка {self.name} Модель {self.model}'


class copier (office_equipment):
    def __init__(self, type, price, quantity, name, model):
        super().__init__(type, price, quantity, name)
        self.model = model
    def __str__(self):
        return f'Вид - {self.type} Стоимость - {self.price} Количество - {self.quantity} Марка {self.name} Модель {self.model}'



pr=printer('Принтер',5000,10,'HP','T520')
print(pr)

sc=scan('Сканер',5000,10,'Canon','A100')
print(sc)

cop=copier('Копиравальный аппарат',5000,10,'Xerox','M300')
print(cop)