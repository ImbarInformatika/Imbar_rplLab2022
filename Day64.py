barang = ["polpen", "buku", "hp", "laptop"]

  	
cari1 = input("masukkan barang yang di cari : ")
if cari1 in barang:
    print(f"{cari1} ditemukan pada index ke- {barang.index(cari1)}")
else :
	print("barang tidak ditemukan")