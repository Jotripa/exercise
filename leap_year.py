#Input tahun
year = int(input("Masukkan tahun: "))
#Pengkondisian
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Ini adalah tahun kabisat")
        else:
            print("Ini Bukanlah tahun kabisat")
    else:
        print("Ini adalah tahun kabisat")    
else:
    print("Ini bukanlah tahun kabisat")    