goods = []
characteristic = {'name': '', 'price': '', 'amount': ''}
listname = []
listprise = []
listamount = []

nm=None
pr=None
am=None

count=1

while True:
    nm = input("Введите наименование товара, для завершения ввода ввебите букву Q:  ")
    if nm=='Q'or nm=='q':
        break
    listname.append(nm)
    pr = input("Введите цену товара: ")
    listprise.append(pr)
    am = input("Введите количество товара: ")
    listamount.append(am)
    characteristic = {'name': nm, 'price': pr, 'amount': am}
    goods.append(count)
    goods.append(characteristic)
    count +=1

print (goods)
sortdict= {'name': listname, 'price': listprise, 'amount': listamount}
print(sortdict)
