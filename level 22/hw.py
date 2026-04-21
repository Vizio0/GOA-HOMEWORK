#1
name = "Lasha"
print(name [0])


#2
surname  = "Chinchaladze"
print(surname[-1])

#3
programming = "python"
print(programming[3])

#4
GOA = "programming"
print(GOA[: 4])

#5
PC = "computer"
print(PC[5 : ])

#6
string = "helloworld"
print(string[4 : 6])

#7
country = "georgia"
print(country[2 : 6])

#8
favword = str(input("enter your fav word:" ))
if favword[0] == "A":
    print(favword[0 : 3])
elif favword[0] == "a":
    print(favword[0 : 3])
else:
    print(favword[-3:])

#9
edu = "education"
print(edu[1 : -1])

#10
job = "Developer"
website = job[:3] + job[-3:]
print(website)


#11
sentence  = ("GOA the besht bro")
print(sentence[:3])

#12

alphabet = "abcdef"
print(alphabet[::2])

#13

mylist = [10, "hi", 3.15, True, "world", 50, False, 7]


midelem = mylist[2:6]

print(midelem)