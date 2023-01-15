#Pengiriman Barang

nama_pengirim = input("Masukkan Nama Pengirim : ")
print()
nama_penerima = input("Masukkan nama Penerima : ")
print()
alamat_pengirim = input("Masukkan Alamat Lengkap Pengirim : ")
print()
alamat_penerima = input("Masukkan alamat Lengkap Penerima : ")
print()
berat_barang = int(input("Masukkan Berat Barang : "))
ongkos_kirim = 8000
print()
total_ongkos_kirim = ongkos_kirim * berat_barang


print("===============================")
print()
print("Detail Pengiriman Barang")
print()
print("===============================")
print()
print("Nama Pengirim      : ", nama_pengirim)
print("Nama Penerima      : ", nama_penerima)
print("Alamat Pengirim    : ", alamat_pengirim)
print("Alamat Penerima    : ", alamat_penerima)
print("Berat Barang       : ",berat_barang, "kg")
print("Ongkos Kirim       : Rp.", ongkos_kirim, "per kg")
print("Total Ongkos Kirim : Rp.",total_ongkos_kirim)
print()
print("===============================")