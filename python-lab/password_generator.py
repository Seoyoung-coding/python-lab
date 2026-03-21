# x$d24g*f9
# Every time you generate a password, the positions of the symbols, numbers, and letters are different.
# This will make the password more difficult for hackers to crack.
# duplicate

# Given
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

## My solution
import random
# Randomly extract a user-specified number from the list (duplicates allowed)
choice_list1 = [random.choice(letters) for i in range(nr_letters)]
choice_list2 = [random.choice(numbers) for j in range(nr_numbers)]
choice_list3 = [random.choice(symbols) for k in range(nr_symbols)]

# Combine three lists
final_list = choice_list1 + choice_list2 + choice_list3

# Converting a list to a string
generated_password = ''.join(str(s) for s in final_list)
print(generated_password)