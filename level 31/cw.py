sentence = input("enter a sentence:")

word = input("enter a word : ")

if sentence.startswith(word):
    print("the sentence starts with this word")
else:
    print("the sentence doesnt start with this word")


winadadeba = input("Enter a sentence: ")
sityva = input("Enter a word: ")

if winadadeba.endswith(sityva):
    print("The sentence ends with this word")
else:
    print("The sentence does not end with this word")


colors = input("Enter your favorite colors: ")

colors_list = colors.split()

print(colors_list)