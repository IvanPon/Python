
class Worker:
    """Базовый класс для всех сотрудников"""

    worker_count = 0

    def __init__(self,name,surname,position,_income):
        self.name=name
        self.surname=surname
        self.position=position
        Worker._income=_income['wage']+_income['bonus']
        Worker.worker_count += 1

class Position(Worker):
    def __init__(self,name,surname,position,_income):
        super().__init__(name,surname,position,_income)
        print(f'Имя: {self.name}. Фамилия - {self.surname}. Должность - {self.position} Зарплата: {self._income}')

dict1={"wage": 4000, "bonus": 3000}
dict2={"wage": 3000, "bonus": 2000}
work1 = Position("Андрей","Иванов","Директор",dict1)
work2 = Position("Анна","Петрова","Бухгалтер",dict2)

print (f'Всего сотрудников: {Worker.worker_count}')

