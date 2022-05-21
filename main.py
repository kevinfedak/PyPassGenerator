# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


your_chars = []

passw_lenght = nr_letters + nr_symbols + nr_numbers

for letter in range (nr_letters):
    your_chars.append(letters[random.randint(0, len(letters) - 1)])

for number in range (nr_numbers):
    your_chars.append(numbers[random.randint(0, len(numbers) - 1)])

for symnol in range (nr_numbers):
    your_chars.append(symbols[random.randint(0, len(symbols) - 1)])

print(your_chars)

random_password = []

for char in range (passw_lenght):
    random_password.append(your_chars[random.randint(0, passw_lenght-1)])

print(''.join(random_password))
