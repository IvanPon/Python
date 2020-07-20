from itertools import count
from itertools import cycle

start_numb=int(input('Введите начальное число: '))
finish_numb=int(input('Введите конечное число: '))

for el in count (start_numb):
    if el>finish_numb:
        break
    else:
        print(el)

text=input('Введите строку: ')
numb=int(input('Введите кол-во повторяемых элементов: '))
c=0
for el in cycle (text):
    if c>=numb:
        break
    print(el)
    c+=1
