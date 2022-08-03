#Input weight and height
weight = float(input("Input your weight(Kg): "))
height = float(input("Input your height(M): "))
#BMI Calculating
bmi = round(weight / height ** 2)
print("Your BMI are " + str(bmi))
#Conditioning
if bmi < 18.5:
    print("You are Underweight")
elif bmi < 25:
    print("You have Normal Weight")
elif bmi < 30:
    print("You are Overweight")
elif bmi < 35:
    print("You are Obese")
elif bmi > 35:
    print("You are Clinically Obese")
else:
    print("Error")
