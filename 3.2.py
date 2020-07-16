def pers_info(name='Ivan', sname='Ponomarev', byear=1981, hometown='Belgorod', email='123@mail.ru', tel='12535'):
    print(f'Имя: {name} Фамилия: {sname} Год рождения: {byear} Город проживания: {hometown} email: {email} телефон: {tel}')


name = input('Введите ваше имя: ')
sname = input('Введите вашу фамилию: ')
byear = input('Введите год рождения: ')
hometown = input('Введите город жительства: ')
email = input('Введите email: ')
tel = input('Введите телефон: ')

pers_info(name, sname, byear, hometown, email, tel)
