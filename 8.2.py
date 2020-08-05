class MyError(Exception):
    def __init__(self,txt):
        self.txt=txt

a=float(input('Введите делимое: '))
b=float(input('Введите делитель: '))
try:
    if b==0:
        raise MyError('На ноль делить нельзя')
except MyError as err:
    print(err)
else:
    print(a / b)
