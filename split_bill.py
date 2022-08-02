#ucapan salam
print("Selamat datang di split_bill.py")
#Input tagihan
bill = float(input("Masukkan jumlah tagihan(Maksimal 1 jt) : Rp"))
#Input tip
tip = int(input("Berapa persen tip yang ingin diberikan? 10, 12, 15?"))
#Input jumlah orang
people = int(input("Jumlah orang : "))
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
print(f"Tiap orang harus membayar : Rp.{final}")