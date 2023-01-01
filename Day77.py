#menghitung harga luas tanah dan pajaknya

harga_permeter = 300000

panjang = float(input("masukkan panjang : "))
lebar = float(input("masukkan lebar : "))
luas = panjang * lebar
total_harga = luas * harga_permeter
print()

if total_harga > 50000000 and total_harga < 100000000:
    diskon = 3/100
    potongan =  (total_harga *3)/100
    total_bayar = total_harga - potongan
    
elif total_harga > 100000000:
    diskon = 5/100
    potongan =  (total_harga *5)/100
    total_bayar = total_harga - potongan
    
else:
    diskon = 1/100
    potongan = (total_harga * 1)/100
    total_bayar = total_harga - potongan

print("<====> Informasi Transaksi <====>")
print("Harga            : ", "Rp.", total_harga)
print("Luas Tanah       : ", luas, "m²")
print("Diskon           : ", diskon, "%")
print("Total Potongan   : ", "Rp.", potongan)
print("Total Bayar      : ", "Rp.", total_bayar)
