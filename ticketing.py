#Ucapan Salam
print("Selamat datang wahanan roller coaster taman jaya harapan!")
#Inputing tinggi badan
height = int(input("Masukkan tinggi badanmu: "))
bill = 0
#Pengkondisian
if height >= 120:
    age = int(input("Masukkan umur anda: "))
    if age < 12:
        bill = 20000
        print("Harga tiketmu adalah Rp. 20.000")
    elif age <= 18:
        bill = 50000
        print("Harga tiketmu adalah Rp. 50.000")
    else: 
        bill = 75000
        print("Harga tiketmu adalah Rp. 75.000")
    print_tiket = input("Apakah anda menginginkan tiket untuk di print ? y/t? ")
    if print_tiket == "y":
        bill += 3000
        print(f"Total tagihan anda adalah {bill}")

else:
    print("Kamu belum bisa menaiki wahana ini")