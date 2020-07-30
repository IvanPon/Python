class Matrix:
    def __init__(self, a):
        self.a = a
        print(a)

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.a)):
            for j in range(len(self.a[0])):
                try:
                    summa = other.a[i][j] + self.a[i][j]
                    numbers.append(summa)
                except:
                    try:
                        numbers.append(self.a[i][j])
                    except:
                       numbers.append(other.a[i][j])
                if len(numbers) == len(self.a) and len(numbers) == len(other.a):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


m1 = Matrix([[3, 2, 3], [3, 4, 4], [7, 5, 7]])
m2 = Matrix([[3, 5, 4], [2, 4, 6], [1, 3]])



print(m1 + m2)
