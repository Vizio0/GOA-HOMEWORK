texti = input("გთხოვთ, შეიყვანეთ წინადადება ან სიტყვა: ")
upper_count = sum(1 for c in texti if c.isupper())
lower_count = sum(1 for c in texti if c.islower())
print(f"დიდი ასოები: {upper_count}")
print(f"პატარა ასოები: {lower_count}")

