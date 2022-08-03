#Greetings
print("Welcome to Love Calculator!")
#Input name
name1 = input("Your name: ")
name2 = input("Your date's name: ")
#Convert to lowercase
combine_str = name1 + name2 
lower_case_str = combine_str.lower()
#Counting true string
t = lower_case_str.count("t")
r = lower_case_str.count("r")
u = lower_case_str.count("u")
e = lower_case_str.count("e")
true = t + r + u + e
#Counting love string
l = lower_case_str.count("l")
o = lower_case_str.count("o")
v = lower_case_str.count("v")
e = lower_case_str.count("e")
love = l + o + v + e
#Counting true love value
love_score = int(str(true) + str(love))
print(love_score)
#Conditioning
if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, Go get yourself time and date!")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your love score is {love_score}, You two are matching!!!")
else:
    print(f"Your love score is {love_score}")
