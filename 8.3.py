class check:
    def __init__(self, a):
        self._a = a

    def isnum(self, a):
        try:
            a = int(a)
        except ValueError:
            print('Введено не число')
            return False
        return a


list = []
while True:
    num = input('Введите целочисленное число (для выхода введите stop): ')
    if num == 'stop':
        break
    if check(num).isnum(num) != False:
        list.append(check(num).isnum(num))

print(list)
