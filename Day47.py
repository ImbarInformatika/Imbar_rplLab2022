print("<=====>MENGECEK NILAI MAHASISWA<=====>")
nama = input("NAMA : ")
nim = input("NIM  : ")
kelas = input("KELAS : ")

print()
tugas = int(input("Masukkan nilai TUGAS : "))
uts = int(input("Masukkan nilai UTS : "))
final = int(input("Masukkan nilai FINAL : "))
nilai = (0.15 * tugas) + (0.35 * uts) + (0.50 * final)

if nilai >= 85 and nilai < 100:
    kamu = "LULUS MEMUASKAN"

elif nilai >= 80 and nilai < 85:
    kamu = "LULUS BAIK"

elif nilai >= 70 and nilai < 85:
    kamu = "LULUS"

else :
    kamu = "TIDAK LULUS"
    
print()
print("<=====>MENETAPKAN DENGAN INI<=====>")
print("NAMA : ", nama)
print("KELAS : ", kelas)
print("KELAS : ", nim)
print()
print("DENGAN INI DI NYATAKAN <===>    ", kamu, "   <===> DENGAN NILAI", nilai)
