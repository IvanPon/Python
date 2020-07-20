def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
        yield f


n = int(input("Укажите факториал какого числа вычислить: "))
q=1
for i in fact(n):
    print(f'{q}!={i}')
    q+=1