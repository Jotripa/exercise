#Input year
year = int(input("Input year: "))
#Conditioning
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is a Leap Year!")
        else:
            print("This is not a Leap Year1")
    else:
        print("This is a Leap Year!")    
else:
    print("This is not a Leap Year")    
