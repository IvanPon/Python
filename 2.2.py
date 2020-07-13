a = []

while True:
    element = input("Enter an line's element. For finish enter a quit:   ")
    if element == "quit":
        break
    else:
        a.append(element)
print(a)

b = []
add = False

if len(a) % 2 == 1:
    add = True
    lastel = a.pop()

for i in range(0, len(a), 2):
    x = a[i]
    y = a[i + 1]
    b.extend([y, x])

if add == True:
    b.append(lastel)

print(b)
