for i in range(100, 400):
    if i % 5 == 0 and i % 3 != 0:
        print(i)


for i in range(1, 100):
    if i % 2 == 0 and i % 5 == 0:
        print("EvenFive")
    elif i % 2 == 0:
        print("Even")
    elif i % 5 == 0:
        print("Five")
    else:
        print(i)


N = int(input("enter a number: "))
ramdenia = 0

for i in range(1, N + 1):
    if i % 3 == 0:
        ramdenia += 1

print("raodenoba:", ramdenia)


for i in range(1, 50):
    if i % 4 != 0:
        print(i)


number = int(input("enter a number: "))
sul = 0

while number >= 0:
    sul += number
    number = int(input("enter a number: "))

print("jami:", sul)