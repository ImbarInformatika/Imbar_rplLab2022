#Menghitung gaji karyawan dengan lemburnya

gaji_lembur = 55000
gaji_pokok = int(input("Masukkan Gaji : "))
lama_lembur = int(input("Masukkan Berapa Jam Lembur : "))

print()
print("<===> Gaji Karyawan Yang Lembur <===>")
print("Jumlah Gaji Pokok : ", "Rp.",gaji_pokok)
print("Gaji Lembur       : ","Rp.", gaji_lembur * lama_lembur)
print("Total Gaji        : ", "Rp.", gaji_pokok+(gaji_lembur * lama_lembur))