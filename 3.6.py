def word(txt):
    txt = txt[:1].upper() + txt[1:]
    return txt


def sentence(snt):
    sent = []
    snt = snt.split()
    for i in snt:
        sent.append(word(i))
    return sent


text = input('Введите слово из маленьких букв: ')
print(word(text))

text2 = input(('Введите предложение состоящее из маленьких букв: '))
print(' '.join((sentence(text2))))
