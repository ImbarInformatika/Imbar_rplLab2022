angka = [3, 5, 8, 9, 10]
print("sebelum ada perubahan : ", angka)

angka.append(3) #menambahkan satu elemen di bagian akhir list
print("setelah mengunakan append : ", angka)

angka.insert(2, 17) #menambahkan satu elemen pada posisi atau index yang kita inginkan
print("setelah mengunakan insert : ", angka)

angkaku = [19, 4]
angka.extend(angkaku) #menambahkan data yan ada pada list lain
print("setelah mengunakan extend : ", angka)
