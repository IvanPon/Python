rating = [7, 5, 3, 3, 2]

while True:
    nr = input('enter a new element of rating, for quit enter any letter: ')
    if nr.isdigit():
        nr = int(nr)
        i = len(rating) - 1
        while i >= 0:
            if rating[i] >= nr:
                rating.insert(i + 1, nr)
                break
            elif rating[i] < nr and i == 0:
                rating.insert(0, nr)
                break
            else:
                i -= 1
        print(rating)
    else:
        break
