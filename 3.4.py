def exp_1(x,y):
    y=abs(y)
    return (1/(x**y))

def exp_2(x,y):
    z=1
    y=abs(y)
    while y>0:
        z*=x
        y-=1
    return 1/z


while True:
    x=input('Введите действительное положительное число x: ')
    try:
        x=float(x)
    except ValueError:
        print('необходимо ввести действительное положительное число')
        continue
    if x>0:
        x=float(x)
        break
    else:
        print('Число должно быть больше нуля')

while True:
    y=input('Введите целое отрицательное число y: ')
    try:
        y = int(y)
    except ValueError:
        print('необходимо ввести целое отрицательное число')
        continue
    if y < 0:
        y = int(y)
        break
    else:
        print('Число должно быть меньше нуля')

print(exp_1(x,y))
print(exp_2(x,y))