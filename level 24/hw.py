#mutable----shegidzlia rom shecvalo
#immutable---ar shegidzlia rom shecvalo
#len geubneba ramdeni asoa teqstshi, an ramdeni elementia siashi
#3) შექმენით ცვლადი სადაც შეინახავთ რაიმე სიტყვას. დაპრინტეთ რამდენი სიმბოლოა ამ სიტყვაში
word = "hello"
print(len(word))
#4) შექმენით ცვლადი სადაც მომხმარებელს შემოაყვანინებთ რაიმე წინადადაებას. დაპრინტეთ სიმბოლოების რაოდენობა ამ წინადადებაში
sentence = input("enter a sentence: ")
print(len(sentence))

#5) შექმენით სია სადაც შეინახავთ რიცხვებს. for loop ის გამოყენებით დაითვალეთ რამდენი დადებითი და რამდენი უარყოფითი რიცხვია ამ სიაში
numbers = [3, -1, 7, -5, 0, 2, -8]

positive = 0
negative = 0

for i in numbers:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1

print("positive numbers:", positive)
print("positive numbers:", negative)

#6) შექმნეით სია სადაც შეინახავთ რიცხვებს. დაითვალეთ რამდენი რიცხვი არის ამ სიაში ისეთი, რომელიც იყოფა 5-ზე  ???????????????????
numberos =[5, 15, 67, 6767667, 40, 25]
for x in range(len(numberos)):
    if numberos[x] % 5 == 0:
        print(numberos[x])




#7) შექმენით სია სადაც შეინახავთ რიცხვებს. დაპრინტეთ მხოლოდ ისეთი რიცხვები, რომლებიც იყოფა 4-ზეც და 7-ზეც
numeros = [4, 7, 14, 28, 35, 56, 8]

for n in range(len(numeros)):
    if numeros[n] % 4 == 0 and numeros[n] % 7 == 0:
        print(numeros[n])

#8) შექმენით სია სადაც შეინახავთ ნებისმიერ მნიშვნელობებს. დაპრინტეთ მხოლოდ ის ელემენტები, რომლებიც იმყოფებიან ლუწ ინდექსზე
random = ["sui", 10, "hello", 6767, "x", 40, "z"]

for p in range(len(random)):
    if p % 2 == 0:
        print(random[p])

#9) შექმენით სია სადაც შეინახავთ სიტყვებს. დაითვალეთ იმ სიტყვების რაოდენობა, რომელთა სიგრძეც მეტია 5-ზე
words = ["hello", "python", "cat", "programming", "sun"]

for w in words:
    if len(w) > 5:
        print(w)


#10) შექმენით ცვლადი, რომელშიც შეინახავთ რაიმე წინადადებას. for ლუპის გამოყენებით დაპრინტეთ თითოეული სიმბოლო
text = input("enter a sentence: ")

for y in range(len(text)):
    print(text[y])

#11) შექმენით ცვლადი, რომელშიც შეინახავთ რაიმე წინადადებას. for ლუპის გამოყენებით დაპრინტეთ თითოეული სიმბოლო გარდა გამოტოვებისა
something = input("enter a sentence: ")

for j in range(len(text)):
    if text[j] != " ":
        print(text[j])

#12) შექმენით სია სადაც შეინახავთ სიტყვებს. for ლუპის გამოყენებით დაპრინტეთ: 'სიტყვა - სიგრძე'

words = ["cotton", "son", "field"]

for w in words:
    print(w, "-", len(w))