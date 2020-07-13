text = input('Enter a sentence: ')

count = 0
start = 0

for i in text:
    count += 1
    if i == " ":
        print(text[start:count] if (count - start) < 11 else text[start:start + 10])
        start = count

print(text[start:count])
