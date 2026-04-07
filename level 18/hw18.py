#1
for i in range(200, 501):
    if i % 4 == 0 and i % 7 == 0:
        print(i)



i = 200
while i <= 500:
    if i % 4 == 0 and i % 7 == 0:
        print(i)
    i += 1

#2
for i in range(300, 1001):
    if i % 3 == 0 or i % 10 == 0:
        print(i)



i = 300
while i <= 1000:
    if i % 3 == 0 or i % 10 == 0:
        print(i)
    i += 1

#3
for i in range(1, 51):
    if i % 2 == 0:
        print("Even:", i)
    else:
        print("Odd:", i)

#4?




#5

num = int(input("number: "))
if num % 2 == 0 and num % 3 == 0:
      print("Good")
      
elif num % 2 == 0:
    print("Two")

elif num % 3 == 0:
    print("Three")

else:
    print("None")

#6
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
         print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#7?


#8

num = int(input("number : "))

for i in range(1, num + 1):
    if i % 4 == 0:
        print(i)

#9

for i in range(5):
    num = int(input("enter a number: "))

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")




