#Greetings
print("Welcome to the split_bill.py")
#Input your bill
bill = float(input("Input your bill(Max < 1 jt) : Rp"))
#Input tip
tip = int(input("What percent you'd like to give ? 10, 12, 15?"))
#Input number of people
people = int(input("Number of people : "))
#Calculating tip 
tip_percent = tip / 100
#Calculating total tip amount
tip_amount = bill * tip_percent
#Calculating total bill
total_bill = bill + tip_amount
#Calculating split bill
bill_per_person = total_bill / people
final = round(bill_per_person, 2)
final = "{:.3f}".format(bill_per_person)
print(f"Each People must pay : Rp.{final}")
