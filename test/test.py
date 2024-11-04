
class myClass:
    x = 10
    y = 5

    def addTwo(self, a, b):
        z = self.x + b + self.y + a
        print(z)

    def sum(self):
        self.addTwo(1, 2)

obj = myClass()
obj.addTwo(10, 5)
obj.sum()