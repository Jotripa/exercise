#Import module
import random
#Inputing names
names = input("Input everybody's name with comma and space: ")
name_split = names.split(", ")
#Take name
num_item = len(name_split)
random_name = random.randint(0, num_item - 1)
person_pay = name_split[random_name]
#Print
print(person_pay + " will buy our food today!")
