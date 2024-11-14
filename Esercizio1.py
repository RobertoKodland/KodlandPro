import random
element = "abcdefghijklmnopqrst0123456789"
widthEl = int(input("Quanto la vuoi lunga la password?"))

password = ""
for i in range(widthEl):
    password += random.choice(element)

print(password)
