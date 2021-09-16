import random

chars = "asdfghkljqwertyuiopmnbcxz<#${|>ACSDFGHBVXZNMJKLOYREWQPU!@%^&*(_+1234576980"

num = input("Enter number of password to generate ")
num = int(num)

length = input("Enter password length ")
length = int(length)

gen_password = []

for pwd in range(num):
    password = ""

    for i in range(length):
        password += random.choice(chars)

    gen_password.append(password)


print("Generated Passwords : ")
for p in gen_password:
    print(p)
