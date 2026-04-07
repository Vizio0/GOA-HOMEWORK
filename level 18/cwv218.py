for i in range(1, 101):

    if i % 2 == 0:
        print(i, " luwia")
    else:
        print(i, " kentia")


positive = 0
negative = 0

count = 0
while count < 10:
    num = int(input("შეიყვანეთ რიცხვი: "))
    
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    
    count += 1

print("დადებითი რიცხვების რაოდენობა:", positive)
print("უარყოფითი რიცხვების რაოდენობა:", negative)