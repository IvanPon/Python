from sys import argv

print(argv)

script_salary, amount_hours, rate, award = argv

print("Имя скрипта: ", script_salary)
print("Выработка в часах: ", amount_hours)
print("Ставка в час: ", rate)
print("Премия: ", award)

salary=int(amount_hours)*int(rate)+int(award)

print(f'Зарплата работника составит {salary} рублей')