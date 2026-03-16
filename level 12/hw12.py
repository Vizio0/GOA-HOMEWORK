#sequencing nishnavs kodis mimdevrobit wakitxvas, selection-programa igebs gadawyvetilebas(romelic umetes shemtxvevashi chveni micemuli archevania)
#indentacias viyenebt if/else shi






#math_score = int(input("enter your score in math: "))
#english_score = int(input("enter your score in english: "))
#physics_score = int(input("enter your score in physics : "))

#if math_score >= 90 and english_score >= 90 and physics_score >=90:
   # print("you are an amazing student!")
    #print("you have a high score in all subjects!")

#elif math_score >= 70 and english_score >= 70 and physics_score >= 70:
   # print("good results!")
   # print("school year is successful")

#elif math_score <= 50 and english_score <= 50 and physics_score <= 50:
    #print("you have a bad score in one of the subjects")
   # print("you need to study more")

#else:
   # print("results are low!!!!")
   # print("you can do better")

    


#age = int(input("enter your age: "))
#license = str(input("do you have a license?(yes or no): "))
#drunk = str(input("are you drunk?: "))

#if age >= 18 and license == ("yes") and drunk == "no":
    #print("you can drive a car")
    #print("wish you a safe trip")

#elif age >= 18 and license == "no" and drunk == "no":
    #print("you are old enough")
    #print("magram martvis mowmoba ar gaqvs")

#elif drunk == "yes" and age < 18 and license == "no":
    #print("driving a car is forbidden")
    #print("it might be dangerous")

#else:
    #print("couldnt identify your data")
    #print("try again")

    

price = float(input("Enter product price: "))
quantity = int(input("Enter quantity of items: "))
member = str(input("Are you a member? (yes or no): "))

if price >= 100 and quantity >= 3 and member == "yes":
    print("You received a big discount")
    print("Thank you for being a loyal customer")

elif price >= 100 and quantity >= 3 and member == "no":
    print("You received a discount")
    print("You would receive more if you were a member")

elif price < 50 or quantity == 1 or member == "no":
    print("NO DISCOUNT FOR YOU")
    print("BUY MORE PRODUCTS")

else:
    print("You received a small discount")
    print("Thank you for buying")