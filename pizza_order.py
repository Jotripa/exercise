#Ucapan salam
print("Selamat datang di Pizza Papa!")
ukuran = input("Ukuran apa yang anda inginkan ? s, m, l ? ")
tambah_topping = input("Apakah anda ingin menambahkan toping ? y/t ? ")
tambah_keju = input("Apakah anda ingin menambahkan keju ? y/t ? ")
tagihan = 0
#Pengkondisian
if ukuran == "s":
    tagihan = 50000
elif ukuran == "m":
    tagihan = 75000
else:
    tagihan = 100000

if tambah_topping == "y":
    if ukuran == "s":
        tagihan += 5000
    else:
        tagihan += 7000
else:
    tagihan += 0

if tambah_keju == "y":
    tagihan += 2000
else:
    tagihan += 0

print(f"Total harga adalah : Rp. {tagihan}")