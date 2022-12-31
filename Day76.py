#menghitung harga permeter tanah 
harga = int(input("Masukkan Harga Tanah : "))

luas_tanah = float(input("Masukkan Luas Tanah : "))

harga_permeter = harga / luas_tanah
print()

print("<====> Informasi Harga Tanah <====>")
print("Harga            : ", "Rp.", harga)
print("Luas Tanah       : ", luas_tanah, "m²")
print("Harga_permeter   : ", "Rp.", harga_permeter )
