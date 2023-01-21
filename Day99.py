#Menghitung bom bersama buru

total_bombersama = float(input("Masukkan jumlah bom bersama : "))
print()
total_harian = float(input("Masukkan keseluruhan harian buru : "))
print()
print()
total_bomperorang1hari = total_bombersama / total_harian
print("Total bom bersama per hari adalah : ", total_bomperorang1hari)
print()
print()
jumlah_harianperorang = int(input("Masukkan jumlah harian perorang : "))
print()
print()
total_utangdaribombersama = total_bomperorang1hari * jumlah_harianperorang
print("Jumlah utang perorang di bom bersama adalah : ", total_utangdaribombersama)
