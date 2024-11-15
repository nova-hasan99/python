
def multiplection(n):
    for i in range(1, 11):
        print("{} x {} = {}".format(n, i, n * i))

n = input("Enter number: ")
n = int(n)

while n != 0:
    multiplection(n)
    print(" ")
    n = input("Enter number: ")
    n = int(n)

# for loop
subject = {'Phy': 90, 'En': 85, 'Math': 95}
for subject, marks in subject.items():
    print("{}: {}". format(subject, marks))

#range
n = input("Number for 'reange' test: ")
n = int(n)
print("for 'break' test")
for n in range(10):
    if n == 5:
        break
    print(n)

print("for 'continue' test")
for n in range(10):
    if n == 5:
        continue
    print(n)



