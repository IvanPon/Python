def my_func(x, y, z):
    a = [x, y, z]
    a.remove(min(a))
    return sum(a)

x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
z = int(input('Введите третье число: '))

print(my_func(x, y, z))
