#Greetings
print("Welcome to Papa Pizza!")
ukuran = input("What size you want ? s, m, l ? ")
tambah_topping = input("Do you want to add topping ? y/n ? ")
tambah_keju = input("Do you want to add extra cheese ? y/n ? ")
tagihan = 0
#Conditioning
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

print(f"Your total Bill are : Rp. {tagihan}")
