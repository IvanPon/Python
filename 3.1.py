def division (x,y):
    try:
        x/y
    except ZeroDivisionError:
        return 'делить на ноль нельзя'
    return (x/y)

x=input('Введите делимое: x=')
x=float(x)

y=input('Введите делитель: y=')
y=float(y)

print(f'x/y= {division(x,y)}')