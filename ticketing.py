#Greetings
print("Welcome to jaya harapan indah's roller coaster!")
#Input height
height = int(input("Input your height: "))
bill = 0
#Conditioning
if height >= 120:
    age = int(input("Input your age: "))
    if age < 12:
        bill = 20000
        print("Your ticket are Rp. 20.000")
    elif age <= 18:
        bill = 50000
        print("Your ticket are Rp. 50.000")
    else: 
        bill = 75000
        print("Your ticket are Rp. 75.000")
    print_tiket = input("Would you like to print your ticket ? y/n? ")
    if print_tiket == "y":
        bill += 3000
        print(f"Your total bill are {bill}")

else:
    print("You cannot ride this roller coaster yet!")
