def sm(str):
    for i, number in enumerate(str, 1):
        if number.isdigit():
            continue
        else:
            str = str[:i - 1]
            return str
    return str


summa = 0

while True:
    str = input('Введите строку чисел, разделенных пробелом: ').split()
    newstr = (sm(str))
    newstr = [int(elem) for elem in newstr]

    if len(str) != len(newstr):
        summa = summa + sum(newstr)
        print(f'Работа программы завершена \nИтоговая сумма элементов - {summa}')
        break

    summa = summa + sum(newstr)
    print(summa)
