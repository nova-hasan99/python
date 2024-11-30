
class myClass:
    x = 10
    y = 5

    def addTwo(self, a, b):
        z = self.x + b + self.y + a
        print(z)

    def sum(self):
        self.addTwo(1, 2)

    def __init__(self, v):
        z = self.x + self.y + v
        print("const", z)

obj = myClass(6)
obj.addTwo(10, 5)
obj.sum()