harga = 60000

jumlah = int(input("masukkan jumlah : "))
print()

if jumlah >= 100 and jumlah < 200:
    diskon = 2/100
    total_harga = harga * jumlah
    potongan =  (total_harga * 2)/100
    total_bayar = total_harga - potongan
    
elif jumlah >= 200:
    diskon = 5/100
    total_harga = harga * jumlah
    potongan =  (total_harga * 5)/100
    total_bayar = total_harga - potongan
    
else:
    diskon = 0
    total_harga = harga * jumlah
    potongan = 0
    total_bayar = total_harga

print("<====> Informasi Transaksi <====>")
print("Harga            : ", "Rp.", harga)
print("Jumlah Barang    : ", jumlah, "Sak")
print("Diskon           : ", diskon, "%")
print("Total Potongan   : ", "Rp.", potongan)
print("Total Harga      : ", "Rp.", total_harga)
print("Total Bayar      : ", "Rp.", total_bayar)
