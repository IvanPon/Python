
class Compl:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
          return Compl(self.a + other.a)

    def __str__(self):
        return f"Результат сложения: {self.a}"


mc_1 = Compl(complex(1,2))
mc_2 = Compl(complex(2,3))
mc_3 = Compl(complex(3,4))
print(mc_1+mc_2+mc_3)


