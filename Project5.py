# Passward Generator
import random
letter =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '^']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many nubers would you like in your password?\n"))
nr_symbols = int(input("How many symbol would you like in your password?\n"))

# # 1 method
password_list = []

for char in range(1, nr_letters + 1):
  password_list += random.choice(letter)

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbol)

for char in range(1, nr_letters + 1):
  password_list += random.choice(number)

# print(password_list)
# random.shuffle(password_list)
# print(password_list)


password = ""
for char in password_list:
  password += char

print(f"Your password is:- {password}")

# # 2 method
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letter)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbol)

# for char in range(1, nr_letters + 1):
#   password += random.choice(number)

# print("YOUR PASSWORD IS:- ",password)