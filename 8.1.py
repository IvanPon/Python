
class Data:
    def __init__(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year

    @classmethod
    def set_date(cls,data):
        day, month, year = data
        return cls(day, month, year)

    @staticmethod
    def check_date(self):
        Month_dict = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if int(self.month) < 1 or int(self.month) > 12:
            print('Ошибка - колличество месяцев в году -12')
        else:
            if int(self.day) <= 0 or int(self.day) > Month_dict [int(self.month)]:
                print(f'Некорректный ввод даты  в {self.month}-м месяце нет {self.day}-го числа')
        return (f'{self.day}:{self.month}:{self.year} г.')


date=input('Введите дату в формате день-месяц-год: ')
my_list=date.split('-')

my1=Data.set_date(my_list)

print(Data.check_date(my1))






