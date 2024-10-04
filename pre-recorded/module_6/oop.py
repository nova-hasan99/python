print('.......................public......................')
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

print('.......................constructor......................')
class constructor_test:
    x = 20
    y = 30
    # here add value of z
    def __init__(self, a, b, z):           # call __init__ when use constructor method only
        print(self.x+a + self.y+b)
        self.z = z                         # add a variable in class using constructor method

cons = constructor_test(10, 20, 30)
print(cons.z)

print('.......................static......................')
class static_test:
    x = 10
    y = 20

    @staticmethod
    def addTwo():
        z = static_test.x + static_test.y
        print(z)

static_test.addTwo()

print('.......................inheritance......................')
class father:
    x = 10
    y = 20

    def add(self):
        print(self.x + self.y)
    
    def __init__(self):
        print('father constructor')

class mother:
    a = 10
    b = 20

    def mul(self):
        print(self.a * self.b)

class son(father, mother):
    #pass                       # if no activity needed this class so call only 'pass'

    def addTwo_bySon(self):
        s = self.x + self.a
        print(s)

    def __init__(self):
        print('son constructor')  # if a constructor have in parents class and child class both so parents constructor not initialize in child class
        super().__init__()        # if you want uisng parent constructor in child class so using 'super()' method

inheritance = son()
inheritance.addTwo_bySon()
inheritance.add()
inheritance.mul()

print('.......................protected, privet......................')
#    we can use protected mathod 'parent' & 'child' class both
#    we can't use privet mathod 'parent' & 'child' class both
#    privet only use for own class
class car:
    _brand = 'Toyota'         # '_' means protected
    __brand = 'BMW'           # '__' means privet

    def display(self):
        print(self.__brand)
class brand(car):
    def display(self):
        print(self._brand)
    
obj = car()
obj2 = brand()

obj.display()
obj2.display()

print('.......................over Loading......................')
class overLoading:
    x = 10
    y = 20

    def addTwo(self, a=0, b=0):
        print(self.x + self.y + a + b)

    def chack(self, *a):
        print(a)

obj = overLoading()
obj.addTwo()
obj.addTwo(1)


obj.chack(1)
obj.chack(1, 2)
obj.chack(1, 2, 3)
