import random
import string

website = input("Enter website name: ")

charValues=string.ascii_letters + string.digits + string.punctuation

password=""

pass_len=12

for i in range(pass_len):
    password+=random.choice(charValues)


print("Your random password is:", password)

with open("password_memo.txt", "a") as file:
    file.write(f"{website} : {password}\n")

