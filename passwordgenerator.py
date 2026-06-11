import random
letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"    
symbols="!#$%&()*+"
print("\n***Password Generator***")
num_letters=int(input("\nHow many letters would you like in your password? "))    
num_numbers=int(input("How many numbers would you like in your password? "))
num_symbols=int(input("How many symbols would you like in your password? ")) 
password_list=[]
for i in range(num_letters):
    ch=random.choice(letters)
    password_list.append(ch)
for i in range(num_numbers):
    ch=random.choice(numbers)
    password_list.append(ch)
for i in range(num_symbols):
    ch=random.choice(symbols)
    password_list.append(ch)
random.shuffle(password_list)
password=""
for ch in password_list:
    password=password + ch
print("\nGenerated Password:", password)