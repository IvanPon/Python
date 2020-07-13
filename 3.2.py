monthdict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
             9: 'September', 10: 'October', 11: 'November', 12: 'December'}
while True:
    numbmonth = input('Enter number of month (1-12) :')
    if numbmonth.isdigit():
        numbmonth = int(numbmonth)
        if numbmonth > 0 and numbmonth < 13:
            break
    print('invalid input. ')
month = monthdict.get(numbmonth)
print(month)
