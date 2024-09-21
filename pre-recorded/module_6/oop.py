
class myClass:
    x = 10
    y = 20

    def addTwo(self, a, b):
        print(self.x + self.y + a)

    def addNew(self):
        self.addTwo(5, 6)

obj = myClass()
obj.addTwo(20, 30)
obj.addNew()